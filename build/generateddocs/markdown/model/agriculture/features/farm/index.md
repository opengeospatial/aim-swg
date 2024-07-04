
# Farm - GeoJSON (Schema)

`ogc.model.agriculture.features.farm` *v0.1*

GeoJSON binding for Farm class

[*Status*](http://www.opengis.net/def/status): Under development

## Description

## Agriculture Information Model Closure

Defines dependencies for the complete Agriculture Information Model based on reusable modular components.





## Examples

### Simple Farm Instance GeoSPARQL schema
Example from AIM  using a GeoJSON schema. 

#### json
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

#### jsonld
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

#### ttl
```ttl
@prefix geojson: <https://purl.org/geojson/vocab#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<file:///github/workspace/f1> a geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 1.13e+01 4.412e+01 ) ] .


```

## Schema

```yaml
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

Links to the schema:

* YAML version: [schema.yaml](https://ogcincubator.github.io/aim-swg/build/annotated/model/agriculture/features/farm/schema.json)
* JSON version: [schema.json](https://ogcincubator.github.io/aim-swg/build/annotated/model/agriculture/features/farm/schema.yaml)


# JSON-LD Context

```jsonld
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

You can find the full JSON-LD context here:
[context.jsonld](https://ogcincubator.github.io/aim-swg/build/annotated/model/agriculture/features/farm/context.jsonld)


# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/aim-swg](https://github.com/ogcincubator/aim-swg)
* Path: `_sources/features/farm`

