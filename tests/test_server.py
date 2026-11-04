from fastapi.testclient import TestClient

from server.main import app

client = TestClient(app)


def test_health():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json()["app"] == "OMEGA"
    assert response.json()["storage"] == "disabled"


def test_analysis_pipeline():
    response = client.post(
        "/api/analyze",
        json={
            "text": "تحليل نظام تجريبي",
            "mode": "technical",
            "max_steps": 5,
        },
    )

    assert response.status_code == 200

    data = response.json()

    assert data["engine"] == "OMEGA"
    assert len(data["hypotheses"]) > 0
    assert data["plan"]["method"] == "technical"
    assert data["critique"]["review_status"] == "preliminary"
    assert data["storage"]["persistent"] is False


def test_empty_input():
    response = client.post(
        "/api/analyze",
        json={"text": "   "},
    )

    assert response.status_code == 422


def test_invalid_mode():
    response = client.post(
        "/api/analyze",
        json={
            "text": "Test",
            "mode": "unknown",
        },
    )

    assert response.status_code == 422


def test_extra_fields_rejected():
    response = client.post(
        "/api/analyze",
        json={
            "text": "Test",
            "unexpected": True,
        },
    )

    assert response.status_code == 422
