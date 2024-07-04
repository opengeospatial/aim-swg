---
title: Farm (SAREF) - GeoSPARQL (Model)


toc_footers:
  - Version 0.1
  - <a href='#'>Farm (SAREF) - GeoSPARQL</a>
  - <a href='https://blocks.ogc.org/register.html'>Building Blocks register</a>

search: true

code_clipboard: true

meta:
  - name: Farm (SAREF) - GeoSPARQL (Model)
---


# Farm (SAREF) - GeoSPARQL `ogc.model.agriculture.geosparql-ld.farm`

Defines JSON-LD structures mappable directly to the semantic models, i.e. GeoSPARQL instead of GeoJSON

<p class="status">
    <span data-rainbow-uri="http://www.opengis.net/def/status">Status</span>:
    <a href="http://www.opengis.net/def/status/under-development" target="_blank" data-rainbow-uri>Under development</a>
</p>

<aside class="success">
This building block is <strong><a href="https://github.com/ogcincubator/aim-swg/blob/main/build/tests/model/agriculture/geosparql-ld/farm/" target="_blank">valid</a></strong>
</aside>

# Description

## Agriculture Information Model Closure

Defines dependencies for the complete Agriculture Information Model based on reusable modular components.





# Examples

## Simple Farm Instance GeoSPARQL schema



```json
{
  "@context": [
  		"https://w3id.org/demeter/agri-context.jsonld"
   ],
  "@id": "urn:ngsi-ld:farm:72d9fb43-53f8-4ec8-a33c-fa931360259a",
  "@type": "Farm",
  "name": "Wheat farm",
  "description": "A farm producing wheat",
  "hasGeometry": {
    "@id": "urn:ngsi-ld:AgriFarm:geo:72d9fb43-53f8-4ec8-a33c-fa931360259x",
    "@type": "Point",
    "asWKT": "POINT(11.3 44.12)"
  },
  "containsPlot":[
    {
      "@id": "urn:ngsi-ld:plot:72d9fb43-53f8-4ec8-a33c-fa931360259a",
      "@type": "Plot",
      "hasGeometry": {
        "@id": "urn:ngsi-ld:plot:geo:72d9fb43-53f8-4ec8-a33c-fa931360259y",
        "@type": "Polygon",
        "asWKT": "POLYGON (100 0, 101 0, 101 1, 100 1, 100 0)"
      },
      "area": 2012120,
      "description": "Spring wheat parcel",
      "category": "arable",
      "crop": {
        "@id": "urn:ngsi-ld:crop:df72dc57-1eb9-42a3-88a9-8647ecc954b4",
        "@type": "Crop",
        "cropSpecies":{
          "@id": "urn:demeter:croptype:df72dc57-1eb9-42a3-88a9-8647ecc954b4",
		      "@type": "CropType",
          "name": "Wheat",
          "alternateName": "Triticum aestivum",
          "agroVocConcept": "http://aims.fao.org/aos/agrovoc/c_7951",
          "description": "Spring wheat"
        },
        "cropStatus": "seeded",
        "lastPlantedAt": "2016-08-23T10:18:16Z"
      }
    },
    {
      "@id": "urn:ngsi-ld:plot:72d9fb43-53f8-4ec8-a33c-fa931360259b",
      "@type": "Plot",
      "hasGeometry": {
        "@id": "urn:ngsi-ld:AgriParcel:geo:72d9fb43-53f8-4ec8-a33c-fa931360259z",
        "@type": "Polygon",
        "asWKT": "POLYGON (100 0, 101 0, 101 1, 100 1, 100 1)"
      },
      "area": 200,
      "description": "Spring barley parcel",
      "category": "arable",
      "crop": {
        "@id": "urn:ngsi-ld:crop:df72dc57-1eb9-42a3-88a9-8647ecc954b5",
        "@type": "Crop",
        "cropSpecies":{
          "@id": "urn:demeter:croptype:df72dc57-1eb9-42a3-88a9-8647ecc954b5",
		      "@type": "CropType",
          "name": "Barley",
          "alternateName": "Ordeum",
          "agroVocConcept": "http://aims.fao.org/aos/agrovoc/c_7952",
          "description": "Spring barley"
        },
        "cropStatus": "seeded",
        "lastPlantedAt": "2016-08-23T10:18:16Z"
      }
    }
  ]
}
```

<blockquote class="lang-specific json">
  <p class="example-links">
    <a target="_blank" href="https://ogcincubator.github.io/aim-swg/build/tests/model/agriculture/geosparql-ld/farm/example_1_1.json">Open in new window</a>
    <a target="_blank" href="https://avillar.github.io/TreedocViewer/?dataParser=json&amp;dataUrl=https%3A%2F%2Fogcincubator.github.io%2Faim-swg%2Fbuild%2Ftests%2Fmodel%2Fagriculture%2Fgeosparql-ld%2Ffarm%2Fexample_1_1.json&amp;expand=2&amp;option=%7B%22showTable%22%3A+false%7D">View on JSON Viewer</a></p>
</blockquote>


Example from AIM  using a GeoSPARQL JSON-LD schema. 


# For developers

The source code for this Building Block can be found in the following repository:

* URL: <a href="https://github.com/ogcincubator/aim-swg" target="_blank">https://github.com/ogcincubator/aim-swg</a>
* Path:
<code><a href="https://github.com/ogcincubator/aim-swg/blob/HEAD/_sources/geosparql-ld/farm" target="_blank">_sources/geosparql-ld/farm</a></code>

