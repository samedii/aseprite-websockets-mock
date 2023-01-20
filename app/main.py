from pathlib import Path
import argparse
from fastapi import (
    FastAPI,
    status,
    WebSocket,
)
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import RedirectResponse
import uvicorn


app = FastAPI(
    title="stable-diffusion",
    description="Stable Diffusion API",
    version=Path("VERSION").read_text().strip(),
)

# CORS errors instead of seeing internal exceptions
# https://stackoverflow.com/questions/63606055/why-do-i-get-cors-error-reason-cors-request-did-not-succeed
cors = CORSMiddleware(
    app=app,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", status_code=status.HTTP_303_SEE_OTHER, include_in_schema=False)
def redirect_to_docs():
    return RedirectResponse(url="/docs")


@app.get("/health", status_code=status.HTTP_200_OK)
def health():
    return {}


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    print("waiting", flush=True)
    await websocket.accept()
    print("accepted", flush=True)
    data = await websocket.receive_text()
    print("Received: ", data)
    await websocket.send_bytes(Path("cute_dragon.png").read_bytes(), flush=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--host", type=str, default="0.0.0.0")
    parser.add_argument("--port", type=int, default=8000)
    parser.add_argument("--workers", type=int, default=2)
    parser.add_argument("--reload", action="store_true")
    args = parser.parse_args()

    uvicorn.run(
        "app.main:cors",
        host=args.host,
        port=args.port,
        reload=args.reload,
        workers=1 if args.reload else args.workers,
    )
