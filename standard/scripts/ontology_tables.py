#!/usr/bin/env python3
"""Generate AsciiDoc module summaries and term dictionaries from the AIM v3.0 ontology.

Usage (from the standard/ directory):
    python3 scripts/ontology_tables.py ../v3.0 sections/generated
"""
import os
import sys

from rdflib import OWL, RDF, RDFS, Graph, URIRef
from rdflib.namespace import SKOS

# key -> (source file, display name)
MODULES = {
    "cross-domain": ("cross-domain.ttl", "Cross-Domain"),
    "agri-common": ("agriCommon.ttl", "AgriCommon"),
    "agri-feature": ("agriFeature.ttl", "AgriFeature"),
    "agri-crop": ("agriCrop.ttl", "AgriCrop"),
    "agri-intervention": ("agriIntervention.ttl", "AgriIntervention"),
    "agri-alert": ("agriAlert.ttl", "AgriAlert"),
    "agri-product": ("agriProduct.ttl", "AgriProduct"),
    "agri-property": ("agriProperty.ttl", "AgriProperty"),
    "agri-system": ("agriSystem.ttl", "AgriSystem"),
    "agri-pest": ("agriPest.ttl", "AgriPest"),
    "farm-animal": ("farmAnimal.ttl", "FarmAnimal"),
    "agri-profile": ("demeterAgriProfile.ttl", "AIM Agri Profile"),
}


def cell(text):
    return " ".join(str(text).split()).replace("|", "\\|")


def first(g, s, *preds):
    for p in preds:
        for o in g.objects(s, p):
            if getattr(o, "language", None) in (None, "en"):
                return o
    return ""


def curie(g, term):
    try:
        return g.namespace_manager.normalizeUri(term)
    except Exception:
        return f"<{term}>"


def terms(g, *types):
    found = set()
    for t in types:
        found |= {s for s in g.subjects(RDF.type, t) if isinstance(s, URIRef)}
    return sorted(found, key=lambda s: curie(g, s).lower())


def dictionary(g, key, kind, title, items, extra):
    out = [f"[[table_{key}_{kind}]]", f".{title}", '[cols="3,3,5,3",options="header"]', "|===",
           f"|Term |Label |Definition |{extra[0]}"]
    for s in items:
        label = first(g, s, RDFS.label, SKOS.prefLabel)
        definition = first(g, s, SKOS.definition, RDFS.comment)
        rel = ", ".join(sorted(f"`{curie(g, o)}`" for p in extra[1] for o in g.objects(s, p) if isinstance(o, URIRef)))
        out.append(f"|`{curie(g, s)}` |{cell(label)} |{cell(definition)} |{rel}")
    out.append("|===")
    return out


def main(src, dst):
    os.makedirs(dst, exist_ok=True)
    modules = []
    for key, (fname, name) in MODULES.items():
        g = Graph().parse(os.path.join(src, fname), format="turtle")
        ont = next(g.subjects(RDF.type, OWL.Ontology))
        classes = terms(g, OWL.Class)
        props = terms(g, OWL.ObjectProperty, OWL.DatatypeProperty)
        individuals = terms(g, OWL.NamedIndividual)
        imports = sorted(str(i) for i in g.objects(ont, OWL.imports))
        modules.append((key, name, fname, ont, g.value(ont, OWL.versionIRI), imports, classes, props))

        import_list = " +\n".join(f"`{i}`" for i in imports) or "none"
        out = [f"[[table_{key}_summary]]", f".{name} module summary", '[cols="2,5",options="header"]', "|===",
               "|Item |Value",
               f"|Ontology IRI |`{ont}`",
               f"|Version IRI |`{g.value(ont, OWL.versionIRI)}`",
               f"|Source |`v3.0/{fname}`",
               f"|Imports |{import_list}",
               f"|Classes |{len(classes)}",
               f"|Object and datatype properties |{len(props)}",
               f"|Named individuals |{len(individuals)}",
               f"|Description |{cell(first(g, ont, URIRef('http://purl.org/dc/terms/description')))}",
               "|==="]
        if classes:
            out += [""] + dictionary(g, key, "classes", f"{name} classes", classes,
                                     ("Superclasses", [RDFS.subClassOf]))
        if props:
            out += [""] + dictionary(g, key, "properties", f"{name} properties", props,
                                     ("Domain / range", [RDFS.domain, RDFS.range]))
        with open(os.path.join(dst, f"module_{key}.adoc"), "w") as f:
            f.write("\n".join(out) + "\n")

    out = ["[[table_modules]]", ".AIM version 3.0 ontology modules", '[cols="2,4,4,1,1",options="header"]', "|===",
           "|Module |Ontology IRI |Version IRI |Classes |Properties"]
    for key, name, fname, ont, ver, imports, classes, props in modules:
        out.append(f"|{name} |`{ont}` |`{ver}` |{len(classes)} |{len(props)}")
    out.append("|===")
    with open(os.path.join(dst, "modules.adoc"), "w") as f:
        f.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main(*sys.argv[1:3])
