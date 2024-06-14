from flask import Flask, request
from zoo.routes.animal import animals_blueprint
from zoo.routes.employee import employees_blueprint

from flasgger import Swagger


app = Flask(__name__)
app.register_blueprint(animals_blueprint)
app.register_blueprint(employees_blueprint)
swagger = Swagger(app)


@app.route("/", methods=["GET"])
def animal():
    return "Welcome to Zoo Database"


@app.route("/zoo", methods=["GET", "POST"])
def handle_animal_name():
    if request.method == "POST":
        return {"message": "Add new animal on the zoo database"}
    else:
        return {"message": "Return list animal on the zoo "}


if __name__ == "__main__":
    app.run(debug=True)
