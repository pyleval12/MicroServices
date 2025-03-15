a=[1,2,3]
b=iter(a)
print(next(b))
print(next(b))
print(next(b))

Invoke - WebRequest - Uri POST "http://localhost:8002/products/" -
H "Content-Type:
application/json" -d '{
"id": 1,
"name": "Laptop",
"price": 999.99,
"stock": 10
}'

Invoke-WebRequest -Uri "http://localhost:8002/products/" -Method Post -Headers @{"Content-Type"="application/json"} -Body '{
    "id": 1,
    "name": "Laptop",
    "price": 999.99,
    "stock": 10
}'
