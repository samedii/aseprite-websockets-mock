import websocket


def on_message(ws, message):
    print(message)


def on_error(wsapp, err):
    print("Got a an error: ", err)


wsapp = websocket.WebSocketApp(
    "ws://localhost:8000/ws", on_message=on_message, on_error=on_error
)
wsapp.send("hey")
wsapp.wait()
