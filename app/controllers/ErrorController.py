from flask import Blueprint, jsonify
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