---
title: Farm - GeoJSON (Schema)

language_tabs:
  - json: JSON
  - jsonld: JSON-LD
  - turtle: RDF/Turtle

toc_footers:
  - Version 0.1
  - <a href='#'>Farm - GeoJSON</a>
  - <a href='https://blocks.ogc.org/register.html'>Building Blocks register</a>

search: true

code_clipboard: true

meta:
  - name: Farm - GeoJSON (Schema)
---


# Farm - GeoJSON `ogc.model.agriculture.features.farm`

GeoJSON binding for Farm class

<p class="status">
    <span data-rainbow-uri="http://www.opengis.net/def/status">Status</span>:
    <a href="http://www.opengis.net/def/status/under-development" target="_blank" data-rainbow-uri>Under development</a>
</p>

<aside class="success">
This building block is <strong><a href="https://github.com/ogcincubator/aim-swg/blob/main/build/tests/model/agriculture/features/farm/" target="_blank">valid</a></strong>
</aside>

# Description

## Agriculture Information Model Closure

Defines dependencies for the complete Agriculture Information Model based on reusable modular components.





# Examples

## Simple Farm Instance GeoSPARQL schema



```json
{
  "id": "f1",
  "type": "Feature",
  "featureType": "saref4agri:Farm",
  "geometry": {
    "type": "Point",
    "coordinates": [
      11.3,
      44.12
    ]
  },
  "properties": {
    "name": "Wheat farm",
    "description": "A farm producing wheat"
  }
}
```

<blockquote class="lang-specific json">
  <p class="example-links">
    <a target="_blank" href="https://ogcincubator.github.io/aim-swg/build/tests/model/agriculture/features/farm/example_1_1.json">Open in new window</a>
    <a target="_blank" href="https://avillar.github.io/TreedocViewer/?dataParser=json&amp;dataUrl=https%3A%2F%2Fogcincubator.github.io%2Faim-swg%2Fbuild%2Ftests%2Fmodel%2Fagriculture%2Ffeatures%2Ffarm%2Fexample_1_1.json&amp;expand=2&amp;option=%7B%22showTable%22%3A+false%7D">View on JSON Viewer</a></p>
</blockquote>




```jsonld
{
  "id": "f1",
  "type": "Feature",
  "featureType": "saref4agri:Farm",
  "geometry": {
    "type": "Point",
    "coordinates": [
      11.3,
      44.12
    ]
  },
  "properties": {
    "name": "Wheat farm",
    "description": "A farm producing wheat"
  },
  "@context": "https://ogcincubator.github.io/aim-swg/build/annotated/model/agriculture/features/farm/context.jsonld"
}
```

<blockquote class="lang-specific jsonld">
  <p class="example-links">
    <a target="_blank" href="https://ogcincubator.github.io/aim-swg/build/tests/model/agriculture/features/farm/example_1_1.jsonld">Open in new window</a>
    <a target="_blank" href="https://json-ld.org/playground/#json-ld=https%3A%2F%2Fogcincubator.github.io%2Faim-swg%2Fbuild%2Ftests%2Fmodel%2Fagriculture%2Ffeatures%2Ffarm%2Fexample_1_1.jsonld">View on JSON-LD Playground</a>
</blockquote>




```turtle
@prefix geojson: <https://purl.org/geojson/vocab#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<file:///github/workspace/f1> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.13e+01 4.412e+01 ) ] .


```

<blockquote class="lang-specific turtle">
  <p class="example-links">
    <a target="_blank" href="https://ogcincubator.github.io/aim-swg/build/tests/model/agriculture/features/farm/example_1_1.ttl">Open in new window</a>
</blockquote>


Example from AIM  using a GeoJSON schema. 



# JSON Schema

```yaml--schema
$schema: https://json-schema.org/draft/2020-12/schema
description: Example of a sinmple GeoJSON Feature specialisation
$defs:
  MyFeature:
    allOf:
    - $ref: https://opengeospatial.github.io/bblocks/annotated-schemas/geo/features/feature/schema.yaml
    - properties:
        properties:
          name: string
          description: string
anyOf:
- $ref: '#/$defs/MyFeature'

```

> <a target="_blank" href="https://avillar.github.io/TreedocViewer/?dataParser=yaml&amp;dataUrl=https%3A%2F%2Fogcincubator.github.io%2Faim-swg%2Fbuild%2Fannotated%2Fmodel%2Fagriculture%2Ffeatures%2Ffarm%2Fschema.yaml&amp;expand=2&amp;option=%7B%22showTable%22%3A+false%7D">View on YAML Viewer</a>

Links to the schema:

* YAML version: <a href="https://ogcincubator.github.io/aim-swg/build/annotated/model/agriculture/features/farm/schema.yaml" target="_blank">https://ogcincubator.github.io/aim-swg/build/annotated/model/agriculture/features/farm/schema.yaml</a>
* JSON version: <a href="https://ogcincubator.github.io/aim-swg/build/annotated/model/agriculture/features/farm/schema.json" target="_blank">https://ogcincubator.github.io/aim-swg/build/annotated/model/agriculture/features/farm/schema.json</a>


# JSON-LD Context

```json--ldContext
{
  "@context": {
    "type": "@type",
    "id": "@id",
    "properties": "@nest",
    "geometry": {
      "@context": {
        "coordinates": {
          "@container": "@list",
          "@id": "geojson:coordinates"
        }
      },
      "@id": "geojson:geometry"
    },
    "bbox": {
      "@container": "@list",
      "@id": "geojson:bbox"
    },
    "Feature": "geojson:Feature",
    "FeatureCollection": "geojson:FeatureCollection",
    "GeometryCollection": "geojson:GeometryCollection",
    "LineString": "geojson:LineString",
    "MultiLineString": "geojson:MultiLineString",
    "MultiPoint": "geojson:MultiPoint",
    "MultiPolygon": "geojson:MultiPolygon",
    "Point": "geojson:Point",
    "Polygon": "geojson:Polygon",
    "features": {
      "@container": "@set",
      "@id": "geojson:features"
    },
    "links": {
      "@context": {
        "href": {
          "@type": "@id",
          "@id": "oa:hasTarget"
        },
        "rel": {
          "@context": {
            "@base": "http://www.iana.org/assignments/relation/"
          },
          "@id": "http://www.iana.org/assignments/relation",
          "@type": "@id"
        },
        "type": "dct:type",
        "hreflang": "dct:language",
        "title": "rdfs:label",
        "length": "dct:extent"
      },
      "@id": "rdfs:seeAlso"
    },
    "geojson": "https://purl.org/geojson/vocab#",
    "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
    "oa": "http://www.w3.org/ns/oa#",
    "dct": "http://purl.org/dc/terms/",
    "@version": 1.1
  }
}
```

> <a target="_blank" href="https://json-ld.org/playground/#json-ld=https%3A%2F%2Fogcincubator.github.io%2Faim-swg%2Fbuild%2Fannotated%2Fmodel%2Fagriculture%2Ffeatures%2Ffarm%2Fcontext.jsonld">View on JSON-LD Playground</a>

You can find the full JSON-LD context here:
<a href="https://ogcincubator.github.io/aim-swg/build/annotated/model/agriculture/features/farm/context.jsonld" target="_blank">https://ogcincubator.github.io/aim-swg/build/annotated/model/agriculture/features/farm/context.jsonld</a>

# For developers

The source code for this Building Block can be found in the following repository:

* URL: <a href="https://github.com/ogcincubator/aim-swg" target="_blank">https://github.com/ogcincubator/aim-swg</a>
* Path:
<code><a href="https://github.com/ogcincubator/aim-swg/blob/HEAD/_sources/features/farm" target="_blank">_sources/features/farm</a></code>

