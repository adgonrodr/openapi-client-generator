import json
import argparse
import logging
import os.path

from jinja2 import Environment, FileSystemLoader, select_autoescape, StrictUndefined

OPENAPI_CLIENT_TEMPLATE = "openapi_client_template.py.j2"


def main():
    parser = argparse.ArgumentParser(description='Generate a Python API client from manifests')
    parser.add_argument('--manifest', '-m', type=str, required=True,
                        help='Path to the manifest JSON file')
    parser.add_argument('--output', '-o', type=str, default='target',
                        help='Path to the output client .py file')
    args = parser.parse_args()

    with open(args.manifest, 'r') as f:
        manifest = json.load(f)

    template_env = Environment(
        loader=FileSystemLoader(
            os.path.join(os.path.dirname(__file__), "templates")
        ),
        autoescape=select_autoescape(),
        undefined=StrictUndefined,
    )
    try:
        openapi_client_template = template_env.get_template(OPENAPI_CLIENT_TEMPLATE)
    except Exception as e:
        logging.error(f"{OPENAPI_CLIENT_TEMPLATE} not found", e)
        raise e

    if not os.path.exists(args.output):
        logging.info(f"Path {args.output} not found. Creating it.")
        os.mkdir(args.output)

    openapi_client_path = f"{args.output}/client.py"

    with open(openapi_client_path, "w") as f:
        logging.info(f"Templating OpenAPI client for {args.manifest} manifest")
        openapi_client_code = openapi_client_template.render(manifest=manifest)
        openapi_client_code_no_empty_lines = "\n".join(
            [line for line in openapi_client_code.splitlines() if line.strip()]
        )
        f.writelines(openapi_client_code_no_empty_lines)
        logging.debug(openapi_client_code_no_empty_lines)

    logging.info(f'Generated client code at {args.output}')


if __name__ == '__main__':
    main()
