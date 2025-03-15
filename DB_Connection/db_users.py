
from sqlalchemy import create_engine, text, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

def create_table(DATABASE_URL):

# 🔹 Подключение к PostgreSQL (замени параметры, если нужно)

    engine = create_engine(DATABASE_URL)

    Base = declarative_base()

    class User(Base):
        __tablename__ = "users"

        id = Column(Integer, primary_key=True)
        first_name = Column(String(50), nullable=False)
        last_name = Column(String(50), nullable=False)
        age = Column(Integer, nullable=False)
        gender = Column(String(10), nullable=False)


    Base.metadata.create_all(engine)

    # 🔹 Создание сессии
    Session = sessionmaker(bind=engine)
    session = Session()

    # 🔹 Добавление пользователей в таблицу
    users = [
        User(first_name="John", last_name="Doe", age=30, gender="Male"),
        User(first_name="Alice", last_name="Smith", age=25, gender="Female"),
        User(first_name="Bob", last_name="Johnson", age=35, gender="Male")
        ]
    session.add_all(users)
    session.commit()

    return "All fine"
