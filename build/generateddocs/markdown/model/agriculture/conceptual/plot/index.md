
# Plot (Model)

`ogc.model.agriculture.conceptual.plot` *v0.1*

Conceptual model for Plot/Parcel (independent of JSON or other schema encoding).

[*Status*](http://www.opengis.net/def/status): Under development

## Description

## Plot (SAREF model)

TBD - how does this relate to the other equivalent classes supported by AIM?





## Examples

### Simple Farm Instance
Example from AIM  

#### ttl
```ttl
@prefix ns0: <http://foodie-cloud.com/model/foodie#> .
@prefix ns1: <https://uri.fiware.org/ns/data-models#> .
@prefix ns2: <http://www.opengis.net/ont/geosparql#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<urn:demeter:croptype:df72dc57-1eb9-42a3-88a9-8647ecc954b4>
  ns0:description "Spring wheat" ;
  a ns0:CropType ;
  ns1:agroVocConcept <http://aims.fao.org/aos/agrovoc/c_7951> ;
  ns1:alternateName "Triticum aestivum" ;
  ns1:name "Wheat" .

<urn:ngsi-ld:crop:df72dc57-1eb9-42a3-88a9-8647ecc954b4>
  ns0:cropSpecies <urn:demeter:croptype:df72dc57-1eb9-42a3-88a9-8647ecc954b4> ;
  a <https://w3id.org/def/saref4agri#Crop> ;
  ns1:cropStatus "seeded" ;
  ns1:lastPlantedAt "2016-08-23T10:18:16Z"^^xsd:dateTime .


<urn:ngsi-ld:plot:72d9fb43-53f8-4ec8-a33c-fa931360259a>
  ns0:crop <urn:ngsi-ld:crop:df72dc57-1eb9-42a3-88a9-8647ecc954b4> ;
  ns0:description "Spring wheat parcel" ;
  ns2:hasGeometry <urn:ngsi-ld:plot:geo:72d9fb43-53f8-4ec8-a33c-fa931360259y> ;
  a ns0:Plot ;
  ns1:area 2012120 ;
  ns1:category "arable" .


<urn:ngsi-ld:plot:geo:72d9fb43-53f8-4ec8-a33c-fa931360259y>
  ns2:asWKT "POLYGON (100 0, 101 0, 101 1, 100 1, 100 0)"^^ns2:wktLiteral ;
  a <http://www.opengis.net/ont/sf#Polygon> .
```


# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/aim-swg](https://github.com/ogcincubator/aim-swg)
* Path: `_sources/conceptual/plot`
