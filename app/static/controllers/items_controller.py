from ..constants import MICROSERVICE_URL
from flask import Blueprint, abort, jsonify, request
from google.appengine.api import urlfetch
from requests.exceptions import *
from werkzeug.exceptions import *
import logging
import requests


items = Blueprint('items', __name__)
urlfetch.set_default_fetch_deadline(30)


@items.route('/', methods=['POST'])
def post_data():
    try:
        c_request = request.form
        c_request = c_request if c_request else request.get_json()
        m_request = requests.post('{}/{}/'.format(
            MICROSERVICE_URL,
            'items'
        ), json=c_request)
        m_request.raise_for_status()
        m_response = m_request.json()

        return jsonify(m_response)
    
    except HTTPException as e:
        logging.error("Client to middleware error.")
        logging.error(str(e))
        abort(
            e.response.status_code if e.response else
            400
        )
    
    except RequestException as e:
        logging.error("Middleware to microservice error.")
        logging.error(str(e))
        abort(
            e.response.status_code if isinstance(e, HTTPError) else
            404 if isinstance(e, URLRequired) else
            504 if all(isinstance(e, error) for error in [TooManyRedirects,
                                                          Timeout]) else
            500
        )

    except Exception as e:
        logging.error("Middleware error.")
        abort(500)


@items.route('/', methods=['GET'])
def get_data():
    try:
        c_request = request.args
        m_request = requests.get('{}/{}/'.format(
            MICROSERVICE_URL,
            'items'
        ), params=c_request)
        m_request.raise_for_status()
        m_response = m_request.json()

        return jsonify(m_response)

    except HTTPException as e:
        logging.error("Client to middleware error.")
        logging.error(str(e))
        abort(
            e.response.status_code if e.response else
            400
        )
    
    except RequestException as e:
        logging.error("Middleware to microservice error.")
        logging.error(str(e))
        abort(
            e.response.status_code if isinstance(e, HTTPError) else
            404 if isinstance(e, URLRequired) else
            504 if all(isinstance(e, error) for error in [TooManyRedirects,
                                                          Timeout]) else
            500
        )

    except Exception as e:
        logging.error("Middleware error.")
        logging.error(str(e))
        abort(500)


@items.route('/<int:id>', methods=['GET'])
def get_data_by_id(id):
    try:
        c_request = request.args
        m_request = requests.get('{}/{}/{}'.format(
            MICROSERVICE_URL,
            'items',
            str(id)
        ), params=c_request)
        m_request.raise_for_status()
        m_response = m_request.json()

        return jsonify(m_response)

    except HTTPException as e:
        logging.error("Client to middleware error.")
        logging.error(str(e))
        abort(
            e.response.status_code if e.response else
            400
        )
    
    except RequestException as e:
        logging.error("Middleware to microservice error.")
        logging.error(str(e))
        abort(
            e.response.status_code if isinstance(e, HTTPError) else
            404 if isinstance(e, URLRequired) else
            504 if all(isinstance(e, error) for error in [TooManyRedirects,
                                                          Timeout]) else
            500
        )

    except Exception as e:
        logging.error("Middleware error.")
        abort(500)


@items.route('/<int:id>', methods=['PUT'])
def put_data(id):
    try:
        c_request = request.form
        c_request = c_request if c_request else request.get_json()
        m_request = requests.put('{}/{}/{}'.format(
            MICROSERVICE_URL,
            'items',
            str(id)
        ), json=c_request)
        m_request.raise_for_status()
        m_response = m_request.json()

        return jsonify(m_response)

    except HTTPException as e:
        logging.error("Client to middleware error.")
        logging.error(str(e))
        abort(
            e.response.status_code if e.response else
            400
        )
    
    except RequestException as e:
        logging.error("Middleware to microservice error.")
        logging.error(str(e))
        abort(
            e.response.status_code if isinstance(e, HTTPError) else
            404 if isinstance(e, URLRequired) else
            504 if all(isinstance(e, error) for error in [TooManyRedirects,
                                                          Timeout]) else
            500
        )

    except Exception as e:
        logging.error("Middleware error.")
        abort(500)


@items.route('/<int:id>', methods=['DELETE'])
def delete_data(id):
    try:
        m_request = requests.delete('{}/{}/{}'.format(
            MICROSERVICE_URL,
            'items',
            str(id)
        ))
        m_request.raise_for_status()
        m_response = m_request.json()

        return jsonify(m_response)
    
    except HTTPException as e:
        logging.error("Client to middleware error.")
        logging.error(str(e))
        abort(
            e.response.status_code if e.response else
            400
        )
    
    except RequestException as e:
        logging.error("Middleware to microservice error.")
        logging.error(str(e))
        abort(
            e.response.status_code if isinstance(e, HTTPError) else
            404 if isinstance(e, URLRequired) else
            504 if all(isinstance(e, error) for error in [TooManyRedirects,
                                                          Timeout]) else
            500
        )

    except Exception as e:
        logging.error("Middleware error.")
        abort(500)