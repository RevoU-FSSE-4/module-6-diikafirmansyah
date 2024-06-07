from flask import Blueprint, request, jsonify

employes_blueprint = Blueprint("employes", __name__)
employes = []


@employes_blueprint.route("/employes", methods=["GET"])
def get_employes():
    return jsonify({"List of employes": employes}), 200


@employes_blueprint.route("/employes", methods=["POST"])
def add_employe():
    data = request.get_json()
    name = data.get("name")
    gender = data.get("gender")
    age = data.get("age")
    if name and gender and age:
        employes.append({"name": name, "gender": gender, "age" : age})
        return (
            jsonify(
                {
                    "Message": "employe added into the list!",
                    "name": name,
                    "gender": gender,
                    "age": age,
                }
            ),
            201,
        )
    else:
        return jsonify({"Error": "no employe added to the list"}), 400


@employes_blueprint.route("/employes/<int:employe_index>", methods=["GET"])
def get_employe(employe_index):
    try:
        employe = employes[employe_index]
        return jsonify({"employe Information": employe}), 200
    except IndexError:
        return jsonify({"Error": "We dont have that employe on the list"}), 400


@employes_blueprint.route("/employes/<int:employe_index>", methods=["DELETE"])
def delete_employe(employe_index):
    try:
        del employes[employe_index]
        employe = employes[employe_index]
        return (
            jsonify({"Release employe": employe, "Remaining employe": employes}),
            200,
        )
    except IndexError:
        return jsonify({f"Error": "We dont have that employe on the list"}), 400


@employes_blueprint.route("/employes/<int:employe_index>", methods=["PUT"])
def put_emplpoye(employe_index):
    data = request.get_json()
    name = data.get("name")
    gender = data.get("gender")
    age = data.get("age")
    try:
        if name and gender and age:
            employes[employe_index] = {"name": name, "gender": gender, "age": age}
            return (
                jsonify(
                    {
                        "Message": "employe updated into the list!",
                        "Updated": employes[employe_index],
                    }
                ),
                201,
            )
        else:
            return jsonify({"Error": "no employe added to the list"}), 400
    except IndexError:
        return jsonify({"Error": "employe not found"}), 404
