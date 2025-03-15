from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import httpx

app = FastAPI()


class OrderItem(BaseModel):
    product_id: int
    quantity: int


class Order(BaseModel):
    id: int
    user_id: int
    items: List[OrderItem]
    total: float = 0


orders_db = []


@app.post("/orders/", response_model=Order)
async def create_order(order: Order):
    # Проверяем существование пользователя
    async with httpx.AsyncClient() as client:
        user_response = await client.get(f"http://users:8001/users/{order.user_id}")
        if user_response.status_code != 200:
            raise HTTPException(status_code=404, detail="User not found")

        # Проверяем наличие продуктов и считаем общую сумму
        total = 0
        for item in order.items:
            product_response = await client.get(f"http://products:8002/products/{item.product_id}")
            if product_response.status_code != 200:
                raise HTTPException(status_code=404, detail="Product not found")
            product = product_response.json()
            total += product["price"] * item.quantity

        order.total = total
        orders_db.append(order)
        return order