import os

import pytest
from main import create_app

headers = {"x-access-tokens": "testing"}
os.environ.update({"TOKEN": "testing"})


@pytest.fixture()
def app():
    app = create_app()
    yield app


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()


def test_index(client):
    response = client.get("/", headers=headers)
    print(response.json)
    assert "ok" in response.json["APP"]


def test_restart_kodi(client):
    response = client.post("/kodi/restart/", headers=headers)
    print(response.json)
    assert response.json["code"] == 0
