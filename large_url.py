# -*- coding: utf-8 -*-

import json

from flask import Flask
from flask import request
from flask import Response
import requests

app = Flask(__name__)


@app.route('/', methods=['GET'])
def enlarge_url():
    """Get large URL as received from GET request parameter."""
    url = request.args.get('url')

    if url:
        result = {
            'url': get_large_url(url)
        }
        return Response(json.dumps(result), status=200,
                        mimetype='application/json')
    else:
        result = {}
        return Response(status=400, mimetype='application/json')


def get_large_url(url):
    """Get large URL from Location header.

    Parameters:
    url -- URL to start requesting from.

    Return:
    Last URL as extracted from sequential Location header.
    """
    response = requests.head(url)

    while response.is_redirect:
        url = response.headers['location']
        response = requests.head(url)

    return url


if __name__ == '__main__':
    app.run()
