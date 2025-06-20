#!/usr/bin/env python3
"""
Fetches an OpenAPI/Swagger spec (JSON or YAML) and extracts a “rich” manifest,
organized as a class rather than standalone functions.
"""

import requests
import json
import argparse
import logging
import yaml
import os
import re


class SwaggerManifestGenerator:
    """
    Encapsulates all logic required to:
      1. Load an OpenAPI/Swagger spec (from a URL or local file),
      2. Walk through its paths/operations and build a “rich” manifest entry
         for each endpoint (parameters + enums + requestBody schema + responses),
      3. Save the resulting manifest JSON to disk.
    """

    def __init__(self, source: str, output_dir: str):
        """
        :param source: URL or local file path of the OpenAPI/Swagger spec (JSON or YAML)
        :param output_dir: Directory where `manifest.json` will be written
        """
        self.source = source
        self.output_dir = output_dir
        self.spec = None  # Will hold the loaded OpenAPI spec (dict)
        self.manifest = []  # Will hold the list of extracted manifest entries

    # --------------------------------------------------------------------------
    # Public API
    # --------------------------------------------------------------------------
    def run(self) -> None:
        """
        Entry point: load the spec, extract the manifest, and write it to disk.
        """
        self.spec = self._load_spec(self.source)
        self.manifest = self._extract_manifests()
        self._ensure_output_dir()
        self._write_manifest()

        print(f"✅ Generated {len(self.manifest)} manifest entries → "
              f"{os.path.join(self.output_dir, 'manifest.json')}")

    # --------------------------------------------------------------------------
    # Step 1: Load the OpenAPI spec (JSON or YAML) from URL or file
    # --------------------------------------------------------------------------
    def _load_spec(self, source: str) -> dict:
        """
        Load and parse a Swagger/OpenAPI spec from a URL or local file path.

        :param source: either a URL (starting with http:// or https://) or a local path
        :return: parsed spec as a Python dict
        """
        if source.startswith(("http://", "https://")):
            response = requests.get(source)
            response.raise_for_status()
            content_type = response.headers.get("content-type", "").lower()
            text = response.text
            if source.lower().endswith((".yaml", ".yml")) or "yaml" in content_type:
                return yaml.safe_load(text)
            else:
                return response.json()
        else:
            # Treat source as a local file path
            with open(source, "r") as f:
                text = f.read()
                if source.lower().endswith((".yaml", ".yml")):
                    return yaml.safe_load(text)
                else:
                    return json.loads(text)

    # --------------------------------------------------------------------------
    # Step 2: Extract “rich” manifest entries for every path + method
    # --------------------------------------------------------------------------
    def _extract_manifests(self) -> list:
        """
        Walk through self.spec["paths"] and, for each HTTP operation,
        build a manifest entry that includes:
          - operationId (snake_case)
          - path, method, summary
          - parameters (with schema + enum + type + location)
          - requestBody (mediaType + schema), if any
          - responses["200"] (mediaType + schema), if any
          - security requirements (e.g. bearer)
        """
        manifests = []
        components = self.spec.get("components", {})

        for path, path_item in self.spec.get("paths", {}).items():
            for http_method, op in path_item.items():
                if http_method.lower() not in ["get", "post", "put", "patch", "delete", "options", "head"]:
                    continue

                # 1. operationId (use user‐provided if present, otherwise derive one)
                raw_op_id = op.get("operationId") or f"{http_method.lower()}_{self._sanitize_path(path)}"
                operation_id = self._sanitize_op_name(raw_op_id)

                # 2. Basic metadata
                summary = op.get("summary", "")
                method = http_method.upper()

                # 3. Extract parameters
                parameters = []
                for p in op.get("parameters", []):
                    parameters.append(self._build_param_entry(p))

                # 4. Extract requestBody (if present)
                request_body = None
                if "requestBody" in op:
                    request_body = self._build_request_body_entry(op["requestBody"])

                # 5. Extract responses["200"] (if present)
                responses = {}
                if "responses" in op and "200" in op["responses"]:
                    responses = self._build_response_entry(op["responses"]["200"])

                # 6. Extract security (only checking for “bearer” here)
                security = []
                if "security" in op:
                    for sec_item in op["security"]:
                        for scheme_name in sec_item.keys():
                            sc = components.get("securitySchemes", {}).get(scheme_name)
                            if sc and sc.get("type") == "http" and sc.get("scheme") == "bearer":
                                security.append({"scheme": "bearer", "name": "Authorization"})

                manifests.append({
                    "operationId": operation_id,
                    "path": path,
                    "method": method,
                    "summary": summary,
                    "parameters": parameters,
                    "requestBody": request_body,
                    "responses": responses,
                    "security": security
                })

        return manifests

    # --------------------------------------------------------------------------
    # Step 3: Write manifest out to filesystem
    # --------------------------------------------------------------------------
    def _ensure_output_dir(self) -> None:
        """
        Create self.output_dir if it doesn’t already exist.
        """
        if not os.path.isdir(self.output_dir):
            os.makedirs(self.output_dir, exist_ok=True)

    def _write_manifest(self) -> None:
        """
        Dump self.manifest (a list of dicts) as JSON into `<output_dir>/manifest.json`.
        """
        path = os.path.join(self.output_dir, "manifest.json")
        with open(path, "w") as f:
            json.dump(self.manifest, f, indent=2)

    # --------------------------------------------------------------------------
    # Helper routines for “extract_manifests”
    # --------------------------------------------------------------------------
    def _build_param_entry(self, p: dict) -> dict:
        """
        Given one parameter object `p` from the OpenAPI spec, return a dictionary:
          {
            name: <original name>,
            python_name: <snake_case>,
            in: <"path" or "query" or "header">,
            description: <p.get("description","")>,
            schema: <fully resolved schema dict>,
            py_type: <inferred Python type>,
            required: <True/False>,
            default_repr: <repr(default)> or None,
            enum: <list of allowed values> or None,
          }
        """
        pname = p["name"]
        location = p["in"]  # "path" / "query" / "header"
        required = p.get("required", False)

        raw_schema = p.get("schema", {})
        schema_obj = self._resolve_ref_if_needed(raw_schema)

        ptype = self._infer_type(schema_obj)
        default = schema_obj.get("default", None)
        default_repr = repr(default) if default is not None else None
        python_name = self._sanitize_op_name(pname)

        enum_vals = schema_obj.get("enum", None)

        return {
            "name": pname,
            "python_name": python_name,
            "in": location,
            "description": p.get("description", ""),
            "schema": schema_obj,
            "py_type": ptype,
            "required": required,
            "default_repr": default_repr,
            "enum": enum_vals
        }

    def _build_request_body_entry(self, rb: dict) -> dict:
        """
        Given op["requestBody"], return:
          {
            mediaType: <e.g. "application/json">,
            schema: <resolved schema dict>
          }
        """
        content = rb.get("content", {})
        if not content:
            return None

        # Prefer "application/json" if present, otherwise take the first mediaType
        if "application/json" in content:
            media_type = "application/json"
        else:
            media_type = next(iter(content.keys()))

        schema_obj = content[media_type].get("schema", {})
        schema_obj = self._resolve_ref_if_needed(schema_obj)

        return {
            "mediaType": media_type,
            "schema": schema_obj
        }

    def _build_response_entry(self, resp200: dict) -> dict:
        """
        Given op["responses"]["200"], return:
          {
            "200": {
              mediaType: <first mediaType or "application/json">,
              schema: <resolved schema dict>
            }
          }
        """
        content = resp200.get("content", {})
        if not content:
            return {}

        # Prefer "application/json" if present, otherwise take the first mediaType key
        if "application/json" in content:
            media_type = "application/json"
        else:
            media_type = next(iter(content.keys()))

        schema_obj = content[media_type].get("schema", {})
        schema_obj = self._resolve_ref_if_needed(schema_obj)

        return {
            "200": {
                "mediaType": media_type,
                "schema": schema_obj
            }
        }

    # --------------------------------------------------------------------------
    # Utility methods
    # --------------------------------------------------------------------------
    def _resolve_ref_if_needed(self, schema_obj: dict) -> dict:
        """
        If schema_obj contains a "$ref", follow it within self.spec and return the
        resolved schema. Otherwise, return schema_obj as‐is.
        """
        if "$ref" in schema_obj:
            return self._resolve_ref(schema_obj["$ref"])
        else:
            return schema_obj

    def _resolve_ref(self, ref: str) -> dict:
        """
        Resolve a JSON Reference of the form "#/components/schemas/SomeSchema" by
        walking self.spec.  Raise KeyError if it cannot be found.
        """
        if not ref.startswith("#/"):
            raise ValueError(f"Only local references are supported: {ref}")

        parts = ref.lstrip("#/").split("/")
        node = self.spec
        for part in parts:
            node = node.get(part)
            if node is None:
                raise KeyError(f"Reference {ref} not found in spec")
        return node

    def _infer_type(self, schema: dict) -> str:
        """
        Map OpenAPI primitive types to basic Python type hints:
          integer → int
          number  → float
          string  → str
          boolean → bool
          array   → List[Any]
          object  → Dict[str, Any]
          (default) → Any
        """
        t = schema.get("type")
        if t == "integer":
            return "int"
        if t == "number":
            return "float"
        if t == "string":
            return "str"
        if t == "boolean":
            return "bool"
        if t == "array":
            return "List[Any]"
        if t == "object":
            return "Dict[str, Any]"
        return "Any"

    def _sanitize_op_name(self, name: str) -> str:
        """
        Convert a CamelCase or kebab‐case operationId to snake_case.
        e.g. "GetProjects" or "get-projects" → "get_projects"
        """
        # First: camelCase / PascalCase → snake
        s1 = re.sub(r"(.)([A-Z][a-z]+)", r"\1_\2", name)
        s2 = re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", s1)
        # Then: replace hyphens with underscores
        return s2.replace("-", "_").lower()

    def _sanitize_path(self, path: str) -> str:
        """
        Convert a URL path like "/foo/{bar}/baz" → "foo_bar_baz"
        so it can be appended to the HTTP method to form a fallback operationId.
        """
        return path.strip("/").replace("/", "_").replace("{", "").replace("}", "")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    parser = argparse.ArgumentParser(
        description="Generate a 'rich' manifest JSON from a Swagger/OpenAPI URL or file"
    )
    parser.add_argument(
        "--swagger-url", "-s",
        type=str,
        required=True,
        help="URL or local path to the Swagger/OpenAPI spec (JSON or YAML)"
    )
    parser.add_argument(
        "--output", "-o",
        type=str,
        default="target",
        help="Directory to write `manifest.json` (default: ./target)"
    )
    args = parser.parse_args()

    generator = SwaggerManifestGenerator(source=args.swagger_url, output_dir=args.output)
    generator.run()