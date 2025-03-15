from sqlalchemy import Column, Integer, String
from db_config import Base, get_session

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    age = Column(Integer, nullable=False)
    gender = Column(String(10), nullable=False)

def create_test_users():
    session = get_session()
    try:
        users = [
            User(first_name="John", last_name="Doe", age=30, gender="Male"),
            User(first_name="Alice", last_name="Smith", age=25, gender="Female")
        ]
        session.add_all(users)
        session.commit()
        return "Users created successfully"
    except Exception as e:
        session.rollback()
        return f"Error creating users: {str(e)}"
    finally:
        session.close()
