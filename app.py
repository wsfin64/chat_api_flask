import requests
from flask import Flask, jsonify
from os import environ
from model.model import ModelSchema
from exceptions.custom_exceptions import MissingModelException

app = Flask(__name__)


@app.get("/")
def root():
    return "Please, inform model's username in path request"


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


@app.get("/favorites")
def verify_if_favorites_is_online():

    favorites_online = []
    favorites = environ.get('FAVORITES').split(',')

    for favorite in favorites:
        fav = favorite.replace(" ", "").replace("'", "")
        req = requests.get(f"{environ.get('CHAT_URL')}/{fav}")

        if req.status_code == 200:
            model = ModelSchema().load(req.json())

            if model.room_status == 'public':
                favorites_online.append(model)

    if len(favorites_online) == 0:
        return jsonify("None of your favorites are online now"), 200

    return jsonify(favorites_online), 200


@app.route("/<string>", methods=['POST', 'PUT', 'PATCH', 'DELETE'])
def post_model(string):
    return f"""
        <h2>method not allowed, use GET instead</h2>
        <img src={environ.get('GIF_IMAGE')} alt='gia_baker'>
    """


@app.post('/')
def default():
    return f"""
     <video controls autoplay loop>
    <source src="{environ.get('VIDEO')}" type="video/mp4">
    Your browser does not support the video tag.
</video> 
"""


if __name__ == '__main__':
    app.run()
