from flask import Blueprint, request, jsonify
from flasgger import swag_from

animals_blueprint = Blueprint("animals", __name__)
animals = []


@animals_blueprint.route("/animals", methods=["GET"])
@swag_from("docs/Allanimal.yml")
def get_animals():
    return jsonify({"List of animals": animals}), 200


@animals_blueprint.route("/animals", methods=["POST"])
@swag_from("docs/Addanimal.yml")
def add_animal():
    data = request.get_json()
    animal = data.get("animal")
    food = data.get("food")
    if animal and food:
        animals.append({"animal": animal, "food": food})
        return (
            jsonify(
                {
                    "Message": "Animal added into the zoo!",
                    "animal": animal,
                    "food": food,
                }
            ),
            201,
        )
    else:
        return jsonify({"Error": "no animals added to the zoo"}), 400


@animals_blueprint.route("/animals/<int:animal_index>", methods=["GET"])
@swag_from("docs/seeanimals.yml")
def get_animal(animal_index):
    try:
        animal = animals[animal_index]
        return jsonify({"Animal Information": animal}), 200
    except IndexError:
        return jsonify({"Error": "We dont have that animal on the zoo"}), 400


@animals_blueprint.route("/animals/<int:animal_index>", methods=["DELETE"])
@swag_from("docs/deleteanimals.yml")
def delete_animal(animal_index):
    try:
        del animals[animal_index]
        animal = animals[animal_index]
        return jsonify({"Release Animal": animal, "Remaining animals": animal}), 200
    except IndexError:
        return jsonify({f"Error": "We dont have that animal on the zoo"}), 400


@animals_blueprint.route("/animals/<int:animal_index>", methods=["PUT"])
@swag_from("docs/updateanimals.yml")
def put_animal(animal_index):
    data = request.get_json()
    animal = data.get("animal")
    food = data.get("food")
    try:
        if animal and food:
            animals[animal_index] = {"animal": animal, "food": food}
            return (
                jsonify(
                    {
                        "Message": "Animal updated into the zoo!",
                        "Updated": animals[animal_index],
                    }
                ),
                201,
            )
        else:
            return jsonify({"Error": "no animals added to the zoo"}), 400
    except IndexError:
        return jsonify({"Error": "animal not found"}), 404
