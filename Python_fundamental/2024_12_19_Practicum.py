import os
import dotenv
from pathlib import Path
import mysql.connector

dotenv.load_dotenv(Path('.env'))
dbconfig = {'host': os.environ.get('host'),
            'user': os.environ.get('user'),
            'password': os.environ.get('password'),
            'database': 'sakila'}

connection = mysql.connector.connect(**dbconfig)
cursor = connection.cursor()

def get_category() ->dict:
    cursor.execute('select category_id, name from category')
    return {k:v for k, v in cursor.fetchall()}

def show_dict(dictionary):
    for key, value in dictionary.items():
        print(f'{key}: {value}')

def get_film_with_category(category: int) -> list:
    select = """select f.title, f.description, f.release_year, f.rating, f.special_features
        from film as f
        inner join film_category as fc
        on f.film_id = fc.film_id
        and category_id = %s;"""
    cursor.execute(select, (category, ))
    return cursor.fetchall()

def show_films(films: list) -> None:
    for i, row in enumerate(films, start=1):
        print(f'{i}: {row}')
        if i % 10 == 0:
            n = int(input('Показать следующие 10 фильмов? 1-да, 0-нет: '))
            if n == 0:
                break
    else: print('Это были все фильмы этой выборки')


def base_branch():
    while True:
        print("Выберете критерий поиска:\n\t1 - по актеру,\t2 - по категории")
        user_choice = int(input('Ведите номер: '))
        all_choice = {
            1: actor_search,
            2: category_search
        }
        all_choice[user_choice]()

def category_search():
    show_dict(get_category())
    n = int(input('Укажите номер категории: '))
    show_films(get_film_with_category(n))


# def search_film_actors() ->dict:
#     cursor.execute('select category_id, name from category')
#     return {k:v for k, v in cursor.fetchall()}


def actor_search():
    select = """select f.title, f.description, f.release_year, f.rating, f.special_features, a.actor_name
            from film as f
            inner join film_actor as fa on f.film_id = fa.film_id
            inner join (
                select actor_id, concat(first_name, " ", last_name) as actor_name
            from actor
            ) as a
            on a.actor_id = fa.actor_id
            and a.actor_name like %s"""
    actor_name = f'%{input("Введите имя или фамилию актера").upper()}%'
    cursor.execute(select, (actor_name,))
    show_films(cursor.fetchall())


base_branch()