#!/usr/bin/env python3

import os

import connexion

from swagger_server import encoder


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    spec_dir = os.path.join(here, "swagger")  # absolute path to swagger_server/swagger
    app = connexion.App(__name__, specification_dir=spec_dir)
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api(
        'swagger.yaml',
        arguments={'title': 'Simple Inventory API'},
        pythonic_params=True
    )
    app.run(port=8080)


if __name__ == '__main__':
    main()
