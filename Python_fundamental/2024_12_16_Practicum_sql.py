import os
import dotenv
from pathlib import Path
import mysql.connector


dotenv.load_dotenv(Path('.env'))
dbconfig = {'host': os.environ.get('host'),
            'user': os.environ.get('user'),
            'password': os.environ.get('password'),
            'database': os.environ.get('database')}


# В базе данных ich_edit три таблицы. Users с полями (id, name, age), Products с полями (pid, prod,
# quantity) и Sales с полями (sid, id, pid).
# Программа должна вывести все покупки каждого пользователя.


connection = mysql.connector.connect(**dbconfig)
name = input("Enter name: ")
cursor = connection.cursor()
cursor.execute(
f'''
    SELECT u.id, u.name, p.pid, p.prod, p.quantity
    FROM ich_edit.sales s 
    inner join users as u
    on u.id = s.id
    and u.name = %s
    inner join ich_edit.product p
    on s.pid = p.pid
''', (name,)
)

result = cursor.fetchall()
print(*result, sep='\n')
cursor.close()
connection.close()