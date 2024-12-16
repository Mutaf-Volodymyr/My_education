# В базе данных ich_edit три таблицы. Users с полями (id, name, age), Products с полями (pid, prod,
# quantity) и Sales с полями (sid, id, pid).
# Программа должна вывести все покупки каждого пользователя.

import mysql.connector
dbconfig = {'host': '******',
            'user': '****',
            'password': '******',
            'database': '****'}

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


# for row in result:
#     print(row)
#
# cursor.close()
# connection.close()
#
# import mysql.connector
#

#
# # Создаем объект курсора для выполнения SQL-запросов
# cursor = conn.cursor()
# print("Подключение успешно!")
#
# # Создаем таблицу "employees" (сотрудники)
# # create_table_query = '''
# #     CREATE TABLE IF NOT EXISTS employees (
# #     employee_id INT PRIMARY KEY AUTO_INCREMENT,
# #     first_name VARCHAR(50),
# #     last_name VARCHAR(50),
# #     hire_date DATE,
# #     salary DECIMAL(10, 2)
# #     )
# # '''
#
#
# print("Таблица 'employees' создана!")
# cursor.execute(create_table_query)
#
# # Добавляем запись в таблицу "employees"
# insert_query = '''
#     INSERT INTO employees (first_name, last_name, hire_date, salary)
#     VALUES (%s, %s, %s, %s)
# '''
# data = ('Анна', 'Кузнецова', '2020-05-13', 80000.00)
#
#
# cursor.execute(insert_query, data)
# cursor.execute(
#     "INSERT INTO employees (first_name, last_name, hire_date, salary) "
#     "VALUES (%s, %s, %s, %s)",
#     ('Анна', 'Кузнецова', '2020-05-13', 80000.00)
# )
#
# conn.commit() # Сохраняем изменения








