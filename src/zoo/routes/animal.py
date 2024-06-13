from flask import Blueprint, request
from flasgger import swag_from
from zoo.services.animal_service import AnimalService
from zoo.repository.animal_repository import AnimalRepository
animals_blueprint = Blueprint("animals", __name__)
animal_service = AnimalService(animal_repository = AnimalRepository())
@animals_blueprint.route("/animals", methods=["GET"])
@swag_from("docs/allAnimal.yml")
def get_animals():
    animals = animal_service.get_all()
    return animals
@animals_blueprint.route("/animals", methods=["POST"])
@swag_from("docs/addAnimal.yml")
def add_animal():
    data = request.get_json()
    try:
        animal = animal_service.add_animal(data)
    except ValueError as e:
        return {"error": str(e)}, 400
    return animal, 201
@animals_blueprint.route("/animals/<string:id>", methods=["GET"])
@swag_from("docs/seeInfoAnimal.yml")
def get_animal(id):
    animal = animal_service.get_animal(id)
    if animal is None:
        return{"Error": "Animal not found"}, 400
    return animal
@animals_blueprint.route("/animals/<string:id>", methods=["PUT"])
@swag_from("docs/updateInfoAnimal.yml")
def update_animal(id):
    data = request.get_json()
    try:
        animal = animal_service.update_animal(data, id)
    except ValueError as e:
        return {"Error": str(e)}, 400
    return animal, 201
@animals_blueprint.route("/animals/<string:id>", methods=["DELETE"])
@swag_from("docs/deleteAnimal.yml")
def delete_animal(id):
    animal = animal_service.delete_post(id)
    if animal is None:
        return {"Error": "Animal not found"}, 400
    return {"Animal has been realsed": animal}, 200