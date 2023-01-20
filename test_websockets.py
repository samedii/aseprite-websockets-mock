import websocket


def on_message(wsapp, message):
    print(message)


ws = websocket.WebSocket()
ws.connect("ws://localhost:8000/ws")
ws.send("Hello, Server")
print(ws.recv())
ws.close()
