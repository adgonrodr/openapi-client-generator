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


class OpenAPIClientGenerator:
    """
    Loads a manifest (list of endpoint definitions) and uses Jinja2 templates
    to generate:
      - client.py
      - tests/test_client.py
    """

    CLIENT_TEMPLATE = "openapi_client_template.py.j2"
    TEST_TEMPLATE = "openapi_client_test_template.py.j2"

    def __init__(self, api_name: str, manifest_path: str, output_dir: str, templates_dir: str = None):
        """
        :param api_name: API name.
        :param manifest_path: Path to the manifest JSON file.
        :param output_dir: Directory to write generated files (client.py, tests/).
        :param templates_dir: Directory containing Jinja2 templates.
                              If None, assumes templates/ next to this script.
        """
        self.api_name = api_name
        self.manifest_path = manifest_path
        self.output_dir = output_dir
        self.templates_dir = templates_dir or os.path.join(os.path.dirname(__file__), "templates")
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
        print(f"✅ Generated client and tests in '{self.output_dir}'")

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
        Ensure that the output directory and its tests/ subdirectory exist.
        """
        if not os.path.isdir(self.output_dir):
            os.makedirs(self.output_dir, exist_ok=True)

    def _render_client(self) -> None:
        """
        Render client.py from the CLIENT_TEMPLATE and self.manifest.
        """
        client_py_path = os.path.join(self.output_dir, f"{self.api_name.lower()}_api_client.py")
        rendered = self.client_template.render(api_name=self.api_name, manifest=self.manifest)
        # Strip out purely blank lines
        cleaned = "\n".join(line for line in rendered.splitlines() if line.strip())
        with open(client_py_path, "w") as f:
            f.write(cleaned)

    def _render_tests(self) -> None:
        """
        Render tests/test_client.py from the TEST_TEMPLATE and self.manifest.
        """
        test_py_path = os.path.join(self.output_dir, f"test_{self.api_name.lower()}_api_client.py")
        rendered = self.test_template.render(api_name=self.api_name, manifest=self.manifest)
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
        required=True,
        help="Path to the manifest JSON file"
    )
    parser.add_argument(
        "--output", "-o",
        type=str,
        default="target",
        help="Directory to write generated client.py and tests/ (default: ./target_client)"
    )
    parser.add_argument(
        "--templates", "-t",
        type=str,
        default=None,
        help="Path to directory containing Jinja2 templates (default: ./templates next to this script)"
    )
    args = parser.parse_args()

    generator = OpenAPIClientGenerator(
        api_name=args.api_name,
        manifest_path=args.manifest,
        output_dir=args.output,
        templates_dir=args.templates
    )
    generator.run()
