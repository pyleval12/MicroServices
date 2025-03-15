from sqlalchemy import create_engine, text, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker


# 🔹 Подключение к PostgreSQL (замени параметры, если нужно)
DATABASE_URL = "postgresql://admin:secret@localhost:5432/mydatabase"
engine = create_engine(DATABASE_URL)

try:
    engine = create_engine(DATABASE_URL)
    with engine.connect() as connection:
        result = connection.execute(text("SELECT * FROM persons "))
        rows = result.fetchall()

        print("✅ Успешное подключение к базе данных!")
 #      print(type(row))
 #        for row in rows:
 #            print(row)
        data = [dict(zip(result.keys(), row)) for row in rows]
        for item in data:
            print(f"User first name:{item["fname"]}\nUser last name:{item["lname"]}\nUser age:{item["age"]}\nUser gender:{item["gender"]}")
except Exception as e:
    print(f"❌ Ошибка подключения: {e}")
