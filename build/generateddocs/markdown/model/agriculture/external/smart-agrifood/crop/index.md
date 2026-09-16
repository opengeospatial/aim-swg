
# SMART AgriCrop (Schema)

`ogc.model.agriculture.external.smart-agrifood.crop` *v0.1*

Smart Data Models - Agri Food - Agri Crop model

[*Status*](http://www.opengis.net/def/status): Under development

## Description

## Crop 

Crop using the Smart-data-models schema and LD context.  This is an object that may be bound to a GeoJSON feature or any other container as a property range.





## Examples

### AgriCrop example
Example from https://smart-data-models.github.io/dataModel.Agrifood/AgriCrop/examples/example-normalized.json

#### json
```json
{
  "id": "urn:ngsi-ld:AgriCrop:df72dc57-1eb9-42a3-88a9-8647ecc954b4",
  "type": "AgriCrop",
  "dateCreated": {
    "type": "DateTime",
    "value": "2017-01-01T01:20:00Z"
  },
  "dateModified": {
    "type": "DateTime",
    "value": "2017-05-04T12:30:00Z"
  },
  "name": {
    "type": "Text",
    "value": "Wheat"
  },
  "alternateName": {
    "type": "Text",
    "value": "Triticum aestivum"
  },
  "agroVocConcept": {
    "type": "Text",
    "value": "http://aims.fao.org/aos/agrovoc/c_7951"
  },
  "seeAlso": {
    "type": "StructuredValue",
    "value": [
      "https://example.org/concept/wheat",
      "https://datamodel.org/example/wheat"
    ]
  },
  "description": {
    "type": "Text",
    "value": "Spring wheat"
  },
  "relatedSource": {
    "type": "StructuredValue",
    "value": [
      {
        "application": "urn:ngsi-ld:AgriApp:72d9fb43-53f8-4ec8-a33c-fa931360259a",
        "applicationEntityId": "app:weat"
      }
    ]
  },
  "hasAgriSoil": {
    "type": "StructuredValue",
    "value": [
      "urn:ngsi-ld:AgriSoil:00411b56-bd1b-4551-96e0-a6e7fde9c840",
      "urn:ngsi-ld:AgriSoil:e8a8389a-edf5-4345-8d2c-b98ac1ce8e2a"
    ]
  },
  "hasAgriFertiliser": {
    "type": "StructuredValue",
    "value": [
      "urn:ngsi-ld:AgriFertiliser:1b0d6cf7-320c-4a2b-b2f1-4575ea850c73",
      "urn:ngsi-ld:AgriFertiliser:380973c8-4d3b-4723-a899-0c0c5cc63e7e"
    ]
  },
  "hasAgriPest": {
    "type": "StructuredValue",
    "value": [
      "urn:ngsi-ld:AgriPest:1b0d6cf7-320c-4a2b-b2f1-4575ea850c73",
      "urn:ngsi-ld:AgriPest:380973c8-4d3b-4723-a899-0c0c5cc63e7e"
    ]
  },
  "plantingFrom": {
    "type": "StructuredValue",
    "value": [
      {
        "dateRange": "-09-28/-10-12",
        "description": "Best Season"
      },
      {
        "dateRange": "-10-11/-10-18",
        "description": "Season OK"
      }
    ]
  },
  "harvestingInterval": {
    "type": "StructuredValue",
    "value": [
      {
        "dateRange": "-03-21/-04-01",
        "description": "Best Season"
      },
      {
        "dateRange": "-04-02/-04-15",
        "description": "Season OK"
      }
    ]
  },
  "wateringFrequency": {
    "type": "Text",
    "value": "daily"
  }
}
```

#### jsonld
```jsonld
{
  "@context": "https://opengeospatial.github.io/aim-swg/build/annotated/model/agriculture/external/smart-agrifood/crop/context.jsonld",
  "id": "urn:ngsi-ld:AgriCrop:df72dc57-1eb9-42a3-88a9-8647ecc954b4",
  "type": "AgriCrop",
  "dateCreated": {
    "type": "DateTime",
    "value": "2017-01-01T01:20:00Z"
  },
  "dateModified": {
    "type": "DateTime",
    "value": "2017-05-04T12:30:00Z"
  },
  "name": {
    "type": "Text",
    "value": "Wheat"
  },
  "alternateName": {
    "type": "Text",
    "value": "Triticum aestivum"
  },
  "agroVocConcept": {
    "type": "Text",
    "value": "http://aims.fao.org/aos/agrovoc/c_7951"
  },
  "seeAlso": {
    "type": "StructuredValue",
    "value": [
      "https://example.org/concept/wheat",
      "https://datamodel.org/example/wheat"
    ]
  },
  "description": {
    "type": "Text",
    "value": "Spring wheat"
  },
  "relatedSource": {
    "type": "StructuredValue",
    "value": [
      {
        "application": "urn:ngsi-ld:AgriApp:72d9fb43-53f8-4ec8-a33c-fa931360259a",
        "applicationEntityId": "app:weat"
      }
    ]
  },
  "hasAgriSoil": {
    "type": "StructuredValue",
    "value": [
      "urn:ngsi-ld:AgriSoil:00411b56-bd1b-4551-96e0-a6e7fde9c840",
      "urn:ngsi-ld:AgriSoil:e8a8389a-edf5-4345-8d2c-b98ac1ce8e2a"
    ]
  },
  "hasAgriFertiliser": {
    "type": "StructuredValue",
    "value": [
      "urn:ngsi-ld:AgriFertiliser:1b0d6cf7-320c-4a2b-b2f1-4575ea850c73",
      "urn:ngsi-ld:AgriFertiliser:380973c8-4d3b-4723-a899-0c0c5cc63e7e"
    ]
  },
  "hasAgriPest": {
    "type": "StructuredValue",
    "value": [
      "urn:ngsi-ld:AgriPest:1b0d6cf7-320c-4a2b-b2f1-4575ea850c73",
      "urn:ngsi-ld:AgriPest:380973c8-4d3b-4723-a899-0c0c5cc63e7e"
    ]
  },
  "plantingFrom": {
    "type": "StructuredValue",
    "value": [
      {
        "dateRange": "-09-28/-10-12",
        "description": "Best Season"
      },
      {
        "dateRange": "-10-11/-10-18",
        "description": "Season OK"
      }
    ]
  },
  "harvestingInterval": {
    "type": "StructuredValue",
    "value": [
      {
        "dateRange": "-03-21/-04-01",
        "description": "Best Season"
      },
      {
        "dateRange": "-04-02/-04-15",
        "description": "Season OK"
      }
    ]
  },
  "wateringFrequency": {
    "type": "Text",
    "value": "daily"
  }
}
```

#### ttl
```ttl
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix ngsi-ld: <https://uri.etsi.org/ngsi-ld/> .
@prefix ns1: <https://smartdatamodels.org/dataModel.Agrifood/> .
@prefix ns2: <https://smartdatamodels.org/> .

<urn:ngsi-ld:AgriCrop:df72dc57-1eb9-42a3-88a9-8647ecc954b4> a ns1:AgriCrop ;
    ns2:alternateName [ a <file:///github/workspace/Text> ;
            ngsi-ld:hasValue "Triticum aestivum" ] ;
    ns1:agroVocConcept [ a <file:///github/workspace/Text> ;
            ngsi-ld:hasValue "http://aims.fao.org/aos/agrovoc/c_7951" ] ;
    ns1:harvestingInterval [ a <file:///github/workspace/StructuredValue> ;
            ngsi-ld:hasValue [ dcterms:description "Best Season" ;
                    ns1:dateRange "-03-21/-04-01" ],
                [ dcterms:description "Season OK" ;
                    ns1:dateRange "-04-02/-04-15" ] ] ;
    ns1:hasAgriFertiliser [ a <file:///github/workspace/StructuredValue> ;
            ngsi-ld:hasValue "urn:ngsi-ld:AgriFertiliser:1b0d6cf7-320c-4a2b-b2f1-4575ea850c73",
                "urn:ngsi-ld:AgriFertiliser:380973c8-4d3b-4723-a899-0c0c5cc63e7e" ] ;
    ns1:hasAgriPest [ a <file:///github/workspace/StructuredValue> ;
            ngsi-ld:hasValue "urn:ngsi-ld:AgriPest:1b0d6cf7-320c-4a2b-b2f1-4575ea850c73",
                "urn:ngsi-ld:AgriPest:380973c8-4d3b-4723-a899-0c0c5cc63e7e" ] ;
    ns1:hasAgriSoil [ a <file:///github/workspace/StructuredValue> ;
            ngsi-ld:hasValue "urn:ngsi-ld:AgriSoil:00411b56-bd1b-4551-96e0-a6e7fde9c840",
                "urn:ngsi-ld:AgriSoil:e8a8389a-edf5-4345-8d2c-b98ac1ce8e2a" ] ;
    ns1:plantingFrom [ a <file:///github/workspace/StructuredValue> ;
            ngsi-ld:hasValue [ dcterms:description "Season OK" ;
                    ns1:dateRange "-10-11/-10-18" ],
                [ dcterms:description "Best Season" ;
                    ns1:dateRange "-09-28/-10-12" ] ] ;
    ns1:relatedSource [ a <file:///github/workspace/StructuredValue> ;
            ngsi-ld:hasValue [ ns1:application "urn:ngsi-ld:AgriApp:72d9fb43-53f8-4ec8-a33c-fa931360259a" ;
                    ns1:applicationEntityId "app:weat" ] ] ;
    ns1:wateringFrequency [ a <file:///github/workspace/Text> ;
            ngsi-ld:hasValue "daily" ] ;
    ns2:dateCreated [ a <file:///github/workspace/DateTime> ;
            ngsi-ld:hasValue "2017-01-01T01:20:00Z" ] ;
    ns2:dateModified [ a <file:///github/workspace/DateTime> ;
            ngsi-ld:hasValue "2017-05-04T12:30:00Z" ] ;
    ns2:name [ a <file:///github/workspace/Text> ;
            ngsi-ld:hasValue "Wheat" ] ;
    ns2:seeAlso [ a <file:///github/workspace/StructuredValue> ;
            ngsi-ld:hasValue "https://datamodel.org/example/wheat",
                "https://example.org/concept/wheat" ] .


```


### AIM example
Example from AIM farm example

#### json
```json
{
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

```

#### jsonld
```jsonld
{
  "@context": "https://opengeospatial.github.io/aim-swg/build/annotated/model/agriculture/external/smart-agrifood/crop/context.jsonld",
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
```

#### ttl
```ttl
@prefix ns1: <https://smartdatamodels.org/dataModel.Agrifood/> .

<urn:ngsi-ld:crop:df72dc57-1eb9-42a3-88a9-8647ecc954b4> a <file:///github/workspace/Crop> ;
    ns1:cropStatus "seeded" ;
    ns1:lastPlantedAt "2016-08-23T10:18:16Z" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
$schemaVersion: 0.0.7
modelTags: ''
$id: https://smart-data-models.github.io/dataModel.Agrifood/AgriCrop/schema.json
title: Smart Data Models - Agri Food
description: This entity contains a harmonised description of a generic crop. This
  entity is primarily associated with the agricultural vertical and related IoT applications.
type: object
allOf:
- $ref: https://smart-data-models.github.io/data-models/common-schema.json#/definitions/GSMA-Commons
- $ref: https://smart-data-models.github.io/dataModel.Agrifood/agrifood-schema.json#/definitions/AgriFood-Commons
- properties:
    type:
      type: string
      enum:
      - AgriCrop
      description: Property. NGSI Entity Type. it has to be AgriCrop
      x-jsonld-id: '@type'
    agroVocConcept:
      type: string
      format: uri
      description: Property. Model:'http://schema.org/URL'. The link with the defined
        concept into the AgroVoc vocabulary
      x-jsonld-id: https://smartdatamodels.org/dataModel.Agrifood/agroVocConcept
    hasAgriSoil:
      type: array
      description: Relationship. Model:'http://schema.org/URL'. Reference to the recommended
        types of soil suitable for growing this crop
      items:
        anyOf:
        - type: string
          minLength: 1
          maxLength: 256
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$
          description: Property. Identifier format of any NGSI entity
        - type: string
          format: uri
          description: Property. Identifier format of any NGSI entity
      x-jsonld-id: https://smartdatamodels.org/dataModel.Agrifood/hasAgriSoil
    hasAgriFertiliser:
      type: array
      description: Relationship. Model:'http://schema.org/URL'. Reference to the recommended
        types of fertiliser suitable for growing this crop
      items:
        anyOf:
        - type: string
          minLength: 1
          maxLength: 256
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$
          description: Property. Identifier format of any NGSI entity
        - type: string
          format: uri
          description: Property. Identifier format of any NGSI entity
      x-jsonld-id: https://smartdatamodels.org/dataModel.Agrifood/hasAgriFertiliser
    hasAgriPest:
      type: array
      description: Relationship. Reference to the pests known to attack this crop.
        Model:'https://schema.org/URL'
      items:
        anyOf:
        - type: string
          minLength: 1
          maxLength: 256
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$
          description: Property. Identifier format of any NGSI entity
        - type: string
          format: uri
          description: Property. Identifier format of any NGSI entity
      x-jsonld-id: https://smartdatamodels.org/dataModel.Agrifood/hasAgriPest
    harvestingInterval:
      type: array
      description: 'Property. Model:''http://schema.org/URL''. A list of the recommended
        harvesting interval date(s) for this crop. Specified using ISO8601 repeating
        date intervals: <br/><br/>**interval, description**<br/><br/>Where **interval**
        is in the form of **start date/end date**<br/><br/>--MM-DD/--MM-DD<br/><br/>Meaning
        repeat each year from this start date to this end date'
      items:
        type: object
        properties:
          dateRange:
            type: string
            pattern: ^-[0-1][0-9]-[0-3][0-9]/-[0-1][0-9]-[0-3][0-9]$
            description: Property. Range of dates in a string format
            x-jsonld-id: https://smartdatamodels.org/dataModel.Agrifood/dateRange
          description:
            type: string
            description: Property. Descriptions of the range dates
            x-jsonld-id: http://purl.org/dc/terms/description
      minItems: 2
      maxItems: 2
      x-jsonld-id: https://smartdatamodels.org/dataModel.Agrifood/harvestingInterval
    plantingFrom:
      type: array
      description: 'Property. Model:''http://schema.org/URL''. A list of the recommended
        planting interval date(s) for this crop. Specified using ISO8601 repeating
        date intervals: <br/><br/>**interval, description**<br/><br/>Where **interval**
        is in the form of **start date/end date**<br/><br/>--MM-DD/--MM-DD<br/><br/>Meaning
        repeat each year from this start date to this end date'
      items:
        type: object
        properties:
          dateRange:
            type: string
            pattern: ^-[0-1][0-9]-[0-3][0-9]/-[0-1][0-9]-[0-3][0-9]$
            description: Property. Range of dates in a string format
            x-jsonld-id: https://smartdatamodels.org/dataModel.Agrifood/dateRange
          description:
            type: string
            description: Property. Descriptions of the range dates
            x-jsonld-id: http://purl.org/dc/terms/description
      minItems: 2
      maxItems: 2
      x-jsonld-id: https://smartdatamodels.org/dataModel.Agrifood/plantingFrom
    wateringFrequency:
      type: string
      description: 'Property. Model:''http://schema.org/URL''. Units:''''. A description
        of the recommended watering schedule. A choice from an enumerated list. One
        of: **daily, weekly, biweekly, monthly, onDemand, other**. Enum:''daily, weekly,
        biweekly, monthly, onDemand,    other'''
      enum:
      - daily
      - weekly
      - biweekly
      - monthly
      - onDemand
      - other
      x-jsonld-id: https://smartdatamodels.org/dataModel.Agrifood/wateringFrequency
required:
- id
- type
- name
x-jsonld-extra-terms:
  AgriApp: https://smartdatamodels.org/dataModel.Agrifood/AgriApp
  AgriCrop: https://smartdatamodels.org/dataModel.Agrifood/AgriCrop
  AgriFarm: https://smartdatamodels.org/dataModel.Agrifood/AgriFarm
  AgriFertilize: https://smartdatamodels.org/dataModel.Agrifood/AgriFertilize
  AgriGreenhouse: https://smartdatamodels.org/dataModel.Agrifood/AgriGreenhouse
  AgriParcel: https://smartdatamodels.org/dataModel.Agrifood/AgriParcel
  AgriParcelOperation: https://smartdatamodels.org/dataModel.Agrifood/AgriParcelOperation
  AgriParcelRecord: https://smartdatamodels.org/dataModel.Agrifood/AgriParcelRecord
  AgriPest: https://smartdatamodels.org/dataModel.Agrifood/AgriPest
  AgriPhytosanitary: https://smartdatamodels.org/dataModel.Agrifood/AgriPhytosanitary
  AgriProductType: https://smartdatamodels.org/dataModel.Agrifood/AgriProductType
  AgriSoil: https://smartdatamodels.org/dataModel.Agrifood/AgriSoil
  Animal: https://smartdatamodels.org/dataModel.Agrifood/Animal
  AnimalDisease: https://smartdatamodels.org/dataModel.Agrifood/AnimalDisease
  AnimalMovement: https://smartdatamodels.org/dataModel.Agrifood/AnimalMovement
  Carcass: https://smartdatamodels.org/dataModel.Agrifood/Carcass
  Compartment: https://smartdatamodels.org/dataModel.Agrifood/Compartment
  FeedRegistry: https://smartdatamodels.org/dataModel.Agrifood/FeedRegistry
  MeatProduct: https://smartdatamodels.org/dataModel.Agrifood/MeatProduct
  Pen: https://smartdatamodels.org/dataModel.Agrifood/Pen
  VeterinarianTreatment: https://smartdatamodels.org/dataModel.Agrifood/VeterinarianTreatment
  aacm: https://smartdatamodels.org/dataModel.Agrifood/aacm
  additionalInfo: https://smartdatamodels.org/dataModel.Agrifood/additionalInfo
  address: https://smartdatamodels.org/address
  addressCountry: https://smartdatamodels.org/addressCountry
  addressLocality: https://smartdatamodels.org/addressLocality
  addressRegion: https://smartdatamodels.org/addressRegion
  alternateName: https://smartdatamodels.org/alternateName
  amount: https://smartdatamodels.org/dataModel.Agrifood/amount
  animal: https://smartdatamodels.org/dataModel.Agrifood/animal
  animals: https://smartdatamodels.org/dataModel.Agrifood/animals
  application: https://smartdatamodels.org/dataModel.Agrifood/application
  applicationEntityId: https://smartdatamodels.org/dataModel.Agrifood/applicationEntityId
  appliedProduct: https://smartdatamodels.org/dataModel.Agrifood/appliedProduct
  area: https://smartdatamodels.org/dataModel.Agrifood/area
  areaServed: https://smartdatamodels.org/areaServed
  arrivalTimestamp: https://smartdatamodels.org/dataModel.Agrifood/arrivalTimestamp
  atmosphericPressure: https://smartdatamodels.org/dataModel.Agrifood/atmosphericPressure
  availabilityRestriction: https://smartdatamodels.org/availabilityRestriction
  availableLanguage: https://smartdatamodels.org/availableLanguage
  avgGrowth: https://smartdatamodels.org/dataModel.Agrifood/avgGrowth
  avgWeight: https://smartdatamodels.org/dataModel.Agrifood/avgWeight
  batch: https://smartdatamodels.org/dataModel.Agrifood/batch
  bbox:
    x-jsonld-container: '@list'
    x-jsonld-id: https://purl.org/geojson/vocab#bbox
  belongsTo: https://smartdatamodels.org/dataModel.Agrifood/belongsTo
  bill: https://smartdatamodels.org/dataModel.Agrifood/bill
  birthdate: https://smartdatamodels.org/dataModel.Agrifood/birthdate
  breed: https://smartdatamodels.org/dataModel.Agrifood/breed
  buildingId: https://smartdatamodels.org/dataModel.Agrifood/buildingId
  calvedBy: https://smartdatamodels.org/dataModel.Agrifood/calvedBy
  carcass: https://smartdatamodels.org/dataModel.Agrifood/carcass
  category: https://smartdatamodels.org/dataModel.Agrifood/category
  cdate: https://smartdatamodels.org/dataModel.Agrifood/cdate
  check: https://smartdatamodels.org/dataModel.Agrifood/check
  ci: https://smartdatamodels.org/dataModel.Agrifood/ci
  co2: https://smartdatamodels.org/dataModel.Agrifood/co2
  code: https://smartdatamodels.org/dataModel.Agrifood/code
  comp: https://smartdatamodels.org/dataModel.Agrifood/comp
  companyId: https://smartdatamodels.org/dataModel.Agrifood/companyId
  compartmentId: https://smartdatamodels.org/dataModel.Agrifood/compartmentId
  contactOption: https://smartdatamodels.org/contactOption
  contactPoint: https://smartdatamodels.org/contactPoint
  contactType: https://smartdatamodels.org/contactType
  coordinates:
    x-jsonld-container: '@list'
    x-jsonld-id: https://purl.org/geojson/vocab#coordinates
  cropStatus: https://smartdatamodels.org/dataModel.Agrifood/cropStatus
  dailyLight: https://smartdatamodels.org/dataModel.Agrifood/dailyLight
  dataProvider: https://smartdatamodels.org/dataProvider
  date: https://smartdatamodels.org/dataModel.Agrifood/date
  dateCreated: https://smartdatamodels.org/dateCreated
  dateModified: https://smartdatamodels.org/dateModified
  deadAnimalsSinceDateOfArrival: https://smartdatamodels.org/dataModel.Agrifood/deadAnimalsSinceDateOfArrival
  deliveryNote: https://smartdatamodels.org/dataModel.Agrifood/deliveryNote
  depth: https://smartdatamodels.org/dataModel.Agrifood/depth
  detail: https://uri.etsi.org/ngsi-ld/detail
  diagnosticTest: https://smartdatamodels.org/dataModel.Agrifood/diagnosticTest
  disease: https://smartdatamodels.org/dataModel.Agrifood/disease
  distributed: https://smartdatamodels.org/dataModel.Agrifood/distributed
  district: https://smartdatamodels.org/district
  dose: https://smartdatamodels.org/dataModel.Agrifood/dose
  drainFlow: https://smartdatamodels.org/dataModel.Agrifood/drainFlow
  dt: https://smartdatamodels.org/dataModel.Agrifood/dt
  edate: https://smartdatamodels.org/dataModel.Agrifood/edate
  efficacy: https://smartdatamodels.org/dataModel.Agrifood/efficacy
  email: https://smartdatamodels.org/email
  empty: https://smartdatamodels.org/dataModel.Agrifood/empty
  enddate: https://smartdatamodels.org/dataModel.Agrifood/enddate
  endedAt: https://smartdatamodels.org/dataModel.Agrifood/endedAt
  endpoint: https://uri.etsi.org/ngsi-ld/endpoint
  entrylimit: https://smartdatamodels.org/dataModel.Agrifood/entrylimit
  farm: https://smartdatamodels.org/dataModel.Agrifood/farm
  farmId: https://smartdatamodels.org/dataModel.Agrifood/farmId
  faxNumber: https://smartdatamodels.org/faxNumber
  fedWith: https://smartdatamodels.org/dataModel.Agrifood/fedWith
  feedConsumption: https://smartdatamodels.org/dataModel.Agrifood/feedConsumption
  hasAgriCrop: https://smartdatamodels.org/dataModel.Agrifood/hasAgriCrop
  hasAgriParcel: https://smartdatamodels.org/dataModel.Agrifood/hasAgriParcel
  hasAgriParcelChildren: https://smartdatamodels.org/dataModel.Agrifood/hasAgriParcelChildren
  hasAgriParcelParent: https://smartdatamodels.org/dataModel.Agrifood/hasAgriParcelParent
  hasAgriProductType: https://smartdatamodels.org/dataModel.Agrifood/hasAgriProductType
  hasAgriProductTypeChildren: https://smartdatamodels.org/dataModel.Agrifood/hasAgriProductTypeChildren
  hasAgriProductTypeParent: https://smartdatamodels.org/dataModel.Agrifood/hasAgriProductTypeParent
  hasAirQualityObserved: https://smartdatamodels.org/dataModel.Agrifood/hasAirQualityObserved
  hasBuilding: https://smartdatamodels.org/dataModel.Agrifood/hasBuilding
  hasDevice: https://smartdatamodels.org/dataModel.Agrifood/hasDevice
  hasOperator: https://smartdatamodels.org/dataModel.Agrifood/hasOperator
  hasProvider: https://smartdatamodels.org/dataModel.Agrifood/hasProvider
  hasWaterQualityObserved: https://smartdatamodels.org/dataModel.Agrifood/hasWaterQualityObserved
  hasWeatherObserved: https://smartdatamodels.org/dataModel.Agrifood/hasWeatherObserved
  healthCondition: https://smartdatamodels.org/dataModel.Agrifood/healthCondition
  hecm: https://smartdatamodels.org/dataModel.Agrifood/hecm
  humidity: https://smartdatamodels.org/dataModel.Agrifood/humidity
  id: '@id'
  idate: https://smartdatamodels.org/dataModel.Agrifood/idate
  idcp: https://smartdatamodels.org/dataModel.Agrifood/idcp
  idmachine: https://smartdatamodels.org/dataModel.Agrifood/idmachine
  idpdf: https://smartdatamodels.org/dataModel.Agrifood/idpdf
  idtf: https://smartdatamodels.org/dataModel.Agrifood/idtf
  idtpismv: https://smartdatamodels.org/dataModel.Agrifood/idtpismv
  infection: https://smartdatamodels.org/dataModel.Agrifood/infection
  inidate: https://smartdatamodels.org/dataModel.Agrifood/inidate
  initialWeight: https://smartdatamodels.org/dataModel.Agrifood/initialWeight
  irrigationRecord: https://smartdatamodels.org/dataModel.Agrifood/irrigationRecord
  irrigationSystemType: https://smartdatamodels.org/dataModel.Agrifood/irrigationSystemType
  landLocation: https://smartdatamodels.org/dataModel.Agrifood/landLocation
  lastPlantedAt: https://smartdatamodels.org/dataModel.Agrifood/lastPlantedAt
  lastUpdate: https://smartdatamodels.org/dataModel.Agrifood/lastUpdate
  ldate: https://smartdatamodels.org/dataModel.Agrifood/ldate
  leafRelativeHumidity: https://smartdatamodels.org/dataModel.Agrifood/leafRelativeHumidity
  leafTemperature: https://smartdatamodels.org/dataModel.Agrifood/leafTemperature
  leafWetness: https://smartdatamodels.org/dataModel.Agrifood/leafWetness
  legalId: https://smartdatamodels.org/dataModel.Agrifood/legalId
  locatedAt: https://smartdatamodels.org/dataModel.Agrifood/locatedAt
  location: https://uri.etsi.org/ngsi-ld/location
  loginname: https://smartdatamodels.org/dataModel.Agrifood/loginname
  luminosity: https://smartdatamodels.org/dataModel.Agrifood/luminosity
  machine: https://smartdatamodels.org/dataModel.Agrifood/machine
  macm: https://smartdatamodels.org/dataModel.Agrifood/macm
  maf: https://smartdatamodels.org/dataModel.Agrifood/maf
  manure: https://smartdatamodels.org/dataModel.Agrifood/manure
  matdet: https://smartdatamodels.org/dataModel.Agrifood/matdet
  material: https://smartdatamodels.org/dataModel.Agrifood/material
  maxValue: https://smartdatamodels.org/dataModel.Agrifood/maxValue
  mdt: https://smartdatamodels.org/dataModel.Agrifood/mdt
  measur: https://smartdatamodels.org/dataModel.Agrifood/measur
  measure: https://smartdatamodels.org/dataModel.Agrifood/measure
  metadata: https://smartdatamodels.org/dataModel.Agrifood/metadata
  micm: https://smartdatamodels.org/dataModel.Agrifood/micm
  minValue: https://smartdatamodels.org/dataModel.Agrifood/minValue
  mix: https://smartdatamodels.org/dataModel.Agrifood/mix
  mmcm: https://smartdatamodels.org/dataModel.Agrifood/mmcm
  movement: https://smartdatamodels.org/dataModel.Agrifood/movement
  msoup: https://smartdatamodels.org/dataModel.Agrifood/msoup
  mst: https://smartdatamodels.org/dataModel.Agrifood/mst
  mud: https://smartdatamodels.org/dataModel.Agrifood/mud
  name: https://smartdatamodels.org/name
  names: https://smartdatamodels.org/dataModel.Agrifood/names
  notes: https://smartdatamodels.org/dataModel.Agrifood/notes
  numAnimals: https://smartdatamodels.org/dataModel.Agrifood/numAnimals
  operationType: https://smartdatamodels.org/dataModel.Agrifood/operationType
  ownedBy: https://smartdatamodels.org/dataModel.Agrifood/ownedBy
  owner: https://smartdatamodels.org/owner
  parameter: https://smartdatamodels.org/dataModel.Agrifood/parameter
  parcel: https://smartdatamodels.org/dataModel.Agrifood/parcel
  parentCompartmentId: https://smartdatamodels.org/dataModel.Agrifood/parentCompartmentId
  pen: https://smartdatamodels.org/dataModel.Agrifood/pen
  phaseOutPeriod: https://smartdatamodels.org/dataModel.Agrifood/phaseOutPeriod
  phenologicalCondition: https://smartdatamodels.org/dataModel.Agrifood/phenologicalCondition
  plan: https://smartdatamodels.org/dataModel.Agrifood/plan
  plannedEndAt: https://smartdatamodels.org/dataModel.Agrifood/plannedEndAt
  plannedStartAt: https://smartdatamodels.org/dataModel.Agrifood/plannedStartAt
  postOfficeBoxNumber: https://smartdatamodels.org/postOfficeBoxNumber
  postalCode: https://smartdatamodels.org/postalCode
  pp: https://smartdatamodels.org/dataModel.Agrifood/pp
  preventive: https://smartdatamodels.org/dataModel.Agrifood/preventive
  prior: https://smartdatamodels.org/dataModel.Agrifood/prior
  prod: https://smartdatamodels.org/dataModel.Agrifood/prod
  product: https://smartdatamodels.org/dataModel.Agrifood/product
  productSupported: https://smartdatamodels.org/productSupported
  quantity: https://smartdatamodels.org/dataModel.Agrifood/quantity
  r10: https://smartdatamodels.org/dataModel.Agrifood/r10
  rdate: https://smartdatamodels.org/dataModel.Agrifood/rdate
  recipe: https://smartdatamodels.org/dataModel.Agrifood/recipe
  relatedSource: https://smartdatamodels.org/dataModel.Agrifood/relatedSource
  relativeHumidity: https://smartdatamodels.org/dataModel.Agrifood/relativeHumidity
  reportedAt: https://smartdatamodels.org/dataModel.Agrifood/reportedAt
  reproductiveCondition: https://smartdatamodels.org/dataModel.Agrifood/reproductiveCondition
  result: https://smartdatamodels.org/dataModel.Agrifood/result
  root: https://smartdatamodels.org/dataModel.Agrifood/root
  seclimit: https://smartdatamodels.org/dataModel.Agrifood/seclimit
  seeAlso: https://smartdatamodels.org/seeAlso
  sex: https://smartdatamodels.org/dataModel.Agrifood/sex
  siredBy: https://smartdatamodels.org/dataModel.Agrifood/siredBy
  soilMoistureEc: https://smartdatamodels.org/dataModel.Agrifood/soilMoistureEc
  soilMoistureVwc: https://smartdatamodels.org/dataModel.Agrifood/soilMoistureVwc
  soilSalinity: https://smartdatamodels.org/dataModel.Agrifood/soilSalinity
  soilTemperature: https://smartdatamodels.org/dataModel.Agrifood/soilTemperature
  soilTextureType: https://smartdatamodels.org/dataModel.Agrifood/soilTextureType
  solarRadiation: https://smartdatamodels.org/dataModel.Agrifood/solarRadiation
  soup: https://smartdatamodels.org/dataModel.Agrifood/soup
  source: https://smartdatamodels.org/source
  species: https://smartdatamodels.org/dataModel.Agrifood/species
  speed: https://smartdatamodels.org/dataModel.Agrifood/speed
  st: https://smartdatamodels.org/dataModel.Agrifood/st
  startedAt: https://smartdatamodels.org/dataModel.Agrifood/startedAt
  status: https://uri.etsi.org/ngsi-ld/status
  streetAddress: https://smartdatamodels.org/streetAddress
  streetNr: https://smartdatamodels.org/streetNr
  subcode: https://smartdatamodels.org/dataModel.Agrifood/subcode
  subs: https://smartdatamodels.org/dataModel.Agrifood/subs
  subtype: https://smartdatamodels.org/dataModel.Agrifood/subtype
  supplier: https://smartdatamodels.org/dataModel.Agrifood/supplier
  surface: https://smartdatamodels.org/dataModel.Agrifood/surface
  surname: https://smartdatamodels.org/dataModel.Agrifood/surname
  symbol: https://smartdatamodels.org/dataModel.Agrifood/symbol
  taf: https://smartdatamodels.org/dataModel.Agrifood/taf
  target: https://smartdatamodels.org/dataModel.Agrifood/target
  telephone: https://smartdatamodels.org/telephone
  temperature: https://smartdatamodels.org/dataModel.Agrifood/temperature
  tj: https://smartdatamodels.org/dataModel.Agrifood/tj
  tmi: https://smartdatamodels.org/dataModel.Agrifood/tmi
  typerisk: https://smartdatamodels.org/dataModel.Agrifood/typerisk
  typsoil: https://smartdatamodels.org/dataModel.Agrifood/typsoil
  unitText: https://smartdatamodels.org/dataModel.Agrifood/unitText
  url: https://smartdatamodels.org/url
  user: https://smartdatamodels.org/dataModel.Agrifood/user
  value: https://uri.etsi.org/ngsi-ld/hasValue
  vat: https://smartdatamodels.org/dataModel.Agrifood/vat
  version: https://smartdatamodels.org/dataModel.Agrifood/version
  veterinarian: https://smartdatamodels.org/dataModel.Agrifood/veterinarian
  veterinarianTreatment: https://smartdatamodels.org/dataModel.Agrifood/veterinarianTreatment
  waterConsumption: https://smartdatamodels.org/dataModel.Agrifood/waterConsumption
  waterSource: https://smartdatamodels.org/dataModel.Agrifood/waterSource
  weight: https://smartdatamodels.org/dataModel.Agrifood/weight
  weightStDev: https://smartdatamodels.org/dataModel.Agrifood/weightStDev
  welfareCondition: https://smartdatamodels.org/dataModel.Agrifood/welfareCondition
  workOrder: https://smartdatamodels.org/dataModel.Agrifood/workOrder
  workRecord: https://smartdatamodels.org/dataModel.Agrifood/workRecord
x-jsonld-prefixes:
  ngsi-ld: https://uri.etsi.org/ngsi-ld/

```

Links to the schema:

* YAML version: [schema.yaml](https://opengeospatial.github.io/aim-swg/build/annotated/model/agriculture/external/smart-agrifood/crop/schema.json)
* JSON version: [schema.json](https://opengeospatial.github.io/aim-swg/build/annotated/model/agriculture/external/smart-agrifood/crop/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "id": "@id",
    "dateCreated": "https://smartdatamodels.org/dateCreated",
    "dateModified": "https://smartdatamodels.org/dateModified",
    "source": "https://smartdatamodels.org/source",
    "name": "https://smartdatamodels.org/name",
    "alternateName": "https://smartdatamodels.org/alternateName",
    "dataProvider": "https://smartdatamodels.org/dataProvider",
    "owner": "https://smartdatamodels.org/owner",
    "seeAlso": "https://smartdatamodels.org/seeAlso",
    "relatedSource": "https://smartdatamodels.org/dataModel.Agrifood/relatedSource",
    "type": "@type",
    "agroVocConcept": "https://smartdatamodels.org/dataModel.Agrifood/agroVocConcept",
    "hasAgriSoil": "https://smartdatamodels.org/dataModel.Agrifood/hasAgriSoil",
    "hasAgriFertiliser": "https://smartdatamodels.org/dataModel.Agrifood/hasAgriFertiliser",
    "hasAgriPest": "https://smartdatamodels.org/dataModel.Agrifood/hasAgriPest",
    "harvestingInterval": {
      "@context": {
        "dateRange": "https://smartdatamodels.org/dataModel.Agrifood/dateRange",
        "description": "http://purl.org/dc/terms/description"
      },
      "@id": "https://smartdatamodels.org/dataModel.Agrifood/harvestingInterval"
    },
    "plantingFrom": {
      "@context": {
        "dateRange": "https://smartdatamodels.org/dataModel.Agrifood/dateRange",
        "description": "http://purl.org/dc/terms/description"
      },
      "@id": "https://smartdatamodels.org/dataModel.Agrifood/plantingFrom"
    },
    "wateringFrequency": "https://smartdatamodels.org/dataModel.Agrifood/wateringFrequency",
    "AgriApp": "https://smartdatamodels.org/dataModel.Agrifood/AgriApp",
    "AgriCrop": "https://smartdatamodels.org/dataModel.Agrifood/AgriCrop",
    "AgriFarm": "https://smartdatamodels.org/dataModel.Agrifood/AgriFarm",
    "AgriFertilize": "https://smartdatamodels.org/dataModel.Agrifood/AgriFertilize",
    "AgriGreenhouse": "https://smartdatamodels.org/dataModel.Agrifood/AgriGreenhouse",
    "AgriParcel": "https://smartdatamodels.org/dataModel.Agrifood/AgriParcel",
    "AgriParcelOperation": "https://smartdatamodels.org/dataModel.Agrifood/AgriParcelOperation",
    "AgriParcelRecord": "https://smartdatamodels.org/dataModel.Agrifood/AgriParcelRecord",
    "AgriPest": "https://smartdatamodels.org/dataModel.Agrifood/AgriPest",
    "AgriPhytosanitary": "https://smartdatamodels.org/dataModel.Agrifood/AgriPhytosanitary",
    "AgriProductType": "https://smartdatamodels.org/dataModel.Agrifood/AgriProductType",
    "AgriSoil": "https://smartdatamodels.org/dataModel.Agrifood/AgriSoil",
    "Animal": "https://smartdatamodels.org/dataModel.Agrifood/Animal",
    "AnimalDisease": "https://smartdatamodels.org/dataModel.Agrifood/AnimalDisease",
    "AnimalMovement": "https://smartdatamodels.org/dataModel.Agrifood/AnimalMovement",
    "Carcass": "https://smartdatamodels.org/dataModel.Agrifood/Carcass",
    "Compartment": "https://smartdatamodels.org/dataModel.Agrifood/Compartment",
    "FeedRegistry": "https://smartdatamodels.org/dataModel.Agrifood/FeedRegistry",
    "MeatProduct": "https://smartdatamodels.org/dataModel.Agrifood/MeatProduct",
    "Pen": "https://smartdatamodels.org/dataModel.Agrifood/Pen",
    "VeterinarianTreatment": "https://smartdatamodels.org/dataModel.Agrifood/VeterinarianTreatment",
    "aacm": "https://smartdatamodels.org/dataModel.Agrifood/aacm",
    "additionalInfo": "https://smartdatamodels.org/dataModel.Agrifood/additionalInfo",
    "address": "https://smartdatamodels.org/address",
    "addressCountry": "https://smartdatamodels.org/addressCountry",
    "addressLocality": "https://smartdatamodels.org/addressLocality",
    "addressRegion": "https://smartdatamodels.org/addressRegion",
    "amount": "https://smartdatamodels.org/dataModel.Agrifood/amount",
    "animal": "https://smartdatamodels.org/dataModel.Agrifood/animal",
    "animals": "https://smartdatamodels.org/dataModel.Agrifood/animals",
    "application": "https://smartdatamodels.org/dataModel.Agrifood/application",
    "applicationEntityId": "https://smartdatamodels.org/dataModel.Agrifood/applicationEntityId",
    "appliedProduct": "https://smartdatamodels.org/dataModel.Agrifood/appliedProduct",
    "area": "https://smartdatamodels.org/dataModel.Agrifood/area",
    "areaServed": "https://smartdatamodels.org/areaServed",
    "arrivalTimestamp": "https://smartdatamodels.org/dataModel.Agrifood/arrivalTimestamp",
    "atmosphericPressure": "https://smartdatamodels.org/dataModel.Agrifood/atmosphericPressure",
    "availabilityRestriction": "https://smartdatamodels.org/availabilityRestriction",
    "availableLanguage": "https://smartdatamodels.org/availableLanguage",
    "avgGrowth": "https://smartdatamodels.org/dataModel.Agrifood/avgGrowth",
    "avgWeight": "https://smartdatamodels.org/dataModel.Agrifood/avgWeight",
    "batch": "https://smartdatamodels.org/dataModel.Agrifood/batch",
    "bbox": {
      "@container": "@list",
      "@id": "https://purl.org/geojson/vocab#bbox"
    },
    "belongsTo": "https://smartdatamodels.org/dataModel.Agrifood/belongsTo",
    "bill": "https://smartdatamodels.org/dataModel.Agrifood/bill",
    "birthdate": "https://smartdatamodels.org/dataModel.Agrifood/birthdate",
    "breed": "https://smartdatamodels.org/dataModel.Agrifood/breed",
    "buildingId": "https://smartdatamodels.org/dataModel.Agrifood/buildingId",
    "calvedBy": "https://smartdatamodels.org/dataModel.Agrifood/calvedBy",
    "carcass": "https://smartdatamodels.org/dataModel.Agrifood/carcass",
    "category": "https://smartdatamodels.org/dataModel.Agrifood/category",
    "cdate": "https://smartdatamodels.org/dataModel.Agrifood/cdate",
    "check": "https://smartdatamodels.org/dataModel.Agrifood/check",
    "ci": "https://smartdatamodels.org/dataModel.Agrifood/ci",
    "co2": "https://smartdatamodels.org/dataModel.Agrifood/co2",
    "code": "https://smartdatamodels.org/dataModel.Agrifood/code",
    "comp": "https://smartdatamodels.org/dataModel.Agrifood/comp",
    "companyId": "https://smartdatamodels.org/dataModel.Agrifood/companyId",
    "compartmentId": "https://smartdatamodels.org/dataModel.Agrifood/compartmentId",
    "contactOption": "https://smartdatamodels.org/contactOption",
    "contactPoint": "https://smartdatamodels.org/contactPoint",
    "contactType": "https://smartdatamodels.org/contactType",
    "coordinates": {
      "@container": "@list",
      "@id": "https://purl.org/geojson/vocab#coordinates"
    },
    "cropStatus": "https://smartdatamodels.org/dataModel.Agrifood/cropStatus",
    "dailyLight": "https://smartdatamodels.org/dataModel.Agrifood/dailyLight",
    "date": "https://smartdatamodels.org/dataModel.Agrifood/date",
    "deadAnimalsSinceDateOfArrival": "https://smartdatamodels.org/dataModel.Agrifood/deadAnimalsSinceDateOfArrival",
    "deliveryNote": "https://smartdatamodels.org/dataModel.Agrifood/deliveryNote",
    "depth": "https://smartdatamodels.org/dataModel.Agrifood/depth",
    "detail": "ngsi-ld:detail",
    "diagnosticTest": "https://smartdatamodels.org/dataModel.Agrifood/diagnosticTest",
    "disease": "https://smartdatamodels.org/dataModel.Agrifood/disease",
    "distributed": "https://smartdatamodels.org/dataModel.Agrifood/distributed",
    "district": "https://smartdatamodels.org/district",
    "dose": "https://smartdatamodels.org/dataModel.Agrifood/dose",
    "drainFlow": "https://smartdatamodels.org/dataModel.Agrifood/drainFlow",
    "dt": "https://smartdatamodels.org/dataModel.Agrifood/dt",
    "edate": "https://smartdatamodels.org/dataModel.Agrifood/edate",
    "efficacy": "https://smartdatamodels.org/dataModel.Agrifood/efficacy",
    "email": "https://smartdatamodels.org/email",
    "empty": "https://smartdatamodels.org/dataModel.Agrifood/empty",
    "enddate": "https://smartdatamodels.org/dataModel.Agrifood/enddate",
    "endedAt": "https://smartdatamodels.org/dataModel.Agrifood/endedAt",
    "endpoint": "ngsi-ld:endpoint",
    "entrylimit": "https://smartdatamodels.org/dataModel.Agrifood/entrylimit",
    "farm": "https://smartdatamodels.org/dataModel.Agrifood/farm",
    "farmId": "https://smartdatamodels.org/dataModel.Agrifood/farmId",
    "faxNumber": "https://smartdatamodels.org/faxNumber",
    "fedWith": "https://smartdatamodels.org/dataModel.Agrifood/fedWith",
    "feedConsumption": "https://smartdatamodels.org/dataModel.Agrifood/feedConsumption",
    "hasAgriCrop": "https://smartdatamodels.org/dataModel.Agrifood/hasAgriCrop",
    "hasAgriParcel": "https://smartdatamodels.org/dataModel.Agrifood/hasAgriParcel",
    "hasAgriParcelChildren": "https://smartdatamodels.org/dataModel.Agrifood/hasAgriParcelChildren",
    "hasAgriParcelParent": "https://smartdatamodels.org/dataModel.Agrifood/hasAgriParcelParent",
    "hasAgriProductType": "https://smartdatamodels.org/dataModel.Agrifood/hasAgriProductType",
    "hasAgriProductTypeChildren": "https://smartdatamodels.org/dataModel.Agrifood/hasAgriProductTypeChildren",
    "hasAgriProductTypeParent": "https://smartdatamodels.org/dataModel.Agrifood/hasAgriProductTypeParent",
    "hasAirQualityObserved": "https://smartdatamodels.org/dataModel.Agrifood/hasAirQualityObserved",
    "hasBuilding": "https://smartdatamodels.org/dataModel.Agrifood/hasBuilding",
    "hasDevice": "https://smartdatamodels.org/dataModel.Agrifood/hasDevice",
    "hasOperator": "https://smartdatamodels.org/dataModel.Agrifood/hasOperator",
    "hasProvider": "https://smartdatamodels.org/dataModel.Agrifood/hasProvider",
    "hasWaterQualityObserved": "https://smartdatamodels.org/dataModel.Agrifood/hasWaterQualityObserved",
    "hasWeatherObserved": "https://smartdatamodels.org/dataModel.Agrifood/hasWeatherObserved",
    "healthCondition": "https://smartdatamodels.org/dataModel.Agrifood/healthCondition",
    "hecm": "https://smartdatamodels.org/dataModel.Agrifood/hecm",
    "humidity": "https://smartdatamodels.org/dataModel.Agrifood/humidity",
    "idate": "https://smartdatamodels.org/dataModel.Agrifood/idate",
    "idcp": "https://smartdatamodels.org/dataModel.Agrifood/idcp",
    "idmachine": "https://smartdatamodels.org/dataModel.Agrifood/idmachine",
    "idpdf": "https://smartdatamodels.org/dataModel.Agrifood/idpdf",
    "idtf": "https://smartdatamodels.org/dataModel.Agrifood/idtf",
    "idtpismv": "https://smartdatamodels.org/dataModel.Agrifood/idtpismv",
    "infection": "https://smartdatamodels.org/dataModel.Agrifood/infection",
    "inidate": "https://smartdatamodels.org/dataModel.Agrifood/inidate",
    "initialWeight": "https://smartdatamodels.org/dataModel.Agrifood/initialWeight",
    "irrigationRecord": "https://smartdatamodels.org/dataModel.Agrifood/irrigationRecord",
    "irrigationSystemType": "https://smartdatamodels.org/dataModel.Agrifood/irrigationSystemType",
    "landLocation": "https://smartdatamodels.org/dataModel.Agrifood/landLocation",
    "lastPlantedAt": "https://smartdatamodels.org/dataModel.Agrifood/lastPlantedAt",
    "lastUpdate": "https://smartdatamodels.org/dataModel.Agrifood/lastUpdate",
    "ldate": "https://smartdatamodels.org/dataModel.Agrifood/ldate",
    "leafRelativeHumidity": "https://smartdatamodels.org/dataModel.Agrifood/leafRelativeHumidity",
    "leafTemperature": "https://smartdatamodels.org/dataModel.Agrifood/leafTemperature",
    "leafWetness": "https://smartdatamodels.org/dataModel.Agrifood/leafWetness",
    "legalId": "https://smartdatamodels.org/dataModel.Agrifood/legalId",
    "locatedAt": "https://smartdatamodels.org/dataModel.Agrifood/locatedAt",
    "location": "ngsi-ld:location",
    "loginname": "https://smartdatamodels.org/dataModel.Agrifood/loginname",
    "luminosity": "https://smartdatamodels.org/dataModel.Agrifood/luminosity",
    "machine": "https://smartdatamodels.org/dataModel.Agrifood/machine",
    "macm": "https://smartdatamodels.org/dataModel.Agrifood/macm",
    "maf": "https://smartdatamodels.org/dataModel.Agrifood/maf",
    "manure": "https://smartdatamodels.org/dataModel.Agrifood/manure",
    "matdet": "https://smartdatamodels.org/dataModel.Agrifood/matdet",
    "material": "https://smartdatamodels.org/dataModel.Agrifood/material",
    "maxValue": "https://smartdatamodels.org/dataModel.Agrifood/maxValue",
    "mdt": "https://smartdatamodels.org/dataModel.Agrifood/mdt",
    "measur": "https://smartdatamodels.org/dataModel.Agrifood/measur",
    "measure": "https://smartdatamodels.org/dataModel.Agrifood/measure",
    "metadata": "https://smartdatamodels.org/dataModel.Agrifood/metadata",
    "micm": "https://smartdatamodels.org/dataModel.Agrifood/micm",
    "minValue": "https://smartdatamodels.org/dataModel.Agrifood/minValue",
    "mix": "https://smartdatamodels.org/dataModel.Agrifood/mix",
    "mmcm": "https://smartdatamodels.org/dataModel.Agrifood/mmcm",
    "movement": "https://smartdatamodels.org/dataModel.Agrifood/movement",
    "msoup": "https://smartdatamodels.org/dataModel.Agrifood/msoup",
    "mst": "https://smartdatamodels.org/dataModel.Agrifood/mst",
    "mud": "https://smartdatamodels.org/dataModel.Agrifood/mud",
    "names": "https://smartdatamodels.org/dataModel.Agrifood/names",
    "notes": "https://smartdatamodels.org/dataModel.Agrifood/notes",
    "numAnimals": "https://smartdatamodels.org/dataModel.Agrifood/numAnimals",
    "operationType": "https://smartdatamodels.org/dataModel.Agrifood/operationType",
    "ownedBy": "https://smartdatamodels.org/dataModel.Agrifood/ownedBy",
    "parameter": "https://smartdatamodels.org/dataModel.Agrifood/parameter",
    "parcel": "https://smartdatamodels.org/dataModel.Agrifood/parcel",
    "parentCompartmentId": "https://smartdatamodels.org/dataModel.Agrifood/parentCompartmentId",
    "pen": "https://smartdatamodels.org/dataModel.Agrifood/pen",
    "phaseOutPeriod": "https://smartdatamodels.org/dataModel.Agrifood/phaseOutPeriod",
    "phenologicalCondition": "https://smartdatamodels.org/dataModel.Agrifood/phenologicalCondition",
    "plan": "https://smartdatamodels.org/dataModel.Agrifood/plan",
    "plannedEndAt": "https://smartdatamodels.org/dataModel.Agrifood/plannedEndAt",
    "plannedStartAt": "https://smartdatamodels.org/dataModel.Agrifood/plannedStartAt",
    "postOfficeBoxNumber": "https://smartdatamodels.org/postOfficeBoxNumber",
    "postalCode": "https://smartdatamodels.org/postalCode",
    "pp": "https://smartdatamodels.org/dataModel.Agrifood/pp",
    "preventive": "https://smartdatamodels.org/dataModel.Agrifood/preventive",
    "prior": "https://smartdatamodels.org/dataModel.Agrifood/prior",
    "prod": "https://smartdatamodels.org/dataModel.Agrifood/prod",
    "product": "https://smartdatamodels.org/dataModel.Agrifood/product",
    "productSupported": "https://smartdatamodels.org/productSupported",
    "quantity": "https://smartdatamodels.org/dataModel.Agrifood/quantity",
    "r10": "https://smartdatamodels.org/dataModel.Agrifood/r10",
    "rdate": "https://smartdatamodels.org/dataModel.Agrifood/rdate",
    "recipe": "https://smartdatamodels.org/dataModel.Agrifood/recipe",
    "relativeHumidity": "https://smartdatamodels.org/dataModel.Agrifood/relativeHumidity",
    "reportedAt": "https://smartdatamodels.org/dataModel.Agrifood/reportedAt",
    "reproductiveCondition": "https://smartdatamodels.org/dataModel.Agrifood/reproductiveCondition",
    "result": "https://smartdatamodels.org/dataModel.Agrifood/result",
    "root": "https://smartdatamodels.org/dataModel.Agrifood/root",
    "seclimit": "https://smartdatamodels.org/dataModel.Agrifood/seclimit",
    "sex": "https://smartdatamodels.org/dataModel.Agrifood/sex",
    "siredBy": "https://smartdatamodels.org/dataModel.Agrifood/siredBy",
    "soilMoistureEc": "https://smartdatamodels.org/dataModel.Agrifood/soilMoistureEc",
    "soilMoistureVwc": "https://smartdatamodels.org/dataModel.Agrifood/soilMoistureVwc",
    "soilSalinity": "https://smartdatamodels.org/dataModel.Agrifood/soilSalinity",
    "soilTemperature": "https://smartdatamodels.org/dataModel.Agrifood/soilTemperature",
    "soilTextureType": "https://smartdatamodels.org/dataModel.Agrifood/soilTextureType",
    "solarRadiation": "https://smartdatamodels.org/dataModel.Agrifood/solarRadiation",
    "soup": "https://smartdatamodels.org/dataModel.Agrifood/soup",
    "species": "https://smartdatamodels.org/dataModel.Agrifood/species",
    "speed": "https://smartdatamodels.org/dataModel.Agrifood/speed",
    "st": "https://smartdatamodels.org/dataModel.Agrifood/st",
    "startedAt": "https://smartdatamodels.org/dataModel.Agrifood/startedAt",
    "status": "ngsi-ld:status",
    "streetAddress": "https://smartdatamodels.org/streetAddress",
    "streetNr": "https://smartdatamodels.org/streetNr",
    "subcode": "https://smartdatamodels.org/dataModel.Agrifood/subcode",
    "subs": "https://smartdatamodels.org/dataModel.Agrifood/subs",
    "subtype": "https://smartdatamodels.org/dataModel.Agrifood/subtype",
    "supplier": "https://smartdatamodels.org/dataModel.Agrifood/supplier",
    "surface": "https://smartdatamodels.org/dataModel.Agrifood/surface",
    "surname": "https://smartdatamodels.org/dataModel.Agrifood/surname",
    "symbol": "https://smartdatamodels.org/dataModel.Agrifood/symbol",
    "taf": "https://smartdatamodels.org/dataModel.Agrifood/taf",
    "target": "https://smartdatamodels.org/dataModel.Agrifood/target",
    "telephone": "https://smartdatamodels.org/telephone",
    "temperature": "https://smartdatamodels.org/dataModel.Agrifood/temperature",
    "tj": "https://smartdatamodels.org/dataModel.Agrifood/tj",
    "tmi": "https://smartdatamodels.org/dataModel.Agrifood/tmi",
    "typerisk": "https://smartdatamodels.org/dataModel.Agrifood/typerisk",
    "typsoil": "https://smartdatamodels.org/dataModel.Agrifood/typsoil",
    "unitText": "https://smartdatamodels.org/dataModel.Agrifood/unitText",
    "url": "https://smartdatamodels.org/url",
    "user": "https://smartdatamodels.org/dataModel.Agrifood/user",
    "value": "ngsi-ld:hasValue",
    "vat": "https://smartdatamodels.org/dataModel.Agrifood/vat",
    "version": "https://smartdatamodels.org/dataModel.Agrifood/version",
    "veterinarian": "https://smartdatamodels.org/dataModel.Agrifood/veterinarian",
    "veterinarianTreatment": "https://smartdatamodels.org/dataModel.Agrifood/veterinarianTreatment",
    "waterConsumption": "https://smartdatamodels.org/dataModel.Agrifood/waterConsumption",
    "waterSource": "https://smartdatamodels.org/dataModel.Agrifood/waterSource",
    "weight": "https://smartdatamodels.org/dataModel.Agrifood/weight",
    "weightStDev": "https://smartdatamodels.org/dataModel.Agrifood/weightStDev",
    "welfareCondition": "https://smartdatamodels.org/dataModel.Agrifood/welfareCondition",
    "workOrder": "https://smartdatamodels.org/dataModel.Agrifood/workOrder",
    "workRecord": "https://smartdatamodels.org/dataModel.Agrifood/workRecord",
    "ngsi-ld": "https://uri.etsi.org/ngsi-ld/",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://opengeospatial.github.io/aim-swg/build/annotated/model/agriculture/external/smart-agrifood/crop/context.jsonld)


# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/opengeospatial/aim-swg](https://github.com/opengeospatial/aim-swg)
* Path: `_sources/external/smart-agrifood/crop`

