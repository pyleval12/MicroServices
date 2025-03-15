from sqlalchemy import Column, Integer, ForeignKey, DateTime
from datetime import datetime
from db_config import Base, get_session

class Cart(Base):
    __tablename__ = "carts"
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    product_id = Column(Integer, ForeignKey('products.id'), nullable=False)
    quantity = Column(Integer, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

def add_to_cart(user_id: int, product_id: int, quantity: int):
    session = get_session()
    try:
        cart_item = Cart(
            user_id=user_id,
            product_id=product_id,
            quantity=quantity
        )
        session.add(cart_item)
        session.commit()
        return "Item added to cart successfully"
    except Exception as e:
        session.rollback()
        return f"Error adding item to cart: {str(e)}"
    finally:
        session.close()

def get_user_cart(user_id: int):
    session = get_session()
    try:
        cart_items = session.query(Cart).filter_by(user_id=user_id).all()
        return cart_items
    finally:
        session.close()
