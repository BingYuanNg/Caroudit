from flask import Blueprint, jsonify, request
from app.resources.utils import CustomError


errors = Blueprint('errors', __name__)

@errors.app_errorhandler(CustomError)
def custom_error(error):
    status = 'error'
    output = {
        'status': status,
        'message': error.message
    }

    return jsonify(output)

@errors.app_errorhandler(404)
def not_found(error=None):
    message = {
        'status': 404,
        'message': request.url + ' not found.',
    }
    resp = jsonify(message)
    resp.status_code = 404

    return resp
