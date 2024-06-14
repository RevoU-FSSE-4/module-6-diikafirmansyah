import pytest
from flask import json
from unittest.mock import MagicMock
from app import app
from zoo.routes import employee


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_creat_employee(client):
    employee.employee_service = MagicMock()
    create_employee = {"id": "1", "employee_name": "Jhon", "gender": "male"}
    employee.employee_service.add_employee.return_value = create_employee

    response = client.post(
        "/employees", data=json.dumps(create_employee), content_type="application/json"
    )

    employee.employee_service.add_employee.assert_called_once_with(create_employee)
    assert response.status_code == 200
    assert json.loads(response.get_data()) == create_employee


def test_update_employee(client):
    employee.employee_service = MagicMock()
    update_employee_info = {"employee_name": "Lion", "gender": "male"}
    employee.employee_service.update_employee.return_value = update_employee_info

    response = client.put(
        "/employees/1",
        data=json.dumps(update_employee_info),
        content_type="application/json",
    )

    assert response.status_code == 200
    assert json.loads(response.get_data(as_text=True)) == update_employee_info


def test_get_all_employee(client):
    employee.employee_service = MagicMock()
    all_employee_info = [
        {"id": "1", "employee_name": "Tiger", "gender": "male"},
        {"id": "2", "employee_name": "Lion", "gender": "Female"},
    ]
    employee.employee_service.get_all.return_value = all_employee_info

    response = client.get("/employees")

    employee.employee_service.get_all.assert_called_once()
    assert response.status_code == 200
    assert json.loads(response.get_data()) == all_employee_info


def test_get_employee(client):
    employee.employee_service = MagicMock()
    employee_info = {"id": "1", "employee_name": "Tiger", "gender": "male"}
    employee.employee_service.get_employee.return_value = employee_info

    response = client.get("/employees/1")

    employee.employee_service.get_employee.assert_called_once_with("1")
    assert response.status_code == 200
    assert json.loads(response.get_data()) == employee_info


def test_delete_aninal(client):
    employee.employee_service = MagicMock()
    employee_info_delete = {"id": "1", "employee_name": "Tiger", "gender": "male"}
    employee.employee_service.delete_employee.return_value = employee_info_delete

    response = client.delete("/employees/1")

    employee.employee_service.delete_employee.assert_called_once_with("1")
    assert response.status_code == 200
