from fastapi.testclient import TestClient
from fastapi.websockets import WebSocket
import pytest
from app.main import app


client = TestClient(app)


def test_health():
    response = client.get("/health")
    assert response.status_code == 200


def test_websocket():
    with client.websocket_connect("/ws") as websocket:
        websocket.send_text("hello")
        data = websocket.receive_bytes()
        websocket.close()
