from fastapi.testclient import TestClient
from fastapi.websockets import WebSocket
import pytest
from app.main import app


client = TestClient(app)


def test_health():
    response = client.get("/health")
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_websocket():
    with client.websocket_connect("/ws") as websocket:
        await websocket.send_text("hello")
        data = await websocket.receive_bytes()
        await websocket.close()
