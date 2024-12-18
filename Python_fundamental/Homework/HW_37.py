# В базе данных ich_edit три таблицы. Users с полями (id, name, age),
# Products с полями (pid, prod, quantity) и Sales с полями (sid, id, pid).
# Программа должна запросить у пользователя название таблицы
# и вывести все ее строки или сообщение, что такой таблицы нет.

# import os
# import dotenv
# from pathlib import Path
# import mysql.connector
#
#
# dotenv.load_dotenv(Path('../.env'))
# dbconfig = {'host': os.environ.get('host'),
#             'user': os.environ.get('user'),
#             'password': os.environ.get('password'),
#             'database': 'ich_edit'}
#
# connection = mysql.connector.connect(**dbconfig)
# cursor = connection.cursor()
# cursor.execute('SHOW TABLES')
# tables_dict = dict(enumerate(map(lambda x: x[0], cursor.fetchall()), 1))
# print('Hi. I have the following tables and can show you one of them.')
# for k, v in tables_dict.items():
#     print(f'{k}: {v}')
# choice = int(input('Enter a number: '))
#
# cursor.execute(
# f'''
#     SELECT *
#     FROM ich_edit.{tables_dict[choice]}
# ''')
#
# result = cursor.fetchall()
# print(*result, sep='\n')
# cursor.close()
# connection.close()
#


# В базе данных ich_edit три таблицы. Users с полями (id, name, age), Products с полями (pid, prod, quantity) и Sales с полями (sid, id, pid).
# Программа должна вывести все имена из таблицы users, дать пользователю выбрать одно из них и вывести все покупки этого пользователя.


import os
import dotenv
from pathlib import Path
import mysql.connector


dotenv.load_dotenv(Path('../.env'))
dbconfig = {'host': os.environ.get('host'),
            'user': os.environ.get('user'),
            'password': os.environ.get('password'),
            'database': 'ich_edit'}

connection = mysql.connector.connect(**dbconfig)
cursor = connection.cursor()

cursor.execute(
'''
    SELECT id, name
    FROM ich_edit.users
''')

person_dict = {k: v for k, v in cursor.fetchall()}
for k, v in person_dict.items():
    print(f'{k}: {v}')
name = int(input('Enter a person ID: '))

cursor.execute(
'''
    SELECT u.id, u.name, p.pid, p.prod, p.quantity
    FROM ich_edit.sales s 
    inner join users as u
    on u.id = s.id
    and u.id = %s
    inner join ich_edit.product p
    on s.pid = p.pid
''', (name,)
)
result = cursor.fetchall()
print(*result, sep='\n')

cursor.close()
connection.close()
