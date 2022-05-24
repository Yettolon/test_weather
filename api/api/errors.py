import logging

from flask import jsonify


def bad_request(message):
    response = jsonify({"status": 400, "message": message})
    response.status_code = 400
    logging.error(message)
    return response
