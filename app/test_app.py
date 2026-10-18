
import pytest
from app import app


@pytest.fixture()
def client():
    app.config["TESTING"] = True

    with app.test_client() as test_client:
        yield test_client


def test_homepage_returns_success(client):
    response = client.get("/")

    assert response.status_code == 200
    assert response.json["status"] == "running"


def test_health_endpoint_returns_healthy(client):
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json["status"] == "healthy"


def test_unknown_route_returns_404(client):
    response = client.get("/unknown")

    assert response.status_code == 404
