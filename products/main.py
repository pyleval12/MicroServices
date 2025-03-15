from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

class Product(BaseModel):
    id: int
    name: str
    price: float
    stock: int

products_db = []

@app.post("/products/", response_model=Product)
async def create_product(product: Product):
    products_db.append(product)
    return product

@app.get("/products/{product_id}", response_model=Product)
async def get_product(product_id: int):
    product = next((prod for prod in products_db if prod.id == product_id),None)
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return product