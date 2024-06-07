from flask import Flask, request, jsonify 
from flasgger import Swagger
from animal import animals_blueprint
from employe import employes_blueprint



app = Flask(__name__)
app.register_blueprint(animals_blueprint)
app.register_blueprint(employes_blueprint)
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