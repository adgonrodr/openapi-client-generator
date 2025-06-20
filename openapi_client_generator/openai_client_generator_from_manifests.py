#!/usr/bin/env python3
"""
Generate a Python API client (and pytest tests) from a manifest JSON file.
Refactored into a class-based structure: OpenAPIClientGenerator.
"""

import json
import argparse
import logging
import os
from jinja2 import Environment, FileSystemLoader, select_autoescape, StrictUndefined
from openapi_generate_manifests import SwaggerManifestGenerator

class OpenAPIClientGenerator:
    """
    Loads a manifest (list of endpoint definitions) and uses Jinja2 templates
    to generate:
      - client.py
      - pytest tests
    """

    CLIENT_TEMPLATE = "openapi_client_template.py.j2"
    TEST_TEMPLATE = "openapi_client_test_template.py.j2"
    CLIENT_SUFFIX = "_api_client"
    TEST_PREFIX = "test_"

    def __init__(self,
                 api_name: str,
                 manifest_path: str,
                 client_output_dir: str,
                 tests_output_dir: str,
                 templates_dir: str = None,
                 client_suffix: str = None,
                 test_prefix: str = None):
        """
        :param api_name: API name.
        :param manifest_path: Path to the manifest JSON file.
        :param client_output_dir: Directory to write generated client.py.
        :param tests_output_dir: Directory to write generated test files.
        :param templates_dir: Directory containing Jinja2 templates.
                              If None, assumes templates/ next to this script.
        :param client_suffix: Suffix of generated files.
                              If None, defaults self.CLIENT_SUFFIX
        :param test_prefix: Suffix of generated files.
                              If None, defaults self.TEST_PREFIX
        """
        self.api_name = api_name
        self.manifest_path = manifest_path
        self.client_output_dir = client_output_dir
        self.tests_output_dir = tests_output_dir
        self.templates_dir = templates_dir or os.path.join(os.path.dirname(__file__), "templates")
        self.client_suffix = client_suffix or self.CLIENT_SUFFIX
        self.test_prefix = test_prefix or self.TEST_PREFIX
        self.manifest = []
        self.env = None
        self.client_template = None
        self.test_template = None

    def run(self) -> None:
        """
        Main entry point: load manifest, set up Jinja, generate client and tests.
        """
        self._load_manifest()
        self._prepare_environment()
        self._ensure_output_dirs()
        self._render_client()
        self._render_tests()
        print(f"✅ Generated client in '{self.client_output_dir}' and tests in '{self.tests_output_dir}'")

    def _load_manifest(self) -> None:
        """
        Read the manifest JSON into self.manifest.
        """
        with open(self.manifest_path, "r") as f:
            self.manifest = json.load(f)

    def _prepare_environment(self) -> None:
        """
        Configure the Jinja2 Environment (including the 'do' extension) and load both templates.
        """
        self.env = Environment(
            loader=FileSystemLoader(self.templates_dir),
            autoescape=select_autoescape(),
            undefined=StrictUndefined,
            extensions=["jinja2.ext.do"]  # ENABLE the 'do' tag
        )

        try:
            self.client_template = self.env.get_template(self.CLIENT_TEMPLATE)
        except Exception as e:
            logging.error(f"Client template '{self.CLIENT_TEMPLATE}' not found in '{self.templates_dir}': {e}")
            raise

        try:
            self.test_template = self.env.get_template(self.TEST_TEMPLATE)
        except Exception as e:
            logging.error(f"Test template '{self.TEST_TEMPLATE}' not found in '{self.templates_dir}': {e}")
            raise

    def _ensure_output_dirs(self) -> None:
        """
        Ensure that both output directories exist.
        """
        os.makedirs(self.client_output_dir, exist_ok=True)
        os.makedirs(self.tests_output_dir, exist_ok=True)

    def _render_client(self) -> None:
        """
        Render client.py from the CLIENT_TEMPLATE and self.manifest.
        """
        client_py_path = os.path.join(
            self.client_output_dir,
            f"{self.api_name.lower()}{self.client_suffix}.py"
        )
        rendered = self.client_template.render(
            api_name=self.api_name,
            manifest=self.manifest
        )
        # Strip out purely blank lines
        cleaned = "\n".join(line for line in rendered.splitlines() if line.strip())
        with open(client_py_path, "w") as f:
            f.write(cleaned)

    def _render_tests(self) -> None:
        """
        Render pytest tests from the TEST_TEMPLATE and self.manifest.
        """
        test_file_name = f"{self.test_prefix}{self.api_name.lower()}{self.client_suffix}.py"
        test_py_path = os.path.join(self.tests_output_dir, test_file_name)
        rendered = self.test_template.render(
            api_name=self.api_name,
            manifest=self.manifest
        )
        cleaned = "\n".join(line for line in rendered.splitlines() if line.strip())
        with open(test_py_path, "w") as f:
            f.write(cleaned)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    parser = argparse.ArgumentParser(
        description="Generate Python API client + pytest tests from a manifest JSON"
    )
    parser.add_argument(
        "--api-name", "-n",
        type=str,
        required=True,
        help="API name"
    )
    parser.add_argument(
        "--manifest", "-m",
        type=str,
        required=False,
        default=None,
        help="Path to the manifest JSON file"
    )
    parser.add_argument(
        "--client-output", "-o",
        type=str,
        default=None,
        help="Directory to write generated client.py (default: './<api_name>')"
    )
    parser.add_argument(
        "--tests-output",
        type=str,
        default="tests",
        help="Directory to write generated pytest files (default: './tests')"
    )
    parser.add_argument(
        "--templates", "-t",
        type=str,
        default=None,
        help="Path to directory containing Jinja2 templates (default: './templates')"
    )
    args = parser.parse_args()

    # Determine default client output if not supplied
    client_output = args.client_output or f"{args.api_name.lower()}{OpenAPIClientGenerator.CLIENT_SUFFIX}"
    manifest = args.manifest or f"generated_manifests/{args.api_name.lower()}{SwaggerManifestGenerator.MANIFEST_SUFFIX}"

    if os.path.exists(manifest):
        logging.info(f"Processing manifest {manifest} to build {args.api_name} API Client")
    else:
        msg = f"Error generating {args.api_name} API Client. {manifest} manifest not found."
        logging.error(msg)
        exit(1)

    generator = OpenAPIClientGenerator(
        api_name=args.api_name,
        manifest_path=manifest,
        client_output_dir=client_output,
        tests_output_dir=args.tests_output,
        templates_dir=args.templates
    )
    generator.run()
