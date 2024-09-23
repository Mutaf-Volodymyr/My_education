################# ЗАДАЧИ ##########################
# #
# import json
# lines = {
#          True: 97,
#          2: "I've been running for a reason",
#          "3": ("I", "could", "never", "retain"),
#          4: ["Sweet", "lips", "like", "pink", "lemonade"],
#          5.0: "When he's feeling generous he's gonna give me a taste",
#          "six": "10"
#         }
# lines_json = json.dumps(lines)
# lines = json.loads(lines_json)
# print(lines)


# -----------------------------------------
# import json
# colors = ['black', 'white']
# colors_json = json.dumps(colors, indent='-> ')
# print(colors_json)


# -----------------------------------------
# Дополните приведенный ниже код, чтобы он вывел содержимое словаря countries, расположив его элементы в
# лексикографическом порядке ключей, указав в качестве разделителя элементов , (запятая без пробела),
# в качестве разделителя пар ключ-значение — строку   -  (пробел дефис пробел), а в качестве отступов — три пробела.
#
# import json
# countries = {'Monaco': 'Monaco', 'Iceland': 'Reykjavik', 'Kenya': 'Nairobi', 'Kazakhstan': 'Nur-Sultan',
#              'Mali': 'Bamako', 'Colombia': 'Bogota', 'Finland': 'Helsinki', 'Costa Rica': 'San Jose',
#              'Cuba': 'Havana', 'France': 'Paris', 'Gabon': 'Libreville', 'Liberia': 'Monrovia',
#              'Angola': 'Luanda', 'India': 'New Delhi', 'Canada': 'Ottawa', 'Australia': 'Canberra'}
# json_var = json.dumps(countries, indent=3, separators=(',', ' - '), sort_keys=True)
# print(json_var)

# -----------------------------------------
# Дополните приведенный ниже код, чтобы он преобразовал словарь words в строку в формате JSON, пропуская пары,
# которые имеют недопустимые ключи, и присвоил полученный результат переменной data_json.

# import json
#
# words = {
#          frozenset(["tap", "telephone"]): ("tæp", "telifəun"),
#          "travel": "trævl",
#          ("hello", "world"): ("həˈləʊ", "wɜːld"),
#          "moonlight": "muːn.laɪt",
#          "sunshine": "ˈsʌn.ʃaɪn",
#          ("why", "is", "so", "difficult"): ("waɪ", "ɪz", "səʊ", "ˈdɪfɪkəlt"),
#          "adventure": "ədˈventʃər",
#          "beautiful": "ˈbjuːtɪfl",
#          frozenset(["spoon", "block"]): ("spu:n", "blɔk"),
#          "bicycle": "baisikl",
#          ("pilot", "fly"): ("pailət", "flai")
#         }
#
# data_json = json.dumps(words, skipkeys=True)


# -----------------------------------------
# Вам доступны словари club1, club2 и club3, содержащие данные о различных футбольных клубах.
# Дополните приведенный ниже код, чтобы он объединил данные словари в список и записал полученную
# структуру данных в файл data.json, указав в качестве отступов три символа пробела.
#
# import json
#
# club1 = {"name": "FC Byern Munchen", "country": "Germany", "founded": 1900,
#          "trainer": "Julian Nagelsmann", "goalkeeper": "M. Neuer", "league_position": 1}
#
# club2 = {"name": "FC Barcelona", "country": "Spain", "founded": 1899,
#          "trainer": "Xavier Creus", "goalkeeper": "M. Ter Stegen", "league_position": 7}
#
# club3 = {"name": "FC Manchester United", "country": "England", "founded": 1878,
#          "trainer": "Michael Carrick", "goalkeeper": "D. De Gea", "league_position": 8}
#
# with open('json_1/data.json', 'w') as outfile:
#     json.dump([club1, club2, club3], outfile, indent=3)


# -----------------------------------------
# Ниже представлена программа, которая должна преобразовать словарь specs в строку в формате JSON
# и вывести ее с отступами в три пробела, не заменяя кириллические символы на их коды. В программе допущена ошибка.
# Найдите и исправьте ее, чтобы программа преобразовала словарь specs в строку в формате JSON и вывела ее с отступами
# в три пробела, не заменяя кириллические символы на их коды.

# import json
# specs = {
#          'Модель': 'AMD Ryzen 5 5600G',
#          'Год релиза': 2021,
#          'Сокет': 'AM4',
#          'Техпроцесс': '7 нм',
#          'Ядро': 'Cezanne',
#          'Объем кэша L2': '3 МБ',
#          'Объем кэша L3': '16 МБ',
#          'Базовая частота': '3900 МГц'
#         }
# specs_json = json.dumps(specs, ensure_ascii=False, indent=3)
# print(specs_json)


# -----------------------------------------
# Реализуйте функцию is_correct_json(), которая принимает один аргумент:
# string — произвольная строка
# Функция должна возвращать True, если строка string удовлетворяет формату JSON, или False в противном случае.

# def is_correct_json(string):
#     import json
#     try:
#         data = json.loads(string)
#         return True
#     except ValueError:
#         return False


# -----------------------------------------
# Напишите программу, которая принимает на вход описание одного объекта в формате JSON и выводит все пары ключ-значение этого объекта.
    # Формат входных данных
 # На вход программе подается корректное описание одного объекта в формате JSON.
    # Формат выходных данных
# Программа должна вывести все пары ключ-значение введенного объекта, разделяя ключ и значение двоеточием, каждую на отдельной строке. Если значением ключа является список, то все его элементы должны быть выведены через запятую.


# import sys
# import json
#
# data = json.loads(sys.stdin.read())
#
# for key, value in data.items():
#     if isinstance(value, list):
#         print(f'{key}: {", ".join(map(str, value))}')
#     else:
#         print(f'{key}: {value}')



# -----------------------------------------
# Вам доступен файл data.json, содержащий список различных объектов.
# Напишите программу, которая создает список, элементами которого являются объекты из списка, содержащегося в файле data.json, измененные по следующим правилам:
#     если объект является строкой, в его конец добавляется восклицательный знак
#     если объект является числом, он увеличивается на единицу
#     если объект является логическим значением, он инвертируется
#     если объект является списком, он удваивается
#     если объект является JSON-объектом (словарем), в него добавляется новая пара "newkey": null
#     если объект является пустым значением (null), он не добавляется
# Полученный список программа должна записать в файл updated_data.json.

# import json
#
# with open('json_1/data_1.json', 'r') as file, open('json_1/pdated_data.json', 'w') as outfile:
#     res = []
#     for i in json.load(file):
#         if type(i) == str:
#             res.append(i+'!')
#         elif type(i) == int:
#             res.append(i+1)
#         elif type(i) == bool:
#             res.append(not i)
#         elif type(i) == list:
#             res.append(i+i)
#         elif type(i) == dict:
#             i["newkey"] = None
#             res.append(i)
#         elif i is None:
#             continue
#         else:
#             res.append(i)
#     outfile.write(json.dumps(res, indent=3))



# updated_data = []
# for value in data_json:
#     match value:
#         case str(): value += '!'
#         case bool(): value = not value
#         case int(): value += 1
#         case list(): value *= 2
#         case dict(): value["newkey"] = None
#         case None: continue
#     updated_data.append(value)
#
# with open('updated_data.json', 'w', encoding='utf-8') as file:
#     json.dump(updated_data, file)

# -----------------------------------------
# Вам доступны два файла data1.json и data2.json, каждый из которых содержит по единственному JSON-объекту.
# Напишите программу, которая объединяет два данных JSON-объекта в один JSON-объект, причем если пары из первого
# и второго объектов имеют совпадающие ключи, то значение следует взять из второго объекта.
# Полученный JSON-объект программа должна записать в файл data_merge.json.

# import json
# with (open('json_1/data1.json', 'r') as file1,
#       open('json_1/data2.json', 'r') as file2,
#       open('json_1/data_merge.json', 'w') as outfile):
#     res = json.load(file1) | json.load(file2)
#     outfile.write(json.dumps(res, indent=3))

# -----------------------------------------
# Вам доступен файл people.json, содержащий список JSON-объектов. Причем у различных объектов может
# быть различное количество ключей.
# Напишите программу, которая добавляет в каждый JSON-объект из данного списка все недостающие ключи,
# присваивая этим ключам значение null. Ключ считается недостающим, если он присутствует в каком-либо
# другом объекте, но отсутствует в данном. Программа должна создать список с обновленными JSON-объектами
# и записать его в файл updated_people.json.

# import json
# with open('json_1/people.json', 'r') as file, open('json_1/updated_people.json', 'w') as outfile:
#     res = json.load(file)
#     all_keys = set()
#     for i in res:
#         all_keys = all_keys | set(i.keys())
#     for d in res:
#         for j in all_keys:
#             d.setdefault(j, None)
#     outfile.write(json.dumps(res, indent=3))
#
#
# import json
#
# with open('people.json', encoding='utf8') as fi, open('updated_people.json', 'w') as fo:
#     people = json.load(fi)
#     d = {k: None for i in people for k in i.keys()}
#     json.dump([d | i for i in people], fo)


# -----------------------------------------

# Вам доступен файл countries.json, содержащий список JSON-объектов c информацией о странах и исповедуемых в них религиях:
# Каждый объект из этого списка содержит два атрибута:
# country — страна
# religion — исповедуемая религия
# Напишите программу, которая создает единственный JSON-объект,
# имеющий в качестве ключа название религии, а в качестве значения — список стран, в которых исповедуется данная религия.
# Полученный JSON-объект программа должна записать в файл religion.json.

# import json
# with open('json_1/countries.json', 'r', encoding='utf8') as file, open('json_1/religion.json', 'w') as outfile:
#     data = json.load(file)
#     religion_set = {i:[] for i in {i['religion'] for i in data}}
#     for i in data:
#         religion_set[i['religion']].append(i['country'])
#     outfile.write(json.dumps(religion_set, indent=3))
#
#
# import json
# with open("countries.json") as file_in, open("religion.json", "w") as file_out:
#     d = {}
#     datas = json.load(file_in)
#     for data in datas:
#         d[data['religion']] = d.get(data['religion'], []) + [data['country']]
#     json.dump(d, file_out)


# -----------------------------------------
# Вам доступен файл playgrounds.csv с информацией о спортивных площадках Москвы. В первом столбце записан
# тип площадки,  во втором — административный округ, в третьем — название района, в четвертом — адрес:
#
    # ObjectName;AdmArea;District;Address
# Напишите программу, создающую JSON-объект, ключом в котором является административный округ,
# а значением — JSON-объект, в котором, в свою очередь, ключом является название района,
# относящийся к этому административному округу, а значением — список адресов всех площадок в этом районе.
# Полученный JSON-объект программа должна записать в файл addresses.json.

# import json
# import csv
#
# with open('json_1/playgrounds.csv', encoding='utf8') as file, open('json_1/addresses.json', 'w', encoding='utf8') as outfile:
#     data = csv.DictReader(file, delimiter=';')
#     mydict = {}
#     for row in data:
#         mydict.setdefault(row['AdmArea'], {}).setdefault(row['District'], []).append(row['Address'])
#     json.dump(mydict, outfile, ensure_ascii=False)










