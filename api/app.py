# -*- coding: utf-8 -*-

import json

from flask import Flask
from flask import request
from flask import Response
import requests

app = Flask(__name__)


@app.route('/', methods=['GET', 'OPTIONS'])
def enlarge_url():
    """Get large URL as received from GET request parameter."""
    url = request.args.get('url')

    if request.method == 'GET':
        if url:
            result = {
                'url': get_large_url(url)
            }
            # 200: Success
            response = Response(json.dumps(result), status=200,
                                mimetype='application/json')
            response.headers['Access-Control-Allow-Origin'] = '*'
            response.headers['Access-Control-Allow-Headers'] = 'content-type'
        else:
            result = {}

            # 400: Bad request
            response = Response(status=400, mimetype='application/json')
    elif request.method == 'OPTIONS':
        # 200: Success
        response = Response(status=200)
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Access-Control-Allow-Headers'] = 'content-type'
    else:
        # 405: Method not allowed
        response = Response(status=405)

    return response


def get_large_url(url):
    """Get large URL from Location header.

    Parameters:
    url -- URL to start requesting from.

    Return:
    Last URL as extracted from sequential Location header.
    """
    response = requests.head(add_http(url))

    while response.is_redirect:
        url = response.headers['location']
        response = requests.head(url)

    return url


def add_http(url):
    """Add "http://" at the beginning of the URL if no protocol was defined.

    Parameters:
    url -- URL to add the protocol to.

    Return:
    URL with given protocol or "http://".
    """
    if not '://' in url:
        return 'http://' + url
    return url


if __name__ == '__main__':
    app.run()
