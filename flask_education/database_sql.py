from sqlalchemy import create_engine, MetaData, select, Table, desc, func
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Boolean
import dotenv
import os
from pathlib import Path
import time

dotenv.load_dotenv(Path('.env'))

dbconfig = {'host': os.environ.get('host'),
            'user': os.environ.get('user'),
            'password': os.environ.get('password'),
            'database': os.environ.get('database')}

engine_sakila = create_engine(
    url=f'mysql+pymysql://{dbconfig['user']}:{dbconfig['password']}@{dbconfig['host']}:3306/{dbconfig['database']}',
    # echo=True,
    pool_size=5,
    max_overflow=10
)

# УСЛИ ТАБЛИЦА ЕСТЬ (УСТАРЕВШИЙ ВАРИАНТ)
# metadata = MetaData()
# metadata.reflect(bind=engine_hr)
# Base = automap_base(metadata=metadata)
# Base.prepare()
# Employees = Base.classes.hr.employees

# УСЛИ ТАБЛИЦА ЕСТЬ (НОВЫЙ ВАРИАНТ)
Base = automap_base()
Base.prepare(autoload_with=engine_sakila)

Film = Base.classes.film
Film_category = Base.classes.film_category
Category = Base.classes.category

Film.film_category = relationship(Film_category, backref='film')
Category.film_name = relationship(Film_category, backref='category')


print(dir(Film))
print(dir(Film_category))
print(dir(Category))


# with engine_sakila.connect() as connection:
#     query = select(Film)
#     results = connection.execute(query)




# start_time = time.time()
# with engine_sakila.connect() as connection:
#     query = select(Film)
#     results = connection.execute(query)
# end_time = time.time()
# print(f"Время выполнения Engine: {end_time - start_time:.4f} секунд")
#
# start_time = time.time()
# Session = sessionmaker(bind=engine_sakila)
# with Session() as session:
#     films = session.query(Film).all()
# end_time = time.time()
# print(f"Время выполнения Session: {end_time - start_time:.4f} секунд")
#
#
# start_time = time.time()
# with engine_sakila.connect() as connection:
#     query = select(Film)
#     films = connection.execute(query)
# end_time = time.time()
# print(f"Время выполнения Engine: {end_time - start_time:.4f} секунд")


Session = sessionmaker(bind=engine_sakila)
with Session() as session:
    pass
    # film = session.get(Film, 1)
    # print(film.__dict__)

    # films = session.query(Film).all()

    # films = session.query(Film).filter(Film.release_year > 2021).order_by(desc(Film.title)).all()
    # for film in films:
    #     print(film.release_year, film.title)

    # films = session.query(func.count(Film.film_id)).scalar()
    # # print(films)

    # films = session.query(Film).having(Film.film_id ==1)
    # print(films.__dict__)

    # Подзапрос для вычисления среднего возраста сохраняем в переменную
    # average_release_year_subquery = session.query(func.avg(Film.release_year).label('average_release_year')).subquery()
    # # Основной запрос, использующий подзапрос для фильтрации пользователей
    # films = session.query(Film).filter(Film.release_year > average_release_year_subquery).all()
    # # Выполним подзапрос отдельно для проверки результата
    # print(f"Average age is {session.query(average_release_year_subquery).scalar()}")
    # # Выведем отобранные данные
    # for film in films:
    #      print(film.release_year, film.title)

    # film = session.query(Film).join(Film_category).join(Category)
    # print(film)








