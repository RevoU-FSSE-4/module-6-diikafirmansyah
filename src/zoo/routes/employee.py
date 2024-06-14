from flask import Blueprint, request
from flasgger import swag_from
from zoo.repository.employee_repository import EmployeeRepository
from zoo.services.employee_service import EmployeeService


employees_blueprint = Blueprint("employees", __name__)
employee_service = EmployeeService(employee_repository=EmployeeRepository())


@employees_blueprint.route("/employees", methods=["GET"])
@swag_from("docs/allEmployees.yml")
def get_all():
    employees = employee_service.get_all()
    return employees


@employees_blueprint.route("/employees", methods=["POST"])
@swag_from("docs/addEmployee.yml")
def add_employee():
    data = request.get_json()
    try:
        employee = employee_service.add_employee(data)
    except ValueError as e:
        return {"error": str(e)}, 400
    return employee, 200


@employees_blueprint.route("/employees/<string:id>", methods=["GET"])
@swag_from("docs/seeInfoEmployee.yml")
def get_employee(id):
    employee = employee_service.get_employee(id)
    if employee is None:
        return {"Error": "Employee not found"}, 400
    return employee


@employees_blueprint.route("/employees/<string:id>", methods=["PUT"])
@swag_from("docs/updateInfoEmployee.yml")
def update_employee(id):
    data = request.get_json()
    try:
        employee = employee_service.update_employee(data, id)
    except ValueError as e:
        return {"Error": str(e)}, 400
    return employee, 200


@employees_blueprint.route("/employees/<string:id>", methods=["DELETE"])
@swag_from("docs/deleteEmployee.yml")
def delete_employee(id):
    employee = employee_service.delete_employee(id)
    if employee is None:
        return {"Error": "Employee not found"}, 400
    return {"Employee has been kick out": employee}, 200
