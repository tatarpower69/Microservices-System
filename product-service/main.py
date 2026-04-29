from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI(title="Product Service")

@app.get("/")
def read_root():
    return {"message": "Product Service is running"}

@app.get("/products")
def get_products():
    return [
        {"id": 1, "name": "Laptop", "price": 1200},
        {"id": 2, "name": "Smartphone", "price": 800},
        {"id": 3, "name": "Headphones", "price": 150}
    ]

Instrumentator().instrument(app).expose(app)
