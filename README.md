# mock stable diffusion api with websockets

Install environment

```bash
poetry install
```

Start the server

```bash
python -m app.main --reload
```

## Client example

Using `websocket-client`.

```python
import websocket


def on_message(wsapp, message):
    print(message)


ws = websocket.WebSocket()
ws.connect("ws://localhost:8000/ws")
ws.send("hello")
print(ws.recv())
ws.close()
```
