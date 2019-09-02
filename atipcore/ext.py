from flask import jsonify, request


class RESPONSE_CODE:
    SUCCESS = 2000
    BAD_REQUEST = 4000
    UNKNOWN_ERROR = 4010


def API_SUCCESS(msg="Success", payload=None):
    response = {
        'status': RESPONSE_CODE.SUCCESS,
        'message': msg
    }
    if payload is not None:
        response['payload'] = payload

    return jsonify(response)


def API_ERROR(error_code, msg, error=None, status_code=200):
    response = {
        'status': error_code,
        'message': msg
    }
    if error is not None:
        response['errors'] = error

    response_json = jsonify(response)
    response_json.status_code = status_code
    return response_json


class ValidationError(Exception):
    def __init__(self, error=None, message='Invalid input received.'):
        self.error = error
        self.message = message


def ValidateRequest(schema):
    def decorator(func):
        def decorated_function(*args, **kwargs):
            validation_result = schema.validate(request.json)
            if validation_result.get('success', False) is False:
                raise ValidationError(validation_result.get('error'))

            request.validated_json = validation_result.get('data')
            return func(*args, **kwargs)
        return decorated_function
    return decorator
