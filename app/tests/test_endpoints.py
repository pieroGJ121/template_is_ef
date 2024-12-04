from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

dni = "210"
booking_id = "3012"
ticket_id = "4822"


def test_ticket_purchase_success():
    response = client.post(
        "/ticket/purchase", json={"dni": dni, "id_booking": id_booking}
    )
    assert response.status_code == 200
    assert "purchase" in response.json()


def test_ticket_purchase_user_inexistent():
    response = client.post(
        "/ticket/purchase", json={"dni": "failure", "id_booking": id_booking}
    )
    assert response.status_code == 404


def test_ticket_purchase_booking_inexistent():
    response = client.post("/ticket/purchase", json={"dni": dni, "id_booking": "faker"})
    assert response.status_code == 404


def test_ticket_cancelation_success():
    response = client.post(
        "/ticket/cancelation", json={"dni": dni, "id_booking": id_booking}
    )
    assert response.status_code == 200
    assert "cancelation" in response.json()


def test_ticket_cancelation_user_inexistent():
    response = client.post(
        "/ticket/cancelation", json={"dni": "failure", "id_booking": id_booking}
    )
    assert response.status_code == 404


def test_ticket_cancelation_booking_inexistent():
    response = client.post(
        "/ticket/cancelation", json={"dni": dni, "id_booking": "faker"}
    )
    assert response.status_code == 404


def test_ticket_booking_success():
    response = client.post("/ticket/booking", json={"dni": dni, "id_ticket": id_ticket})
    assert response.status_code == 200
    assert "booking" in response.json()


def test_ticket_booking_user_inexistent():
    response = client.post(
        "/ticket/booking", json={"dni": "failure", "id_ticket": id_ticket}
    )
    assert response.status_code == 404


def test_ticket_cancelation_booking_inexistent():
    response = client.post("/ticket/bookin", json={"dni": dni, "id_ticket": "faker"})
    assert response.status_code == 404
