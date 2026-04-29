from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI(title="User Service")

@app.get("/")
def read_root():
    return {"message": "User Service is running"}

@app.get("/profile/{user_id}")
def get_profile(user_id: int):
    return {"user_id": user_id, "username": f"user_{user_id}", "email": f"user_{user_id}@example.com"}

Instrumentator().instrument(app).expose(app)
