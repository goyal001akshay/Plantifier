from flask import current_app
from werkzeug.exceptions import (MethodNotAllowed, NotFound)
from atipcore.ext import RESPONSE_CODE, API_ERROR, ValidationError


def handle_generic_error(e):
    if current_app.config.get('DEBUG', False) is True:
        raise e

    return API_ERROR(RESPONSE_CODE.UNKNOWN_ERROR, msg='Some unknown error occured.')


def register_error_handlers(app):
    app.register_error_handler(ValidationError, lambda e: API_ERROR(
        RESPONSE_CODE.BAD_REQUEST, e.message, e.error))
    app.register_error_handler(NotFound, lambda e: API_ERROR(
        404, 'Not found', status_code=404))
    app.register_error_handler(MethodNotAllowed, lambda e: API_ERROR(
        405, 'Method not allowed', status_code=405))

    app.register_error_handler(Exception, handle_generic_error)
