# 1. Напишите программу, которая принимает в качестве аргумента командной строки путь к файлу .py
# и запускает его. При запуске файла программа должна выводить сообщение "Файл <имя файла> успешно запущен".
# Если файл не существует или не может быть запущен, программа должна вывести соответствующее сообщение об ошибке.


import argparse, os

parser = argparse.ArgumentParser()
parser.add_argument('--name', help='Path to input file')
args = parser.parse_args()
name = args.name
if not name.endswith('.py'):
    os.system('echo "I only know how to run .py files"')
elif not os.path.isfile(name):
   os.system('echo "Wrong path"')
else:
    os.system(f'echo "File {name} has been successfully launched. But that is not certain..."')



