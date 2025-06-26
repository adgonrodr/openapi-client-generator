- [Python OpenAPI Client Generator](#python-openapi-client-generator)
  - [Overview](#overview)
  - [Features](#features)
  - [About SQLDBM](#about-sqldbm)
  - [Project Structure](#project-structure)
  - [Requirements](#requirements)
  - [Build](#build)
  - [Usage](#usage)
  - [Customization](#customization)


# Python OpenAPI Client Generator
A utility for generating Python API clients and corresponding pytest tests from OpenAPI/Swagger specifications. This project streamlines the creation of typed client code and test suites by first extracting a rich manifest from an OpenAPI spec and then rendering code via Jinja2 templates.

## Overview

This project consists of two main components:
1. SwaggerManifestGenerator (openapi_generate_manifests.py):  
    - Loads an OpenAPI/Swagger specification (JSON or YAML) from a URL or local file.  
    - Walks through the API paths and operations to build a “rich” manifest (a JSON description of each endpoint, including parameters, request/response schemas, and security requirements).
    - Ouputs a manifest JSON file.
2. OpenAPIClientGenerator (openapi_client_generator_from_manifests.py):
    - Reads the generated manifest JSON.
    - Uses Jinja2 templates to render a Python API client module and corresponding pytest test files.
    - Strips extraneous blank lines and writes clean, ready-to-use code.

## Features
* Automated client generation: Create Python wrappers for any OpenAPI-defined API.
* Type inference: Converts OpenAPI schema types to Python type hints (int, float, str, bool, List[Any], Dict[str, Any]).
* Request/response handling: Renders request body and response schema handling in client methods.
* PyTest: Generates pytest-compatible test files for each endpoint to kickstart your test suite.
* Template-driven: Easily customize Jinja2 templates under templates/ to suit your coding style.

## About SQLDBM
This project integrates with SQLDBM by consuming its exported JSON schema file (sqldbm.json). SQLDBM is a cloud-based data modeling tool that allows you to design, document, and collaborate on your database schemas. By generating an API client around your SQLDBM-managed data models, you can programmatically interact with your database designs and metadata.

## Project Structure
```
openapi-client-generator/                           # Root directory
├── generated_manifests/                            # Output dir for manifest JSON files
├── openapi_client_generator                        # Main package
│   ├── templates/                                  # Jinja2 templates
│   │   ├── openapi_client_template.py.j2           # Client code template
│   │   └── openapi_client_test_template.py.j2      # Test code template
│   ├── __init__.py                                 # Package init
│   ├── openapi_client_generator_from_manifests.py  # Generates client & tests
│   └── openapi_generate_manifests.py               # Extracts manifest from spec
├── sqldbm.json                                     # SQLDBM export file (schema definition)
├── tests/                                          # Generated or handwritten pytest tests
├── .gitignore                                      # Git ignore rules
├── pyproject.toml                                  # Project metadata and dependencies
└── README.md                                       # This file
```

## Requirements
* Python 3.12+
* Poetry (for dependency management)

## Build
1. Clone the repository:
```bash
git clone https://github.com/your-org/openapi-client-generator.git
cd openapi-client-generator
```
2. Install dependencies using Poetry:
```bash
poetry install
```

## Usage

1. Generate a Manifest

```bash
# Extract a rich manifest from an OpenAPI/Swagger spec:
# This produces generated_manifests/myapi_manifest.json containing the endpoint definitions.

poetry run python openapi_client_generator/openapi_generate_manifests.py \
  --api-name Sqldbm \
  --swagger-url https://api.sqldbm.com/swagger/v1/swagger.json \
  [--output generated_manifests]
```

2. Generate Client & Tests

```bash
# Run the client generator against the manifest:
# Results:
#  myapi_api_client.py in myapi_api_client/
#  test_myapi_api_client.py in tests/

poetry run python openapi_client_generator/openapi_client_generator_from_manifests.py \
  --api-name Sqldbm \
  [--manifest generated_manifests/sqldbm_manifest.json] \
  [--client-output [sqldbm_api_client] \
  [--tests-output tests]
```

## Customization
* Templates: Modify templates/openapi_client_template.py.j2 and openapi_client_test_template.py.j2 to adjust generated code style.
* Naming: Pass --client-output and --tests-output to change directories, or use --client-suffix / --test-prefix in code.
