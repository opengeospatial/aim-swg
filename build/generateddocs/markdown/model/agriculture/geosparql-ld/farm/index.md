
# Farm (SAREF) - GeoSPARQL (Model)

`ogc.model.agriculture.geosparql-ld.farm` *v0.1*

Defines JSON-LD structures mappable directly to the semantic models, i.e. GeoSPARQL instead of GeoJSON

[*Status*](http://www.opengis.net/def/status): Under development

## Description

## Agriculture Information Model Closure

Defines dependencies for the complete Agriculture Information Model based on reusable modular components.





## Examples

### Simple Farm Instance GeoSPARQL schema
Example from AIM  using a GeoSPARQL JSON-LD schema. 

#### jsonld
```jsonld
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

#### ttl
```ttl
@prefix geo: <http://www.opengis.net/ont/geosparql#> .
@prefix ns1: <https://smartdatamodels.org/dataModel.Agrifood/> .
@prefix ns2: <http://foodie-cloud.com/model/foodie#> .
@prefix ns3: <https://smartdatamodels.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<urn:ngsi-ld:farm:72d9fb43-53f8-4ec8-a33c-fa931360259a> a <https://saref.etsi.org/saref4agri/Farm> ;
    ns2:containsPlot <urn:ngsi-ld:plot:72d9fb43-53f8-4ec8-a33c-fa931360259a>,
        <urn:ngsi-ld:plot:72d9fb43-53f8-4ec8-a33c-fa931360259b> ;
    ns2:description "A farm producing wheat"^^xsd:string ;
    geo:hasGeometry <urn:ngsi-ld:AgriFarm:geo:72d9fb43-53f8-4ec8-a33c-fa931360259x> ;
    ns3:name "Wheat farm" .

<urn:demeter:croptype:df72dc57-1eb9-42a3-88a9-8647ecc954b4> a ns2:CropType ;
    ns2:description "Spring wheat"^^xsd:string ;
    ns3:alternateName "Triticum aestivum" ;
    ns1:agroVocConcept <http://aims.fao.org/aos/agrovoc/c_7951> ;
    ns3:name "Wheat" .

<urn:demeter:croptype:df72dc57-1eb9-42a3-88a9-8647ecc954b5> a ns2:CropType ;
    ns2:description "Spring barley"^^xsd:string ;
    ns3:alternateName "Ordeum" ;
    ns1:agroVocConcept <http://aims.fao.org/aos/agrovoc/c_7952> ;
    ns3:name "Barley" .

<urn:ngsi-ld:AgriFarm:geo:72d9fb43-53f8-4ec8-a33c-fa931360259x> a <http://www.opengis.net/ont/sf#Point> ;
    geo:asWKT "POINT(11.3 44.12)"^^geo:wktLiteral .

<urn:ngsi-ld:AgriParcel:geo:72d9fb43-53f8-4ec8-a33c-fa931360259z> a <http://www.opengis.net/ont/sf#Polygon> ;
    geo:asWKT "POLYGON (100 0, 101 0, 101 1, 100 1, 100 1)"^^geo:wktLiteral .

<urn:ngsi-ld:crop:df72dc57-1eb9-42a3-88a9-8647ecc954b4> a <https://saref.etsi.org/saref4agri/Crop> ;
    ns2:cropSpecies <urn:demeter:croptype:df72dc57-1eb9-42a3-88a9-8647ecc954b4> ;
    ns1:cropStatus "seeded" ;
    ns1:lastPlantedAt "2016-08-23T10:18:16+00:00"^^xsd:dateTime .

<urn:ngsi-ld:crop:df72dc57-1eb9-42a3-88a9-8647ecc954b5> a <https://saref.etsi.org/saref4agri/Crop> ;
    ns2:cropSpecies <urn:demeter:croptype:df72dc57-1eb9-42a3-88a9-8647ecc954b5> ;
    ns1:cropStatus "seeded" ;
    ns1:lastPlantedAt "2016-08-23T10:18:16+00:00"^^xsd:dateTime .

<urn:ngsi-ld:plot:72d9fb43-53f8-4ec8-a33c-fa931360259a> a ns2:Plot ;
    ns2:crop <urn:ngsi-ld:crop:df72dc57-1eb9-42a3-88a9-8647ecc954b4> ;
    ns2:description "Spring wheat parcel"^^xsd:string ;
    geo:hasGeometry <urn:ngsi-ld:plot:geo:72d9fb43-53f8-4ec8-a33c-fa931360259y> ;
    ns1:area 2012120 ;
    ns1:category "arable" .

<urn:ngsi-ld:plot:72d9fb43-53f8-4ec8-a33c-fa931360259b> a ns2:Plot ;
    ns2:crop <urn:ngsi-ld:crop:df72dc57-1eb9-42a3-88a9-8647ecc954b5> ;
    ns2:description "Spring barley parcel"^^xsd:string ;
    geo:hasGeometry <urn:ngsi-ld:AgriParcel:geo:72d9fb43-53f8-4ec8-a33c-fa931360259z> ;
    ns1:area 200 ;
    ns1:category "arable" .

<urn:ngsi-ld:plot:geo:72d9fb43-53f8-4ec8-a33c-fa931360259y> a <http://www.opengis.net/ont/sf#Polygon> ;
    geo:asWKT "POLYGON (100 0, 101 0, 101 1, 100 1, 100 0)"^^geo:wktLiteral .


```


# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/opengeospatial/aim-swg](https://github.com/opengeospatial/aim-swg)
* Path: `_sources/geosparql-ld/farm`

