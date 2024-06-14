import pytest
from flask import json
from unittest.mock import MagicMock
from app import app
from zoo.routes import animal


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_creat_animal(client):
    animal.animal_service = MagicMock()
    create_animal = {"id": "1", "animal_name": "Tiger", "gender": "male"}
    animal.animal_service.add_animal.return_value = create_animal

    response = client.post(
        "/animals", data=json.dumps(create_animal), content_type="application/json"
    )

    animal.animal_service.add_animal.assert_called_once_with(create_animal)
    assert response.status_code == 200
    assert json.loads(response.get_data()) == create_animal


def test_update_animal(client):
    animal.animal_service = MagicMock()
    update_animal_info = {"animal_name": "Lion", "gender": "male"}
    animal.animal_service.update_animal.return_value = update_animal_info

    response = client.put(
        "/animals/1",
        data=json.dumps(update_animal_info),
        content_type="application/json",
    )

    assert response.status_code == 200
    assert json.loads(response.get_data(as_text=True)) == update_animal_info


def test_get_all_animal(client):
    animal.animal_service = MagicMock()
    all_animal_info = [
        {"id": "1", "animal_name": "Tiger", "gender": "male"},
        {"id": "2", "animal_name": "Lion", "gender": "Female"},
    ]
    animal.animal_service.get_all.return_value = all_animal_info

    response = client.get("/animals")

    animal.animal_service.get_all.assert_called_once()
    assert response.status_code == 200
    assert json.loads(response.get_data()) == all_animal_info


def test_get_animal(client):
    animal.animal_service = MagicMock()
    animal_info = {"id": "1", "animal_name": "Tiger", "gender": "male"}
    animal.animal_service.get_animal.return_value = animal_info

    response = client.get("/animals/1")

    animal.animal_service.get_animal.assert_called_once_with("1")
    assert response.status_code == 200
    assert json.loads(response.get_data()) == animal_info


def test_delete_aninal(client):
    animal.animal_service = MagicMock()
    animal_info_delete = {"id": "1", "animal_name": "Tiger", "gender": "male"}
    animal.animal_service.delete_animal.return_value = animal_info_delete

    response = client.delete("/animals/1")

    animal.animal_service.delete_animal.assert_called_once_with("1")
    assert response.status_code == 200
