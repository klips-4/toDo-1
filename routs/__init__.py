from flask import request
from app import app
from flask_cors import cross_origin

from classes.EndpointFactory import EndpointFactory


@cross_origin()
@app.route('/service', methods=['POST'])
def main_route():
    request_data = request.get_json() or {}
    return EndpointFactory(request_data).process()
