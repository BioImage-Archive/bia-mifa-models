[![DOI](https://zenodo.org/badge/655723200.svg)](https://zenodo.org/badge/latestdoi/655723200)

# BioImage Archive MIFA metadata models

This repository contains schemas and models for working with the BioImage Archive's MIFA (Metadata, Incentives, Formats and Accessibility) metadata implementation. This metadata model is intended to promote the reusability of AI-ready biological image datasets and it is based on the community recommendations  summarised [here](https://arxiv.org/abs/2311.10443).

The MIFA metadata model provides classes to work with the metadata related to the dataset annotations, version, and general study information. For the biological images metadata, the BioImage Archive follows the REMBI (Recommended Metadata for Biological Images) model. You can find the models and tools for working with the BioImage Archive's REMBI implementation here:
[https://github.com/BioImage-Archive/bia-rembi-models](https://github.com/BioImage-Archive/bia-rembi-models)

You can browse the MIFA metadata model here:
[https://BioImage-Archive.github.io/bia-mifa-models](https://BioImage-Archive.github.io/bia-mifa-models)

## Repository contents

The main source of truth is [bia_mifa_models.yaml](src/bia_mifa_models/schema/bia_mifa_models.yaml), a relatively simple to edit YAML file created with [LinkML](https://github.com/linkml).

The yaml definition is used to derive the following files:
  - [Excel](project/excel/bia_mifa_models.xlsx)
  - [GraphQL](project/graphql/bia_mifa_models.graphql)
  - [JSON-LD context](project/jsonld/bia_mifa_models.context.jsonld)
  - [JSON Schema](project/jsonschema/bia_mifa_models.schema.json)
  - [OWL](project/owl/bia_mifa_models.owl.ttl)
  - [Python dataclasses](project/bia_mifa_models.py)
  - [Prefix map](project/prefixmap/bia_mifa_models.yaml)
  - [ProtoBuf definitions](project/protobuf/bia_mifa_models.proto)
  - [SHACL](project/shacl/bia_mifa_models.shacl.ttl)
  - [RDF Shape Expressions](project/shex/bia_mifa_models.shex)
  - [SQL schema](project/sqlschema/bia_mifa_models.sql)

## Repository structure

* [examples/](examples/) - example data from real BioImage Archive submissions
* [project/](project/) - project files, including all artefacts derived from the yaml definition (do not edit these)
* [src/](src/) - source files (edit these)
  * [bia_mifa_models](src/bia_mifa_models)
    * [schema](src/bia_mifa_models/schema) -- LinkML schema - yaml definition
      (edit this)
    * [datamodel](src/bia_mifa_models/datamodel) -- generated
      Python datamodel
    * [pydantic_model](src/bia_mifa_models/pydantic_model) -- generated
      Pydantic datamodel
* [tests/](tests/) - Python tests

## Developer Documentation

Prerequisites: Python 3.7+ and poetry

<details>
Use the `make` command to generate project artefacts:

* `make all`: make everything
* `make deploy`: deploys site
</details>

