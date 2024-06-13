import pytest 
from flask import json
from unittest.mock import MagicMock
from app import app
from zoo.routes import animal

@pytest.fixture 
def client():
    with app.test_client() as client :
        yield client 