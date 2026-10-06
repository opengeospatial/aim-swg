# Agriculture Information Model

The Agriculture Information Model (AIM) is a common vocabulary providing the basis for semantic interoperability across smart farming solutions.
AIM defines the data elements, including concepts, properties and relationships relevant to agri applications, as well as their associated 
semantics/meaning for information exchange.  This repository defines implementation bindings for native RDF as JSON-LD, OGC Features (GeoJSON and FG-JSON variants) and NGSI-LD.



This repository contains the modules comprising all the layers of the Agriculture Information Model (AIM). 

The Agriculture Information Model (AIM) is a common vocabulary providing the basis for semantic interoperability across smart farming solutions. 
AIM defines the data elements, including concepts, properties and relationships relevant to agri applications, as well as their associated 
semantics/meaning for information exchange.  Built upon a thorough analysis of the related state of the art and practice, and driven by the elicited 
stakeholder requirements in H2020 DEMETER project, AIM aims to establish the basis of a common agricultural data space and enable the interoperability 
of different systems, potentially from different vendors. This will in turn enable the analysis of data produced by those systems in an integrated 
manner to make economically and environmentally sound decisions.

AIM has been designed following a layered and modular approach, and is realised as a suite of ontologies implemented in line with best practices, 
reusing existing standards and well-scoped dominant models as much as possible and establishing alignments between them to enable their interoperability 
and the integration of existing data. AIM is scalable and can be easily extended in order to address additional needs and incorporate new concepts,
maintaining its consistency and compliance. In particular, AIM comprises the following layers:

* the meta-model layer defining the building blocks of AIM and enabling the back-and-forth conversion between datasets that are based on the property graph model and linked data datasets
* the cross-domain layer defining relevant concepts and properties that are common across multiple domains, and which enable the interoperability with existing standard models and vocabularies
* the domain layer defining agri-specific concepts and properties covering different aspects of interest of agri applications, and which enables the integration of relevant vocabularies in the sector.
* The pilot-specific layer defining additional concepts and properties that are of specific use for particular applications. 

Additionally, AIM defines a metadata model that can be used to describe datasets, services or applications in agri-related projects/applications.

The cross-domain module has been created by reusing and alignment existing standard ontologies/vocabularies, including: OGC/W3C sosa/ssn, OGC Geosparql,
W3C Time ontology, W3C Data Cube ontology, ISO 191xx standards, WGS84, QUDT, W3C PROV-O, as well as well-known vocabularies like FOAF, Schema.org, and Dublin Core.

The domain modules have been created by reusing well-known ontologies and models related to the agri-food sector, namely the ETSI standard [Saref4Agri](https://saref.etsi.org/saref4agri/v1.1.2/) and the underlying Smart Applications REFerence [SAREF ontology](https://saref.etsi.org/core/v3.1.1/),
[INPIRE/FOODIE ontology](http://agroportal.lirmm.fr/ontologies/FOODIE) and
[SmartDataModel (aka.FIWARE) agrifood related models](https://smartdatamodels.org/).

A key value provided by AIM is that it harmonises and aligns relevant cross-domain standards with domain-specific models 
bridging various views on the agriculture data and providing a formal representation enabling unambiguous translations between them.

AIM is published as both human and implementation-ready machine-actionable resources, including the formal specifications as ontology modules (OWL ontologies), 
JSON-LD contexts enabling services to exchange AIM-compliant data based on the already successful JSON format, and SHACL shapes enabling the validation 
of data against AIM semantics. AIM specification includes guidelines on how to find and identify relevant terms, how to create AIM-based JSON-LD content, 
as well as instructions to validate the generated content.

AIM was originally developed as part of H2020 DEMETER project, and is being reused and extended in many ohter projects related to agriculture, but also in other 
domains (reusing the cross-domain layer).


## Building Blocks

### `ogc.model.agriculture.external.smart-agrifood.crop` — SMART AgriCrop

**Type:** schema

Smart Data Models - Agri Food - Agri Crop model

### `ogc.model.agriculture.conceptual.plot` — Plot

**Type:** model

Conceptual model for Plot/Parcel (independent of JSON or other schema encoding).

### `ogc.model.agriculture.conceptual.farm` — Farm

**Type:** model

Conceptual model for Farm (independent of JSON or other schema encoding).

### `ogc.model.agriculture.features.plot` — Plot - GeoJSON

**Type:** schema

GeoJSON binding for Plot class

### `ogc.model.agriculture.conceptual.agriFeature` — Agri Feature Conceptual

**Type:** model

References the set of spatial features defined or adopted from other standards by the Agriculture Information Model

### `ogc.model.agriculture.geosparql-ld.farm` — Farm (SAREF) - GeoSPARQL

**Type:** model

Defines JSON-LD structures mappable directly to the semantic models, i.e. GeoSPARQL instead of GeoJSON

### `ogc.model.agriculture.features.farm` — Farm - GeoJSON

**Type:** schema

GeoJSON binding for Farm class

### `ogc.model.agriculture.conceptual.all` — Agriculture Information Model - RDF

**Type:** model

All modules of the Agriculture Information Model implemented by pure RDF, including JSON-LD based on JSON structures mappable directly to the semantic models defined in the Cross-Domain Model.

### `ogc.model.agriculture.features.all` — OGC Features - Agriculture 

**Type:** model

All modules of the OGC Features compatible JSON schema implementation of the Agriculture Information Module

