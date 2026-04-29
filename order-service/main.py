from fastapi import FastAPI, HTTPException
from prometheus_fastapi_instrumentator import Instrumentator, metrics
import os
import httpx

app = FastAPI(title="Order Service")

# This will be used to simulate a failure
DB_HOST = os.getenv("DB_HOST", "db")
PRODUCT_SERVICE_URL = os.getenv("PRODUCT_SERVICE_URL", "http://product-service:8000")

@app.get("/")
def read_root():
    return {"message": "Order Service is running"}

@app.post("/orders")
async def create_order(product_id: int, quantity: int):
    # 1. Simulate DB connection check (for the incident simulation)
    if DB_HOST == "invalid_host":
        raise HTTPException(status_code=500, detail="Database connection failed")
    
    # 2. Inter-service communication: Verify product exists
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(f"{PRODUCT_SERVICE_URL}/products")
            products = response.json()
            
            # Check if product_id exists in the returned list
            product_exists = any(p["id"] == product_id for p in products)
            
            if not product_exists:
                raise HTTPException(status_code=404, detail=f"Product with ID {product_id} not found")
                
            product_name = next(p["name"] for p in products if p["id"] == product_id)
            
    except httpx.RequestError as exc:
        raise HTTPException(status_code=503, detail=f"Product Service unavailable: {exc}")

    return {
        "status": "order created",
        "product_id": product_id,
        "product_name": product_name,
        "quantity": quantity,
        "message": "Successfully verified via Product Service"
    }

Instrumentator().add(metrics.default()).instrument(app).expose(app)
