from atipcore.ext import ValidateRequest, API_SUCCESS
from . import scorer
from atipcore.ext import API_SUCCESS
from flask import Flask, jsonify, request
from .ml_model import predict_score
import numpy as np

def to_str(var):
    if type(var) is list:
        return str(var)[1:-1] # list
    if type(var) is np.ndarray:
        try:
            return str(list(var[0]))[1:-1] # numpy 1D array
        except TypeError:
            return str(list(var))[1:-1] # numpy sequence
    return str(var) # everything else

def create_app(app_config={}):

    from flask import Flask
    app = Flask('atipcore')

    for key, value in app_config.items():
        app.config[key] = value

    from atipcore.errorhandler import register_error_handlers
    register_error_handlers(app)

    @app.route('/', methods=('GET',))
    def health():
        return API_SUCCESS(payload={
            'desc': 'Evaluate an flower code based on an model flower code'
        })

    @app.route('/calculate-score', methods=('POST',))
    def calculate_score():
        inputData = request.get_json()
        outputData = predict_score(inputData['sepal_length'], inputData['sepal_width'], inputData['petal_length'], inputData['petal_width'])
        out = to_str(outputData[0])
        return API_SUCCESS(payload = {'flower_code' : out})

    return app
