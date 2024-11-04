# Часы показывают время в формате HH:MM:SS. На этих часах запустили таймер, который прозвенит через
# n секунд. Напишите программу, которая определит, какое время будет на часах, когда прозвенит таймер.

# from datetime import timedelta, datetime
#
#
# start_time = datetime.strptime(input(), '%H:%M:%S')
# sec = timedelta(seconds=int(input()))
# final_time = start_time + sec
# print(final_time.strftime('%H:%M:%S'))

# Напишите программу, которая определяет даты, в которые Артуру нужно подготовить задачи.

# from datetime import timedelta, datetime
# pattern = '%d.%m.%Y'
# start_date = datetime.strptime(input(), '%d.%m.%Y')
# print(start_date.strftime(pattern))
# for i in range(2, 11):
#     start_date = start_date + timedelta(days=i)
#     print(start_date.strftime(pattern))

# Дана последовательность дат. Напишите программу, которая создает и выводит список, элементами которого являются
# неотрицательные целые числа — количество дней между двумя соседними датами последовательности.

# from datetime import timedelta, datetime
#
# pattern = '%d.%m.%Y'
# date_list = [datetime.strptime(d, pattern) for d in input().split()]
# delta_list = [abs(d1 - d2).days for d1, d2 in zip(date_list, date_list[1:])]
# print(delta_list)

# Реализуйте функцию fill_up_missing_dates(), которая принимает на вход один аргумент:
#
# dates — список строковых дат в формате DD.MM.YYYY
# Функция должна возвращать список, в котором содержатся все даты из списка dates, расположенные в порядке возрастания, а также все недостающие промежуточные даты.

# from datetime import timedelta, datetime
# def fill_up_missing_dates(dates: list[str]) -> list[str]:
#     pattern = '%d.%m.%Y'
#     new_dates = [datetime.strptime(d, pattern) for d in dates]
#     min_date = min(new_dates)
#     max_date = max(new_dates)
#     final_list = []
#     while max_date >= min_date:
#         final_list.append(datetime.strftime(min_date, '%d.%m.%Y'))
#         min_date = min_date + timedelta(days=1)
#     return final_list


# Репетитор по математике проводит занятия по 45 минут с перерывами по
# 10 минут. Репетитор обозначает время начала рабочего дня и время окончания рабочего дня.
# Напишите программу, которая генерирует и выводит расписание занятий.

# from datetime import timedelta, datetime
# pattern = '%H:%M'
# start_time = datetime.strptime(input(), pattern)
# finish_time = datetime.strptime(input(), pattern)
# lesson_delta = timedelta(minutes=45)
# frei_delta = timedelta(minutes=10)
#
# while True:
#     end_lesson = start_time + lesson_delta
#     if end_lesson > finish_time:
#         break
#     print(f'{start_time.strftime('%H:%M')} - {end_lesson.strftime('%H:%M')}')
#     start_time = end_lesson + frei_delta


# Дополните приведенный ниже код, чтобы он вывел общее целое количество минут, которое программист затратил на решение всех задач.
# from datetime import date, time, datetime, timedelta
# data = [('07:14', '08:46'),
#         ('09:01', '09:37'),
#         ('10:00', '11:43'),
#         ('12:13', '13:49'),
#         ('15:00', '15:19'),
#         ('15:58', '17:24'),
#         ('17:57', '19:21'),
#         ('19:30', '19:59')]
#
# total = 0
# pattern = '%H:%M'
# for start, end in data:
#     diff = datetime.strptime(end, '%H:%M') - datetime.strptime(start, '%H:%M')
#     total += diff.total_seconds()
#
# print(int(total // 60))


# Докажите, что 13-е число месяца чаще всего приходится на пятницу. Напишите программу,
# которая вычисляет, сколько тринадцатых чисел приходится на каждый день недели в период с 01.01.0001 по 31.12.9999.

# from datetime import date
# from itertools import product
#
# count = {}
# start = date(day=13, month=1, year=1)
# finish = date(day=14, month=12, year=9999)
# for d, i in product(range(1, 10000), range(1, 13)):
#     start = start.replace(month=i, year=d)
#     week = date.weekday(start)
#     count[week] = count.get(week, 0) + 1
#     if start > finish:
#         break
#
# for _, i in sorted(count.items()):
#     print(i)


# Напишите программу, которая принимает на вход текущие дату и время и определяет количество минут, оставшееся до закрытия магазина.
# from datetime import datetime, timedelta, time
#
# schedule = {
#     'Mon': {'start': timedelta(hours=9), 'end': timedelta(hours=21)},
#     'Tue': {'start': timedelta(hours=9), 'end': timedelta(hours=21)},
#     'Wed': {'start': timedelta(hours=9), 'end': timedelta(hours=21)},
#     'Thu': {'start': timedelta(hours=9), 'end': timedelta(hours=21)},
#     'Fri': {'start': timedelta(hours=9), 'end': timedelta(hours=21)},
#     'Sat': {'start': timedelta(hours=10), 'end': timedelta(hours=18)},
#     'Sun': {'start': timedelta(hours=10), 'end': timedelta(hours=18)}
#     }
#
# pattern = '%d.%m.%Y %H:%M'
# today = datetime.strptime(input(), pattern)
# week_day = today.strftime('%a')
# start = today.replace(hour=0, minute=0) + schedule[week_day]['start']
# end = today.replace(hour=0, minute=0) + schedule[week_day]['end']
#
# if end > today >= start:
#     print(int((end - today).total_seconds() // 60))
# else:
#     print('Магазин не работает')


# Даны две даты — левая и правая границы диапазона соответственно. Напишите программу,
# которая из этого диапазона, включая границы, выводит, начиная с даты, у которой сумма
# дня и месяца нечетная, каждую третью дату, только если она не понедельник и не четверг.

# from datetime import datetime, timedelta
# pattern = '%d.%m.%Y'
# start = datetime.strptime(input(), pattern)
# end = datetime.strptime(input(), pattern)
# while True:
#     if (start.day + start.month) % 2:
#         break
#     else:
#         start = start + timedelta(days=1)
# while end >= start:
#     if start.weekday() not in (0, 3):
#         print(start.strftime(pattern))
#     start = start + timedelta(days=3)


# Дан список сотрудников организации, в котором указаны их фамилии,
# имена и даты рождения. Напишите программу, которая определяет
# самого старшего сотрудника из данного списка.

# from datetime import datetime
# pattern = '%d.%m.%Y'
# res = {}
# for _ in range(int(input())):
#     name, surname, birthday = input().split()
#     birthday = datetime.strptime(birthday, pattern)
#     res[birthday] = res.get(birthday, []) + [f'{name} {surname}']
#
# min_birthday = min(res.items())
# if len(min_birthday[1]) == 1:
#     print(f'{min_birthday[0].strftime(pattern)} {min_birthday[1][0]}')
# else:
#     print(f'{min_birthday[0].strftime(pattern)} {len(min_birthday[1])}')


# Дан список сотрудников организации, в котором указаны их фамилии, имена и даты рождения.
# Напишите программу, которая определяет, в какую из дат родилось больше всего сотрудников.

# from datetime import datetime
# pattern = '%d.%m.%Y'
# res = {}
# for _ in range(int(input())):
#     name, surname, birthday = input().split()
#     birthday = datetime.strptime(birthday, pattern)
#     res[birthday] = res.get(birthday, []) + [f'{name} {surname}']
#
# min_birthday = len(max(res.items(), key=lambda x: len(x[1]))[1])
# min_birthdays = filter(lambda x: len(x[1]) == min_birthday, res.items())
# for i, _ in sorted(min_birthdays):
#     print(i.strftime('%d.%m.%Y'))


# Дан список сотрудников организации, в котором указаны их фамилии, имена и даты рождения.
# Напишите программу, которая определяет самого молодого сотрудника,
# празднующего свой день рождения в течение ближайших семи дней от текущей даты.

# from datetime import datetime, timedelta
# pattern = '%d.%m.%Y'
#
# todey = datetime.strptime(input(), pattern)
# next_days = todey + timedelta(days=7)
#
# res = []
# for _ in range(int(input())):
#     name, surname, birthday = input().split()
#     birthday = datetime.strptime(birthday, pattern)
#     if next_days >= birthday.replace(year=todey.year) > todey or next_days >= birthday.replace(year=(todey.year+1)) > todey:
#         res.append((birthday, name, surname))
#
#
# if not res:
#     print('Дни рождения не планируются')
# else:
#     mx = max(res, key=lambda x: x[0])
#     print(*mx[1:])


# оманда BEEGEEK планирует выпустить свой новый курс 08.11.2022 ровно в 12:00.
# Напишите программу, которая принимает на вход текущие дату и время и
# определяет, сколько времени осталось до выхода курса.

from datetime import datetime, timedelta


def plural(days: int, what:str):
    plural_dict = {'d': ("день", "дня", "дней"),
                   'h': ("час", "часа", "часов"),
                   'm': ("минута", "минуты", "минут")}
    if days % 10 == 1 and days % 100 != 11:
        return f"{days} {plural_dict[what][0]}"
    elif 2 <= days % 10 <= 4 and (days % 100 < 10 or days % 100 >= 20):
        return f"{days} {plural_dict[what][1]}"
    return f"{days} {plural_dict[what][2]}"


pattern = '%d.%m.%Y %H:%M'
new_kurs = datetime(year=2022, month=11, day=8, hour=12, minute=00)
todey = datetime.strptime(input(), pattern)

if todey >= new_kurs:
    print('Курс уже вышел!')
else:
    delta = new_kurs - todey
    hours = delta.seconds // 3600
    minutes = (delta.seconds // 60) % 60
    days = delta.days
    print('До выхода курса осталось: ', end='')
    if days:
        print(plural(days, 'd'), end='')
        if hours:
            print(f' и {plural(hours, 'h')}')
    else:
        if hours:
            print(plural(hours, 'h'), end='')
            if minutes:
                print(' и ', end='')
                print(plural(minutes, 'm'))
        else:
            print(plural(minutes, 'm'))




