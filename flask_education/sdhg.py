from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey, Numeric
from sqlalchemy.orm import sessionmaker, relationship, declarative_base
from datetime import datetime, timedelta
from sqlalchemy.sql import func


Base = declarative_base()
engine = create_engine('sqlite:///:memory:')
Session = sessionmaker(bind=engine)
session = Session()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    orders = relationship("Order", back_populates="user")


class Order(Base):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    amount = Column(Numeric)
    created_at = Column(DateTime)
    user = relationship("User", back_populates="orders")

Base.metadata.create_all(engine)

user1 = User(name="Alice", age=30)
user2 = User(name="Bob", age=22)
session.add_all([user1, user2])
session.commit()

order1 = Order(user_id=user1.id, amount=100.50, created_at=datetime.now() - timedelta(days=1))
order2 = Order(user_id=user1.id, amount=200.75, created_at=datetime.now())
order3 = Order(user_id=user2.id, amount=80.99, created_at=datetime.now() - timedelta(days=2))
session.add_all([order1, order2, order3])
session.commit()

# Напишите простой запрос для вывода имен всех пользователей из таблицы User.
# Используйте функцию func.count() для подсчёта общего количества пользователей
# в базе данных.
# Напишите запрос для поиска пользователя по его уникальному идентификатору
# (id). Допустим, мы ищем пользователя с id равным 1.
# with session as session:
#     users = session.query(User).all()
#     for user in users:
#         print(user.__dict__)

# with session as session:
#     count_users = session.query(func.count(User.id)).scalar()
#     print(count_users)
#
# with session as session:
#     user = session.query(User).filter(User.id == 1).one()
#     print(user.__dict__)

with session as session:
    user = session.get(User, 1)
    print(user.__dict__)






