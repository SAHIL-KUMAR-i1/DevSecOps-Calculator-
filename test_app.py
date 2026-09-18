from fastapi.testclient import TestClient
from app import app

client = TestClient(app)


def test_add():
    response = client.post(
        "/calculate",
        json={"a": 10, "b": 5, "operation": "add"}
    )
    assert response.status_code == 200
    assert response.json()["result"] == 15


def test_subtract():
    response = client.post(
        "/calculate",
        json={"a": 10, "b": 5, "operation": "subtract"}
    )
    assert response.status_code == 200
    assert response.json()["result"] == 5


def test_multiply():
    response = client.post(
        "/calculate",
        json={"a": 10, "b": 5, "operation": "multiply"}
    )
    assert response.status_code == 200
    assert response.json()["result"] == 50


def test_divide():
    response = client.post(
        "/calculate",
        json={"a": 10, "b": 5, "operation": "divide"}
    )
    assert response.status_code == 200
    assert response.json()["result"] == 2


def test_divide_by_zero():
    response = client.post(
        "/calculate",
        json={"a": 10, "b": 0, "operation": "divide"}
    )
    assert response.status_code == 400
