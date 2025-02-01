# Создайте модель Event, которая включает поля:
# title (строка),
# date (дата и время события),
# location (строка).
# Добавьте валидацию, чтобы дата события не была в прошлом.


from sqlalchemy import Column
# from pydantic import BaseModel, field_validator
# from datetime import datetime
#
# class Event(BaseModel):
#     title: str
#     date: datetime
#     location: str
#
#     @field_validator('date')
#     def validate_email(cls, value: datetime):
#         if datetime.now() < value:
#             raise ValueError('Event cannot be in the future')
#         return value


# Создайте модель User с полями:
# id (целочисленный тип, первичный ключ),
# name (строковый тип, длина до 50 символов),
# age (целочисленный тип).
# Определите две модели, User и Post, где пользователь может иметь много постов
# (один ко многим). Используйте декларативный базовый класс.



from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, Text, ForeignKey

Base1 = declarative_base()

class User(Base1):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    age = Column(Integer)

class Post(Base1):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    text = Column(Text, nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))


user1 = User(
    name='user1',
    age=18,
)







