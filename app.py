import requests
from flask import Flask, jsonify
from os import environ
from model.model import ModelSchema
from exceptions.custom_exceptions import MissingModelException

app = Flask(__name__)


@app.get("/")
def root():
    return "Please, inform model username in path request"


@app.get('/<model_name>')
def get_model(model_name):  # put application's code here

    if model_name is None:
        raise MissingModelException("Please, inform model username in path request")

    req = requests.get(f"{environ.get('CHAT_URL')}/{model_name}")

    if req.status_code == 200:

        modelo = ModelSchema().load(req.json())

        return jsonify(modelo.to_json()), 200

    elif req.status_code == 404:
        return jsonify({"error": f"Model {model_name} not found"}), 404

    else:
        raise Exception("There is a problem in your request")

if __name__ == '__main__':
    app.run()
