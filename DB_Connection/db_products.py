
from sqlalchemy import create_engine, text, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

def create_table(DATABASE_URL):

# 🔹 Подключение к PostgreSQL (замени параметры, если нужно)

    engine = create_engine(DATABASE_URL)

    Base = declarative_base()

    class Product(Base):
        __tablename__ = "products"

        id = Column(Integer, primary_key=True)
        name = Column(String(100), nullable=False)
        price = Column(Integer, nullable=False)
        stock = Column(Integer, nullable=False)



    Base.metadata.create_all(engine)

    # 🔹 Создание сессии
    Session = sessionmaker(bind=engine)
    session = Session()

    # 🔹 Добавление пользователей в таблицу
    products = [
        Product(id=1, name="iPhone 14", price = "999", stock = 5),
        Product(id=2, name="MacBook", price="2500", stock=2),
        Product(id=3, name="AirPods", price = "199", stock = 10),
        Product(id=4, name="Monitor", price = "500", stock = 7),
        Product(id=5, name="Keyboard", price = "100", stock = 15)
        ]
    session.add_all(products)
    session.commit()

    return "All fine"
