# a = input()
# if len(a) % 2 == 1:
#     print('NO')
# else:
#     while '()' in a or '[]' in a or '{}' in a:
#         a = a.replace('()', '')
#         a = a.replace('[]', '')
#         a = a.replace('{}', '')
#     print('NO' if a else 'YES')


# [[()]]{[]}() True
# [[()]]{[[]}()) False


# https://t.me/inkapsul/91



def fill_student():
    print('Заполнение данных о студенте. Оставьте пустую строку')
    name = input('Введите имя студента: ')
    if not name:
        return None
    age = int(input('Введите вохраст студента: '))
    score = int(input('Введите средний балл студента: '))
    return name, age, score


def fill_students():
    students = []
    while True:
        student = fill_student()
        if student is None:
            break
        students.append(student)
    return students


def get_passed_students(students, passed_score):
    passed_students = []
    for student in students:
        if student[2] > passed_score:
            passed_students.append(student[0])

    return passed_students


avg_score = int(input('Введите пороговое значение среднего балла: ')) # 90

# students = [("Alice", 20, 90), ("Bob", 19, 80), ("Charlie", 21, 95), ("David", 18, 85)]
print(f'Студенты с средним баллом выше {avg_score} : {get_passed_students(fill_students(), avg_score)}') # ['Charlie']









