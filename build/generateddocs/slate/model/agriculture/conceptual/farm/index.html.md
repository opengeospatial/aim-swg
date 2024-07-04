---
title: Farm (Model)


toc_footers:
  - Version 0.1
  - <a href='#'>Farm</a>
  - <a href='https://blocks.ogc.org/register.html'>Building Blocks register</a>

search: true

code_clipboard: true

meta:
  - name: Farm (Model)
---


# Farm `ogc.model.agriculture.conceptual.farm`

Conceptual model for Farm (independent of JSON or other schema encoding).

<p class="status">
    <span data-rainbow-uri="http://www.opengis.net/def/status">Status</span>:
    <a href="http://www.opengis.net/def/status/under-development" target="_blank" data-rainbow-uri>Under development</a>
</p>

<aside class="success">
This building block is <strong><a href="https://github.com/ogcincubator/aim-swg/blob/main/build/tests/model/agriculture/conceptual/farm/" target="_blank">valid</a></strong>
</aside>

# Description

## Farm (SAREF model)

TBD - how does this relate to the other equivalent classes supported by AIM?





# Examples

## Simple Farm Instance



```turtle
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

<urn:demeter:croptype:df72dc57-1eb9-42a3-88a9-8647ecc954b5>
  ns0:description "Spring barley" ;
  a ns0:CropType ;
  ns1:agroVocConcept <http://aims.fao.org/aos/agrovoc/c_7952> ;
  ns1:alternateName "Ordeum" ;
  ns1:name "Barley" .

<urn:ngsi-ld:AgriFarm:geo:72d9fb43-53f8-4ec8-a33c-fa931360259x>
  ns2:asWKT "POINT(11.3 44.12)"^^ns2:wktLiteral ;
  a <http://www.opengis.net/ont/sf#Point> .

<urn:ngsi-ld:AgriParcel:geo:72d9fb43-53f8-4ec8-a33c-fa931360259z>
  ns2:asWKT "POLYGON (100 0, 101 0, 101 1, 100 1, 100 1)"^^ns2:wktLiteral ;
  a <http://www.opengis.net/ont/sf#Polygon> .

<urn:ngsi-ld:crop:df72dc57-1eb9-42a3-88a9-8647ecc954b4>
  ns0:cropSpecies <urn:demeter:croptype:df72dc57-1eb9-42a3-88a9-8647ecc954b4> ;
  a <https://w3id.org/def/saref4agri#Crop> ;
  ns1:cropStatus "seeded" ;
  ns1:lastPlantedAt "2016-08-23T10:18:16Z"^^xsd:dateTime .

<urn:ngsi-ld:crop:df72dc57-1eb9-42a3-88a9-8647ecc954b5>
  ns0:cropSpecies <urn:demeter:croptype:df72dc57-1eb9-42a3-88a9-8647ecc954b5> ;
  a <https://w3id.org/def/saref4agri#Crop> ;
  ns1:cropStatus "seeded" ;
  ns1:lastPlantedAt "2016-08-23T10:18:16Z"^^xsd:dateTime .

<urn:ngsi-ld:farm:72d9fb43-53f8-4ec8-a33c-fa931360259a>
  ns0:containsPlot <urn:ngsi-ld:plot:72d9fb43-53f8-4ec8-a33c-fa931360259a>, <urn:ngsi-ld:plot:72d9fb43-53f8-4ec8-a33c-fa931360259b> ;
  ns0:description "A farm producing wheat" ;
  ns2:hasGeometry <urn:ngsi-ld:AgriFarm:geo:72d9fb43-53f8-4ec8-a33c-fa931360259x> ;
  a <https://w3id.org/def/saref4agri#Farm> ;
  ns1:name "Wheat farm" .

<urn:ngsi-ld:plot:72d9fb43-53f8-4ec8-a33c-fa931360259a>
  ns0:crop <urn:ngsi-ld:crop:df72dc57-1eb9-42a3-88a9-8647ecc954b4> ;
  ns0:description "Spring wheat parcel" ;
  ns2:hasGeometry <urn:ngsi-ld:plot:geo:72d9fb43-53f8-4ec8-a33c-fa931360259y> ;
  a ns0:Plot ;
  ns1:area 2012120 ;
  ns1:category "arable" .

<urn:ngsi-ld:plot:72d9fb43-53f8-4ec8-a33c-fa931360259b>
  ns0:crop <urn:ngsi-ld:crop:df72dc57-1eb9-42a3-88a9-8647ecc954b5> ;
  ns0:description "Spring barley parcel" ;
  ns2:hasGeometry <urn:ngsi-ld:AgriParcel:geo:72d9fb43-53f8-4ec8-a33c-fa931360259z> ;
  a ns0:Plot ;
  ns1:area 200 ;
  ns1:category "arable" .

<urn:ngsi-ld:plot:geo:72d9fb43-53f8-4ec8-a33c-fa931360259y>
  ns2:asWKT "POLYGON (100 0, 101 0, 101 1, 100 1, 100 0)"^^ns2:wktLiteral ;
  a <http://www.opengis.net/ont/sf#Polygon> .
```

<blockquote class="lang-specific turtle">
  <p class="example-links">
    <a target="_blank" href="https://ogcincubator.github.io/aim-swg/build/tests/model/agriculture/conceptual/farm/example_1_1.ttl">Open in new window</a>
</blockquote>


Example from AIM  


# For developers

The source code for this Building Block can be found in the following repository:

* URL: <a href="https://github.com/ogcincubator/aim-swg" target="_blank">https://github.com/ogcincubator/aim-swg</a>
* Path:
<code><a href="https://github.com/ogcincubator/aim-swg/blob/HEAD/_sources/conceptual/farm" target="_blank">_sources/conceptual/farm</a></code>

