---
title: Plot (Model)


toc_footers:
  - Version 0.1
  - <a href='#'>Plot</a>
  - <a href='https://blocks.ogc.org/register.html'>Building Blocks register</a>

search: true

code_clipboard: true

meta:
  - name: Plot (Model)
---


# Plot `ogc.model.agriculture.conceptual.plot`

Conceptual model for Plot/Parcel (independent of JSON or other schema encoding).

<p class="status">
    <span data-rainbow-uri="http://www.opengis.net/def/status">Status</span>:
    <a href="http://www.opengis.net/def/status/under-development" target="_blank" data-rainbow-uri>Under development</a>
</p>

<aside class="success">
This building block is <strong><a href="https://github.com/ogcincubator/aim-swg/blob/main/build/tests/model/agriculture/conceptual/plot/" target="_blank">valid</a></strong>
</aside>

# Description

## Plot (SAREF model)

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

<blockquote class="lang-specific turtle">
  <p class="example-links">
    <a target="_blank" href="https://ogcincubator.github.io/aim-swg/build/tests/model/agriculture/conceptual/plot/example_1_1.ttl">Open in new window</a>
</blockquote>


Example from AIM  


# For developers

The source code for this Building Block can be found in the following repository:

* URL: <a href="https://github.com/ogcincubator/aim-swg" target="_blank">https://github.com/ogcincubator/aim-swg</a>
* Path:
<code><a href="https://github.com/ogcincubator/aim-swg/blob/HEAD/_sources/conceptual/plot" target="_blank">_sources/conceptual/plot</a></code>

