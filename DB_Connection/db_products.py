from sqlalchemy import Column, Integer, String
from db_config import Base, get_session

class Product(Base):
    __tablename__ = "products"
    
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    price = Column(Integer, nullable=False)
    stock = Column(Integer, nullable=False)

def create_test_products():
    session = get_session()
    try:
        products = [
            Product(name="iPhone 14", price=999, stock=5),
            Product(name="MacBook", price=2500, stock=2),
            Product(name="AirPods", price=199, stock=10)
        ]
        session.add_all(products)
        session.commit()
        return "Products created successfully"
    except Exception as e:
        session.rollback()
        return f"Error creating products: {str(e)}"
    finally:
        session.close()
