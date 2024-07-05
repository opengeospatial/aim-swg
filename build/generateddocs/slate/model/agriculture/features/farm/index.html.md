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

<aside class="warning">
Validation for this building block has <strong><a href="https://github.com/ogcincubator/aim-swg/blob/main/build/tests/model/agriculture/features/farm/" target="_blank">failed</a></strong>
</aside>

# Description

## Farm

Fg-JSON/GeoJSON binding for saref4agri:Farm





# Examples

## Simple Farm Instance GeoJSON



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
@prefix foodie: <http://foodie-cloud.com/model/foodie#> .
@prefix geojson: <https://purl.org/geojson/vocab#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix saref4agri: <https://saref.etsi.org/saref4agri/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<file:///github/workspace/f1> a geojson:Feature,
        saref4agri:Farm ;
    foodie:description "A farm producing wheat"^^xsd:string ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.13e+01 4.412e+01 ) ] .


```

<blockquote class="lang-specific turtle">
  <p class="example-links">
    <a target="_blank" href="https://ogcincubator.github.io/aim-swg/build/tests/model/agriculture/features/farm/example_1_1.ttl">Open in new window</a>
</blockquote>


Example from AIM  using a GeoJSON schema. 



## Farm with Plots GeoJSON



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
    "description": "A farm producing wheat",
    "containsPlot": [
      {
        "@id": "urn:ngsi-ld:plot:72d9fb43-53f8-4ec8-a33c-fa931360259a",
        "type": "Feature",
        "featureType": "Plot",
        "geometry": {
          "type": "Polygon",
          "coordinates": [
            [
              [
                100,
                0
              ],
              [
                101,
                0
              ],
              [
                101,
                1
              ],
              [
                100,
                1
              ],
              [
                100,
                0
              ]
            ]
          ]
        },
        "properties": {
          "area": 2012120,
          "description": "Spring wheat parcel",
          "category": "arable"
        }
      },
      {
        "@id": "urn:ngsi-ld:plot:72d9fb43-53f8-4ec8-a33c-fa931360259b",
        "type": "Feature",
        "featureType": "Plot",
        "geometry": {
          "type": "Polygon",
          "coordinates": [ [
            [
              100,
              0
            ],
            [
              101,
              0
            ],
            [
              101,
              1
            ],
            [
              100,
              1
            ],
            [
              100,
              0
            ]
          ] ]
        },
        "properties": {
          "area": 200,
          "description": "Spring barley parcel",
          "category": "arable"
        }
      }
    ]
  }
}
```

<blockquote class="lang-specific json">
  <p class="example-links">
    <a target="_blank" href="https://ogcincubator.github.io/aim-swg/build/tests/model/agriculture/features/farm/example_2_1.json">Open in new window</a>
    <a target="_blank" href="https://avillar.github.io/TreedocViewer/?dataParser=json&amp;dataUrl=https%3A%2F%2Fogcincubator.github.io%2Faim-swg%2Fbuild%2Ftests%2Fmodel%2Fagriculture%2Ffeatures%2Ffarm%2Fexample_2_1.json&amp;expand=2&amp;option=%7B%22showTable%22%3A+false%7D">View on JSON Viewer</a></p>
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
    "description": "A farm producing wheat",
    "containsPlot": [
      {
        "@id": "urn:ngsi-ld:plot:72d9fb43-53f8-4ec8-a33c-fa931360259a",
        "type": "Feature",
        "featureType": "Plot",
        "geometry": {
          "type": "Polygon",
          "coordinates": [
            [
              [
                100,
                0
              ],
              [
                101,
                0
              ],
              [
                101,
                1
              ],
              [
                100,
                1
              ],
              [
                100,
                0
              ]
            ]
          ]
        },
        "properties": {
          "area": 2012120,
          "description": "Spring wheat parcel",
          "category": "arable"
        }
      },
      {
        "@id": "urn:ngsi-ld:plot:72d9fb43-53f8-4ec8-a33c-fa931360259b",
        "type": "Feature",
        "featureType": "Plot",
        "geometry": {
          "type": "Polygon",
          "coordinates": [
            [
              [
                100,
                0
              ],
              [
                101,
                0
              ],
              [
                101,
                1
              ],
              [
                100,
                1
              ],
              [
                100,
                0
              ]
            ]
          ]
        },
        "properties": {
          "area": 200,
          "description": "Spring barley parcel",
          "category": "arable"
        }
      }
    ]
  },
  "@context": "https://ogcincubator.github.io/aim-swg/build/annotated/model/agriculture/features/farm/context.jsonld"
}
```

<blockquote class="lang-specific jsonld">
  <p class="example-links">
    <a target="_blank" href="https://ogcincubator.github.io/aim-swg/build/tests/model/agriculture/features/farm/example_2_1.jsonld">Open in new window</a>
    <a target="_blank" href="https://json-ld.org/playground/#json-ld=https%3A%2F%2Fogcincubator.github.io%2Faim-swg%2Fbuild%2Ftests%2Fmodel%2Fagriculture%2Ffeatures%2Ffarm%2Fexample_2_1.jsonld">View on JSON-LD Playground</a>
</blockquote>




```turtle
@prefix foodie: <http://foodie-cloud.com/model/foodie#> .
@prefix geojson: <https://purl.org/geojson/vocab#> .
@prefix ns1: <https://smartdatamodels.org/dataModel.Agrifood/> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix saref4agri: <https://saref.etsi.org/saref4agri/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<file:///github/workspace/f1> a geojson:Feature,
        saref4agri:Farm ;
    foodie:containsPlot <urn:ngsi-ld:plot:72d9fb43-53f8-4ec8-a33c-fa931360259a>,
        <urn:ngsi-ld:plot:72d9fb43-53f8-4ec8-a33c-fa931360259b> ;
    foodie:description "A farm producing wheat"^^xsd:string ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.13e+01 4.412e+01 ) ] .

<urn:ngsi-ld:plot:72d9fb43-53f8-4ec8-a33c-fa931360259a> a foodie:Plot,
        geojson:Feature ;
    foodie:description "Spring wheat parcel"^^xsd:string ;
    geojson:geometry [ a geojson:Polygon ;
            geojson:coordinates ( ( ( 100 0 ) ( 101 0 ) ( 101 1 ) ( 100 1 ) ( 100 0 ) ) ) ] ;
    ns1:area 2012120 .

<urn:ngsi-ld:plot:72d9fb43-53f8-4ec8-a33c-fa931360259b> a foodie:Plot,
        geojson:Feature ;
    foodie:description "Spring barley parcel"^^xsd:string ;
    geojson:geometry [ a geojson:Polygon ;
            geojson:coordinates ( ( ( 100 0 ) ( 101 0 ) ( 101 1 ) ( 100 1 ) ( 100 0 ) ) ) ] ;
    ns1:area 200 .


```

<blockquote class="lang-specific turtle">
  <p class="example-links">
    <a target="_blank" href="https://ogcincubator.github.io/aim-swg/build/tests/model/agriculture/features/farm/example_2_1.ttl">Open in new window</a>
</blockquote>


Example from AIM  using a GeoJSON schema. 



## Farm, Plots, Crops GeoJSON



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
    "description": "A farm producing wheat",
    "containsPlot": [
      {
        "@id": "urn:ngsi-ld:plot:72d9fb43-53f8-4ec8-a33c-fa931360259a",
        "type": "Feature",
        "featureType": "Plot",
        "geometry": {
          "type": "Polygon",
          "coordinates": [
            [
              [
                100,
                0
              ],
              [
                101,
                0
              ],
              [
                101,
                1
              ],
              [
                100,
                1
              ],
              [
                100,
                0
              ]
            ]
          ]
        },
        "properties": {
          "area": 2012120,
          "description": "Spring wheat parcel",
          "category": "arable",
          "crop": {
            "@id": "urn:ngsi-ld:crop:df72dc57-1eb9-42a3-88a9-8647ecc954b4",
            "@type": "Crop",
            "cropSpecies": {
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
        }
      },
      {
        "@id": "urn:ngsi-ld:plot:72d9fb43-53f8-4ec8-a33c-fa931360259b",
        "type": "Feature",
        "featureType": "Plot",
        "geometry": {
          "type": "Polygon",
          "coordinates": [
            [
              [
                100,
                0
              ],
              [
                101,
                0
              ],
              [
                101,
                1
              ],
              [
                100,
                1
              ],
              [
                100,
                0
              ]
            ]
          ]
        },
        "properties": {
          "area": 200,
          "description": "Spring barley parcel",
          "category": "arable",
          "crop": {
            "@id": "urn:ngsi-ld:crop:df72dc57-1eb9-42a3-88a9-8647ecc954b5",
            "@type": "Crop",
            "cropSpecies": {
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
      }
    ]
  }
}
```

<blockquote class="lang-specific json">
  <p class="example-links">
    <a target="_blank" href="https://ogcincubator.github.io/aim-swg/build/tests/model/agriculture/features/farm/example_3_1.json">Open in new window</a>
    <a target="_blank" href="https://avillar.github.io/TreedocViewer/?dataParser=json&amp;dataUrl=https%3A%2F%2Fogcincubator.github.io%2Faim-swg%2Fbuild%2Ftests%2Fmodel%2Fagriculture%2Ffeatures%2Ffarm%2Fexample_3_1.json&amp;expand=2&amp;option=%7B%22showTable%22%3A+false%7D">View on JSON Viewer</a></p>
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
    "description": "A farm producing wheat",
    "containsPlot": [
      {
        "@id": "urn:ngsi-ld:plot:72d9fb43-53f8-4ec8-a33c-fa931360259a",
        "type": "Feature",
        "featureType": "Plot",
        "geometry": {
          "type": "Polygon",
          "coordinates": [
            [
              [
                100,
                0
              ],
              [
                101,
                0
              ],
              [
                101,
                1
              ],
              [
                100,
                1
              ],
              [
                100,
                0
              ]
            ]
          ]
        },
        "properties": {
          "area": 2012120,
          "description": "Spring wheat parcel",
          "category": "arable",
          "crop": {
            "@id": "urn:ngsi-ld:crop:df72dc57-1eb9-42a3-88a9-8647ecc954b4",
            "@type": "Crop",
            "cropSpecies": {
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
        }
      },
      {
        "@id": "urn:ngsi-ld:plot:72d9fb43-53f8-4ec8-a33c-fa931360259b",
        "type": "Feature",
        "featureType": "Plot",
        "geometry": {
          "type": "Polygon",
          "coordinates": [
            [
              [
                100,
                0
              ],
              [
                101,
                0
              ],
              [
                101,
                1
              ],
              [
                100,
                1
              ],
              [
                100,
                0
              ]
            ]
          ]
        },
        "properties": {
          "area": 200,
          "description": "Spring barley parcel",
          "category": "arable",
          "crop": {
            "@id": "urn:ngsi-ld:crop:df72dc57-1eb9-42a3-88a9-8647ecc954b5",
            "@type": "Crop",
            "cropSpecies": {
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
      }
    ]
  },
  "@context": "https://ogcincubator.github.io/aim-swg/build/annotated/model/agriculture/features/farm/context.jsonld"
}
```

<blockquote class="lang-specific jsonld">
  <p class="example-links">
    <a target="_blank" href="https://ogcincubator.github.io/aim-swg/build/tests/model/agriculture/features/farm/example_3_1.jsonld">Open in new window</a>
    <a target="_blank" href="https://json-ld.org/playground/#json-ld=https%3A%2F%2Fogcincubator.github.io%2Faim-swg%2Fbuild%2Ftests%2Fmodel%2Fagriculture%2Ffeatures%2Ffarm%2Fexample_3_1.jsonld">View on JSON-LD Playground</a>
</blockquote>




```turtle
@prefix foodie: <http://foodie-cloud.com/model/foodie#> .
@prefix geojson: <https://purl.org/geojson/vocab#> .
@prefix ns1: <https://smartdatamodels.org/dataModel.Agrifood/> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix saref4agri: <https://saref.etsi.org/saref4agri/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<file:///github/workspace/f1> a geojson:Feature,
        saref4agri:Farm ;
    foodie:containsPlot <urn:ngsi-ld:plot:72d9fb43-53f8-4ec8-a33c-fa931360259a>,
        <urn:ngsi-ld:plot:72d9fb43-53f8-4ec8-a33c-fa931360259b> ;
    foodie:description "A farm producing wheat"^^xsd:string ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.13e+01 4.412e+01 ) ] .

<urn:ngsi-ld:crop:df72dc57-1eb9-42a3-88a9-8647ecc954b4> a saref4agri:Crop ;
    ns1:cropStatus "seeded" ;
    ns1:lastPlantedAt "2016-08-23T10:18:16+00:00"^^xsd:dateTime .

<urn:ngsi-ld:crop:df72dc57-1eb9-42a3-88a9-8647ecc954b5> a saref4agri:Crop ;
    ns1:cropStatus "seeded" ;
    ns1:lastPlantedAt "2016-08-23T10:18:16+00:00"^^xsd:dateTime .

<urn:ngsi-ld:plot:72d9fb43-53f8-4ec8-a33c-fa931360259a> a foodie:Plot,
        geojson:Feature ;
    foodie:crop <urn:ngsi-ld:crop:df72dc57-1eb9-42a3-88a9-8647ecc954b4> ;
    foodie:description "Spring wheat parcel"^^xsd:string ;
    geojson:geometry [ a geojson:Polygon ;
            geojson:coordinates ( ( ( 100 0 ) ( 101 0 ) ( 101 1 ) ( 100 1 ) ( 100 0 ) ) ) ] ;
    ns1:area 2012120 .

<urn:ngsi-ld:plot:72d9fb43-53f8-4ec8-a33c-fa931360259b> a foodie:Plot,
        geojson:Feature ;
    foodie:crop <urn:ngsi-ld:crop:df72dc57-1eb9-42a3-88a9-8647ecc954b5> ;
    foodie:description "Spring barley parcel"^^xsd:string ;
    geojson:geometry [ a geojson:Polygon ;
            geojson:coordinates ( ( ( 100 0 ) ( 101 0 ) ( 101 1 ) ( 100 1 ) ( 100 0 ) ) ) ] ;
    ns1:area 200 .


```

<blockquote class="lang-specific turtle">
  <p class="example-links">
    <a target="_blank" href="https://ogcincubator.github.io/aim-swg/build/tests/model/agriculture/features/farm/example_3_1.ttl">Open in new window</a>
</blockquote>


Example from AIM  using a GeoJSON schema. 



# JSON Schema

```yaml--schema
$schema: https://json-schema.org/draft/2020-12/schema
description: Farm as GeoJSON
$defs:
  MyFeature:
    allOf:
    - $ref: https://opengeospatial.github.io/bblocks/annotated-schemas/geo/json-fg/feature-lenient/schema.yaml
    - type: object
      properties:
        properties:
          properties:
            name:
              type: string
            description:
              type: string
              x-jsonld-id: http://foodie-cloud.com/model/foodie#description
              x-jsonld-type: http://www.w3.org/2001/XMLSchema#string
            containsPlot:
              type: array
              items:
                $ref: https://ogcincubator.github.io/aim-swg/build/annotated/model/agriculture/features/plot/schema.yaml
              x-jsonld-id: http://foodie-cloud.com/model/foodie#containsPlot
              x-jsonld-type: '@id'
anyOf:
- $ref: '#/$defs/MyFeature'
x-jsonld-extra-terms:
  invalidatedAtTime:
    x-jsonld-id: http://www.w3.org/ns/prov#invalidatedAtTime
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#dateTime
  Crop: https://saref.etsi.org/saref4agri/Crop
  hasAgriCrop:
    x-jsonld-id: https://smartdatamodels.org/dataModel.Agrifood/hasAgriCrop
    x-jsonld-type: '@id'
  affiliation: https://schema.org/affiliation
  versionInfo: http://www.w3.org/2002/07/owl#versionInfo
  generatedAtTime:
    x-jsonld-id: http://www.w3.org/ns/prov#generatedAtTime
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#dateTime
  validFrom:
    x-jsonld-id: http://portele.de/ont/inspire/baseInspire#validFrom
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#dateTime
  hasAgriParcelParent:
    x-jsonld-id: https://smartdatamodels.org/dataModel.Agrifood/hasAgriParcelParent
    x-jsonld-type: '@id'
  crop:
    x-jsonld-id: http://foodie-cloud.com/model/foodie#crop
    x-jsonld-type: '@id'
  Thing: http://www.w3.org/2002/07/owl#Thing
  hasName:
    x-jsonld-id: https://saref.etsi.org/saref4agri/hasName
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#string
  lastPlantedAt:
    x-jsonld-id: https://smartdatamodels.org/dataModel.Agrifood/lastPlantedAt
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#dateTime
  OriginTypeValue: http://foodie-cloud.com/model/foodie#OriginTypeValue
  area: https://smartdatamodels.org/dataModel.Agrifood/area
  originType:
    x-jsonld-id: http://foodie-cloud.com/model/foodie#originType
    x-jsonld-type: '@id'
  maker: http://xmlns.com/foaf/0.1/maker
  sfWithin:
    x-jsonld-id: http://www.opengis.net/ont/geosparql#sfWithin
    x-jsonld-type: '@id'
  AgriFarm: https://smartdatamodels.org/dataModel.Agrifood/AgriFarm
  activity:
    x-jsonld-id: http://inspire.ec.europa.eu/schemas/af/3.0#activity
    x-jsonld-type: '@id'
  Feature: http://www.opengis.net/ont/geosparql#Feature
  label: http://www.w3.org/2000/01/rdf-schema#label
  contains:
    x-jsonld-id: https://saref.etsi.org/saref4agri/contains
    x-jsonld-type: '@id'
  landLocation:
    x-jsonld-id: https://smartdatamodels.org/dataModel.Agrifood/landLocation
    x-jsonld-type: '@id'
  Concept: http://www.w3.org/2004/02/skos/core#Concept
  homepage: http://xmlns.com/foaf/0.1/homepage
  ActivityComplex: http://inspire.ec.europa.eu/schemas/act-core/3.0#ActivityComplex
  holdingSite:
    x-jsonld-id: http://foodie-cloud.com/model/foodie#holdingSite
    x-jsonld-type: '@id'
  creator: http://purl.org/dc/terms/creator
  holdingPlot:
    x-jsonld-id: http://foodie-cloud.com/model/foodie#holdingPlot
    x-jsonld-type: '@id'
  foaf.name: http://xmlns.com/foaf/0.1/name
  holdingZone:
    x-jsonld-id: http://foodie-cloud.com/model/foodie#holdingZone
    x-jsonld-type: '@id'
  cropStatus: https://smartdatamodels.org/dataModel.Agrifood/cropStatus
  hasAgriSoil:
    x-jsonld-id: https://smartdatamodels.org/dataModel.Agrifood/hasAgriSoil
    x-jsonld-type: '@id'
  Building: https://saref.etsi.org/saref4agri/Building
  isContainedIn:
    x-jsonld-id: https://saref.etsi.org/saref4agri/isContainedIn
    x-jsonld-type: '@id'
  location:
    x-jsonld-id: http://www.w3.org/2003/01/geo/wgs84_pos#location
    x-jsonld-type: '@id'
  TractorType: http://foodie-cloud.com/model/foodie#TractorType
  AgriGreenhouse: https://smartdatamodels.org/dataModel.Agrifood/AgriGreenhouse
  rights: http://purl.org/dc/terms/rights
  Farm: https://saref.etsi.org/saref4agri/Farm
  hasAgriParcel:
    x-jsonld-id: https://smartdatamodels.org/dataModel.Agrifood/hasAgriParcel
    x-jsonld-type: '@id'
  machine:
    x-jsonld-id: http://foodie-cloud.com/model/foodie#machine
    x-jsonld-type: '@id'
  isDefinedBy: http://www.w3.org/2000/01/rdf-schema#isDefinedBy
  hasGeometry:
    x-jsonld-id: http://www.opengis.net/ont/geosparql#hasGeometry
    x-jsonld-type: '@id'
  sfContains:
    x-jsonld-id: http://www.opengis.net/ont/geosparql#sfContains
    x-jsonld-type: '@id'
  title: http://purl.org/dc/terms/title
  validTo:
    x-jsonld-id: http://portele.de/ont/inspire/baseInspire#validTo
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#dateTime
  Holding: http://inspire.ec.europa.eu/schemas/af/3.0#Holding
  Parcel: https://saref.etsi.org/saref4agri/Parcel
  Plot: http://foodie-cloud.com/model/foodie#Plot
  Site: http://inspire.ec.europa.eu/schemas/af/3.0#Site
  hasAgriParcelChildren:
    x-jsonld-id: https://smartdatamodels.org/dataModel.Agrifood/hasAgriParcelChildren
    x-jsonld-type: '@id'
  seeAlso: http://www.w3.org/2000/01/rdf-schema#seeAlso
  MachineType: http://foodie-cloud.com/model/foodie#MachineType
  notes:
    x-jsonld-id: http://foodie-cloud.com/model/foodie#notes
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#string
  EconomicActivityNACEValue: http://inspire.ec.europa.eu/schemas/act-core/3.0#EconomicActivityNACEValue
  BuildingSpace: https://saref.etsi.org/saref4agri/BuildingSpace
  comment: http://www.w3.org/2000/01/rdf-schema#comment
  contributor: http://purl.org/dc/terms/contributor
  containsZone:
    x-jsonld-id: http://foodie-cloud.com/model/foodie#containsZone
    x-jsonld-type: '@id'
  tractor:
    x-jsonld-id: http://foodie-cloud.com/model/foodie#tractor
    x-jsonld-type: '@id'
  code:
    x-jsonld-id: http://foodie-cloud.com/model/foodie#code
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#string
  AgriParcel: https://smartdatamodels.org/dataModel.Agrifood/AgriParcel
  prefLabel: http://www.w3.org/2004/02/skos/core#prefLabel
  ManagementZone: http://foodie-cloud.com/model/foodie#ManagementZone
  locationGeoJson:
    x-jsonld-id: https://uri.etsi.org/ngsi-ld/location
    x-jsonld-type: '@id'
  containsSite:
    x-jsonld-id: http://inspire.ec.europa.eu/schemas/af/3.0#contains
    x-jsonld-type: '@id'
x-jsonld-prefixes:
  saref4agri: https://saref.etsi.org/saref4agri/
  foodie: http://foodie-cloud.com/model/foodie#

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
      "@context": {},
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
    "featureType": "@type",
    "time": {
      "@context": {
        "date": {
          "@id": "owlTime:hasTime",
          "@type": "xsd:date"
        },
        "timestamp": {
          "@id": "owlTime:hasTime",
          "@type": "xsd:dateTime"
        },
        "interval": {
          "@id": "owlTime:hasTime",
          "@container": "@list"
        }
      },
      "@id": "dct:time"
    },
    "coordRefSys": "http://www.opengis.net/def/glossary/term/CoordinateReferenceSystemCRS",
    "place": "dct:spatial",
    "Polyhedron": "geojson:Polyhedron",
    "MultiPolyhedron": "geojson:MultiPolyhedron",
    "Prism": {
      "@id": "geojson:Prism",
      "@context": {
        "base": "geojson:prismBase",
        "lower": "geojson:prismLower",
        "upper": "geojson:prismUpper"
      }
    },
    "MultiPrism": {
      "@id": "geojson:MultiPrism",
      "@context": {
        "prisms": "geojson:prisms"
      }
    },
    "coordinates": {
      "@container": "@list",
      "@id": "geojson:coordinates"
    },
    "geometries": {
      "@id": "geojson:geometry",
      "@container": "@list"
    },
    "description": {
      "@id": "foodie:description",
      "@type": "xsd:string"
    },
    "containsPlot": {
      "@context": {},
      "@id": "foodie:containsPlot",
      "@type": "@id"
    },
    "invalidatedAtTime": {
      "@id": "http://www.w3.org/ns/prov#invalidatedAtTime",
      "@type": "xsd:dateTime"
    },
    "Crop": "saref4agri:Crop",
    "hasAgriCrop": {
      "@id": "https://smartdatamodels.org/dataModel.Agrifood/hasAgriCrop",
      "@type": "@id"
    },
    "affiliation": "https://schema.org/affiliation",
    "versionInfo": "http://www.w3.org/2002/07/owl#versionInfo",
    "generatedAtTime": {
      "@id": "http://www.w3.org/ns/prov#generatedAtTime",
      "@type": "xsd:dateTime"
    },
    "validFrom": {
      "@id": "http://portele.de/ont/inspire/baseInspire#validFrom",
      "@type": "xsd:dateTime"
    },
    "hasAgriParcelParent": {
      "@id": "https://smartdatamodels.org/dataModel.Agrifood/hasAgriParcelParent",
      "@type": "@id"
    },
    "crop": {
      "@id": "foodie:crop",
      "@type": "@id"
    },
    "Thing": "http://www.w3.org/2002/07/owl#Thing",
    "hasName": {
      "@id": "saref4agri:hasName",
      "@type": "xsd:string"
    },
    "lastPlantedAt": {
      "@id": "https://smartdatamodels.org/dataModel.Agrifood/lastPlantedAt",
      "@type": "xsd:dateTime"
    },
    "OriginTypeValue": "foodie:OriginTypeValue",
    "area": "https://smartdatamodels.org/dataModel.Agrifood/area",
    "originType": {
      "@id": "foodie:originType",
      "@type": "@id"
    },
    "maker": "http://xmlns.com/foaf/0.1/maker",
    "sfWithin": {
      "@id": "http://www.opengis.net/ont/geosparql#sfWithin",
      "@type": "@id"
    },
    "AgriFarm": "https://smartdatamodels.org/dataModel.Agrifood/AgriFarm",
    "activity": {
      "@id": "http://inspire.ec.europa.eu/schemas/af/3.0#activity",
      "@type": "@id"
    },
    "label": "rdfs:label",
    "contains": {
      "@id": "saref4agri:contains",
      "@type": "@id"
    },
    "landLocation": {
      "@id": "https://smartdatamodels.org/dataModel.Agrifood/landLocation",
      "@type": "@id"
    },
    "Concept": "http://www.w3.org/2004/02/skos/core#Concept",
    "homepage": "http://xmlns.com/foaf/0.1/homepage",
    "ActivityComplex": "http://inspire.ec.europa.eu/schemas/act-core/3.0#ActivityComplex",
    "holdingSite": {
      "@id": "foodie:holdingSite",
      "@type": "@id"
    },
    "creator": "dct:creator",
    "holdingPlot": {
      "@id": "foodie:holdingPlot",
      "@type": "@id"
    },
    "foaf.name": "http://xmlns.com/foaf/0.1/name",
    "holdingZone": {
      "@id": "foodie:holdingZone",
      "@type": "@id"
    },
    "cropStatus": "https://smartdatamodels.org/dataModel.Agrifood/cropStatus",
    "hasAgriSoil": {
      "@id": "https://smartdatamodels.org/dataModel.Agrifood/hasAgriSoil",
      "@type": "@id"
    },
    "Building": "saref4agri:Building",
    "isContainedIn": {
      "@id": "saref4agri:isContainedIn",
      "@type": "@id"
    },
    "location": {
      "@id": "http://www.w3.org/2003/01/geo/wgs84_pos#location",
      "@type": "@id"
    },
    "TractorType": "foodie:TractorType",
    "AgriGreenhouse": "https://smartdatamodels.org/dataModel.Agrifood/AgriGreenhouse",
    "rights": "dct:rights",
    "Farm": "saref4agri:Farm",
    "hasAgriParcel": {
      "@id": "https://smartdatamodels.org/dataModel.Agrifood/hasAgriParcel",
      "@type": "@id"
    },
    "machine": {
      "@id": "foodie:machine",
      "@type": "@id"
    },
    "isDefinedBy": "rdfs:isDefinedBy",
    "hasGeometry": {
      "@id": "http://www.opengis.net/ont/geosparql#hasGeometry",
      "@type": "@id"
    },
    "sfContains": {
      "@id": "http://www.opengis.net/ont/geosparql#sfContains",
      "@type": "@id"
    },
    "title": "dct:title",
    "validTo": {
      "@id": "http://portele.de/ont/inspire/baseInspire#validTo",
      "@type": "xsd:dateTime"
    },
    "Holding": "http://inspire.ec.europa.eu/schemas/af/3.0#Holding",
    "Parcel": "saref4agri:Parcel",
    "Plot": "foodie:Plot",
    "Site": "http://inspire.ec.europa.eu/schemas/af/3.0#Site",
    "hasAgriParcelChildren": {
      "@id": "https://smartdatamodels.org/dataModel.Agrifood/hasAgriParcelChildren",
      "@type": "@id"
    },
    "seeAlso": "rdfs:seeAlso",
    "MachineType": "foodie:MachineType",
    "notes": {
      "@id": "foodie:notes",
      "@type": "xsd:string"
    },
    "EconomicActivityNACEValue": "http://inspire.ec.europa.eu/schemas/act-core/3.0#EconomicActivityNACEValue",
    "BuildingSpace": "saref4agri:BuildingSpace",
    "comment": "rdfs:comment",
    "contributor": "dct:contributor",
    "containsZone": {
      "@id": "foodie:containsZone",
      "@type": "@id"
    },
    "tractor": {
      "@id": "foodie:tractor",
      "@type": "@id"
    },
    "code": {
      "@id": "foodie:code",
      "@type": "xsd:string"
    },
    "AgriParcel": "https://smartdatamodels.org/dataModel.Agrifood/AgriParcel",
    "prefLabel": "http://www.w3.org/2004/02/skos/core#prefLabel",
    "ManagementZone": "foodie:ManagementZone",
    "locationGeoJson": {
      "@id": "https://uri.etsi.org/ngsi-ld/location",
      "@type": "@id"
    },
    "containsSite": {
      "@id": "http://inspire.ec.europa.eu/schemas/af/3.0#contains",
      "@type": "@id"
    },
    "geojson": "https://purl.org/geojson/vocab#",
    "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
    "oa": "http://www.w3.org/ns/oa#",
    "dct": "http://purl.org/dc/terms/",
    "owlTime": "http://www.w3.org/2006/time#",
    "xsd": "http://www.w3.org/2001/XMLSchema#",
    "saref4agri": "https://saref.etsi.org/saref4agri/",
    "foodie": "http://foodie-cloud.com/model/foodie#",
    "@version": 1.1
  }
}
```

> <a target="_blank" href="https://json-ld.org/playground/#json-ld=https%3A%2F%2Fogcincubator.github.io%2Faim-swg%2Fbuild%2Fannotated%2Fmodel%2Fagriculture%2Ffeatures%2Ffarm%2Fcontext.jsonld">View on JSON-LD Playground</a>

You can find the full JSON-LD context here:
<a href="https://ogcincubator.github.io/aim-swg/build/annotated/model/agriculture/features/farm/context.jsonld" target="_blank">https://ogcincubator.github.io/aim-swg/build/annotated/model/agriculture/features/farm/context.jsonld</a>

# Validation

## SHACL Shapes

The following sets of SHACL shapes are used for validating this building block:

* Farm <small><code>ogc.model.agriculture.conceptual.farm</code></small>
  * [https://ogcincubator.github.io/aim-swg/SHACL/agriFeature-SHACL.ttl](https://ogcincubator.github.io/aim-swg/SHACL/agriFeature-SHACL.ttl)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: <a href="https://github.com/ogcincubator/aim-swg" target="_blank">https://github.com/ogcincubator/aim-swg</a>
* Path:
<code><a href="https://github.com/ogcincubator/aim-swg/blob/HEAD/_sources/features/farm" target="_blank">_sources/features/farm</a></code>

