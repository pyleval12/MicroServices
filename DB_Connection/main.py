from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker
from datetime import datetime
from db_config import Base, engine
from db_users import create_test_users
from db_products import create_test_products
from db_cart import add_to_cart, get_user_cart

DATABASE_URL = "postgresql://user:password@localhost:5432/testdb"
engine = create_engine(DATABASE_URL)
Base = declarative_base()

# # Модель пользователя
# class User(Base):
#     __tablename__ = "users"
    
#     id = Column(Integer, primary_key=True)
#     first_name = Column(String(50), nullable=False)
#     last_name = Column(String(50), nullable=False)
#     age = Column(Integer, nullable=False)
#     gender = Column(String(10), nullable=False)

# # Модель продукта
# class Product(Base):
#     __tablename__ = "products"
    
#     id = Column(Integer, primary_key=True)
#     name = Column(String(100), nullable=False)
#     price = Column(Integer, nullable=False)
#     stock = Column(Integer, nullable=False)

# # Модель корзины
# class Cart(Base):
#     __tablename__ = "carts"
    
#     id = Column(Integer, primary_key=True)
#     user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
#     product_id = Column(Integer, ForeignKey('products.id'), nullable=False)
#     quantity = Column(Integer, nullable=False)
#     created_at = Column(DateTime, default=datetime.utcnow)
#     updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

def init_db():
    # Создаем все таблицы
    Base.metadata.create_all(engine)
    
    # Создаем тестовые данные
    print(create_test_users())
    print(create_test_products())
    
    # Тестируем корзину
    print(add_to_cart(user_id=1, product_id=1, quantity=2))
    cart_items = get_user_cart(user_id=1)
    print(f"Items in cart: {len(cart_items)}")

if __name__ == "__main__":
    init_db()