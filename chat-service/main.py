from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI(title="Chat Service")

@app.get("/")
def read_root():
    return {"message": "Chat Service is running"}

@app.get("/messages")
def get_messages():
    return [
        {"from": "admin", "text": "Welcome to the system!"},
        {"from": "user_1", "text": "Hello, I need help with my order."}
    ]

Instrumentator().instrument(app).expose(app)
