from fastapi.testclient import TestClient

from src.main import app

client = TestClient(app)


def test_home():

    response = client.get("/")

    assert response.status_code == 200

    assert response.json() == {"message": "Welcome to Smart Expense Tracker API"}


def test_add_expense():

    response = client.post(
        "/expenses",
        json={
            "id": 101,
            "title": "Book",
            "amount": 500,
            "category": "Education",
            "date": "2026-07-31",
        },
    )

    # POST now returns 201 Created

    assert response.status_code == 201

    assert response.json()["message"] == "Expense added successfully"


def test_get_expenses():

    response = client.get("/expenses")

    assert response.status_code == 200

    assert isinstance(response.json(), list)


def test_total_expenses():

    response = client.get("/expenses/total")

    assert response.status_code == 200

    assert "total" in response.json()


def test_filter_category():

    response = client.get("/expenses/category/Education")

    assert response.status_code == 200

    assert isinstance(response.json(), list)


def test_monthly_summary():
    response = client.get("/expenses/monthly/2026-07")

    assert response.status_code == 200
    assert "month" in response.json()
    assert "total" in response.json()
