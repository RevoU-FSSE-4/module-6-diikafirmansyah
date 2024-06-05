from flask import Flask, request, jsonify 
from flasgger import Swagger


app = Flask(__name__)
swagger = Swagger (app)


@app. route("/", methods=["GET"])
def animal():
    return "Welcome to the ZOO"


@app. route("/animal", methods=["GET", "POST"])
def handle_animal_name():
    if request.method == "POST":
        return {"message": "Add new animal on ZOO"}
    else:
         return {"message": "Return list of animal "}