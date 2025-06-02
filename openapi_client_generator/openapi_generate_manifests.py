"""
Fetches an OpenAPI/Swagger spec and extracts endpoint manifests.
"""
import requests
import json
import argparse
import logging
import yaml
import os
import re


def load_swagger(url: str) -> dict:
    """
    Load and parse a Swagger/OpenAPI spec from a URL.
    """
    resp = requests.get(url)
    resp.raise_for_status()
    ct = resp.headers.get('content-type', '')
    if url.endswith('.yaml') or 'yaml' in ct:
        import yaml
        return yaml.safe_load(resp.text)
    return resp.json()


def sanitize_op_name(name: str) -> str:
    """
    Convert camelCase or PascalCase to snake_case.
    """
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    s2 = re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1)
    return s2.replace('-', '_').lower()


def sanitize_path(path: str) -> str:
    return path.strip('/').replace('/', '_').replace('{', '').replace('}', '')


def infer_type(schema: dict) -> str:
    t = schema.get('type') if schema else None
    if t == 'integer': return 'int'
    if t == 'number': return 'float'
    if t == 'string': return 'str'
    if t == 'boolean': return 'bool'
    if t == 'array': return 'List[Any]'
    if t == 'object': return 'Dict[str, Any]'
    return 'Any'


def extract_manifests(spec: dict) -> list:
    manifests = []
    for path, path_item in spec.get('paths', {}).items():
        for method, op in path_item.items():
            if method.lower() not in ['get','post','put','patch','delete','options','head']:
                continue
            operation_id = op.get('operationId') or f"{method.lower()}_{sanitize_path(path)}"
            python_op = sanitize_op_name(operation_id)
            summary = op.get('summary','')
            params = []
            for p in op.get('parameters', []):
                schema = p.get('schema', {})
                p_type = infer_type(schema)
                required = p.get('required', False)
                default = schema.get('default', None)
                default_repr = repr(default) if default is not None else None
                original = p['name']
                python_name = sanitize_op_name(original)
                params.append({
                    'name': original,
                    'python_name': python_name,
                    'in': p['in'],
                    'description': p.get('description',''),
                    'py_type': p_type,
                    'required': required,
                    'default_repr': default_repr
                })
            has_body = 'requestBody' in op
            manifests.append({
                'operationId': python_op,
                'path': path,
                'method': method.upper(),
                'summary': summary,
                'parameters': params,
                'requestBody': has_body
            })
    return manifests


def main():
    parser = argparse.ArgumentParser(description='Generate manifests from Swagger URL')
    parser.add_argument('--swagger-url', '-s', type=str, required=True,
                        help='URL to the Swagger/OpenAPI spec (JSON or YAML)')
    parser.add_argument('--output', '-o', type=str, default="target",
                        help='Path to output JSON manifest file')
    args = parser.parse_args()

    spec = load_swagger(args.swagger_url)
    manifests = extract_manifests(spec)

    if not os.path.exists(args.output):
        logging.info(f"Path {args.output} not found. Creating it.")
        os.mkdir(args.output)

    openapi_client_path = f"{args.output}/manifest.json"

    with open(openapi_client_path, 'w') as f:
        json.dump(manifests, f, indent=2)

    logging.info(f'Generated {len(manifests)} manifests and saved to {args.output}')


if __name__ == '__main__':
    main()
