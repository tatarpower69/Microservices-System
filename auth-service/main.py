from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI(title="Auth Service")

@app.get("/")
def read_root():
    return {"message": "Auth Service is running"}

@app.post("/login")
def login():
    return {"status": "success", "token": "fake-jwt-token"}

@app.post("/register")
def register():
    return {"status": "user created"}

Instrumentator().instrument(app).expose(app)
