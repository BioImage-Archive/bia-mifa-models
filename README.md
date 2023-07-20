# BioImage Archive FAIM metadata models

This repository contains schemas and models for working with the BioImage Archive's FAIM (Formats, Accessibility, Incentives and Metadata) metadata implementation. This metadata model is intended to promote the reusability of AI-ready biological image datasets and it is based on the community recommendations  summarised [here](https://zenodo.org/record/7681687).

The FAIM metadata model provides classes to work with the metadata related to the dataset annotations, version, and general study information. For the biological images metadata, the BioImage Archive follows the REMBI (Recommended Metadata for Biological Images) model. You can find the models and tools for working with the BioImage Archive's REMBI implementation here:
[https://github.com/BioImage-Archive/bia-rembi-models](https://github.com/BioImage-Archive/bia-rembi-models)

You can browse the FAIM metadata model here:
[https://BioImage-Archive.github.io/bia-faim-models](https://BioImage-Archive.github.io/bia-faim-models)

## Repository contents

The main source of truth is [bia_faim_models.yaml](src/bia_faim_models/schema/bia_faim_models.yaml), a relatively simple to edit YAML file created with [LinkML](https://github.com/linkml).

The yaml definition is used to derive the following files:
  - [Excel](project/excel/bia_faim_models.xlsx)
  - [GraphQL](project/graphql/bia_faim_models.graphql)
  - [JSON-LD context](project/jsonld/bia_faim_models.context.jsonld)
  - [JSON Schema](project/jsonschema/bia_faim_models.schema.json)
  - [OWL](project/owl/bia_faim_models.owl.ttl)
  - [Python dataclasses](project/bia_faim_models.py)
  - [Prefix map](project/prefixmap/bia_faim_models.yaml)
  - [ProtoBuf definitions](project/protobuf/bia_faim_models.proto)
  - [SHACL](project/shacl/bia_faim_models.shacl.ttl)
  - [RDF Shape Expressions](project/shex/bia_faim_models.shex)
  - [SQL schema](project/sqlschema/bia_faim_models.sql)

## Repository structure

* [examples/](examples/) - example data from real BioImage Archive submissions
* [project/](project/) - project files, including all artefacts derived from the yaml definition (do not edit these)
* [src/](src/) - source files (edit these)
  * [bia_faim_models](src/bia_faim_models)
    * [schema](src/bia_faim_models/schema) -- LinkML schema - yaml definition
      (edit this)
    * [datamodel](src/bia_faim_models/datamodel) -- generated
      Python datamodel
* [tests/](tests/) - Python tests

## Developer Documentation

Prerequisites: Python 3.7+ and poetry

<details>
Use the `make` command to generate project artefacts:

* `make all`: make everything
* `make deploy`: deploys site
</details>

