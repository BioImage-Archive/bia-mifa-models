# bia-faim-models

Schemas and models for working with the BioImage Archive's FAIM (Formats, Accessibility, Incentives and Metadata) metadata implementation

## Website

[https://BioImage-Archive.github.io/bia-faim-models](https://BioImage-Archive.github.io/bia-faim-models)

## Repository Structure

* [examples/](examples/) - example data
* [project/](project/) - project files (do not edit these)
* [src/](src/) - source files (edit these)
  * [bia_faim_models](src/bia_faim_models)
    * [schema](src/bia_faim_models/schema) -- LinkML schema
      (edit this)
    * [datamodel](src/bia_faim_models/datamodel) -- generated
      Python datamodel
* [tests/](tests/) - Python tests

## Developer Documentation

<details>
Use the `make` command to generate project artefacts:

* `make all`: make everything
* `make deploy`: deploys site
</details>

## Credits

This project was made with
[linkml-project-cookiecutter](https://github.com/linkml/linkml-project-cookiecutter).
