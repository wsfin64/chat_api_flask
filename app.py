import requests
from flask import Flask, jsonify
from os import environ
from model.model import ModelSchema

app = Flask(__name__)


@app.get('/<model_name>')
def get_model(model_name):  # put application's code here

    req = requests.get(f"{environ.get('CHAT_URL')}/{model_name}")

    modelo = ModelSchema().load(req.json())

    return jsonify(modelo.to_json())


if __name__ == '__main__':
    app.run()
