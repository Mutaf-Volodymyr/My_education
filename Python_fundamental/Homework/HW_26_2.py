# 2. Напишите программу, которая принимает в качестве аргумента командной строки путь
# к директории и выводит список всех файлов и поддиректорий внутри этой директории.
# Для этой задачи используйте модуль os и его функцию walk.
# Программа должна выводить полный путь к каждому файлу и директории.

import argparse, os

parser = argparse.ArgumentParser()
parser.add_argument('--pathdir', help='Path to input file')
args = parser.parse_args()
pathdir = args.pathdir

for dir_path, dir_dir, filenames in os.walk(pathdir):
    for directory in dir_dir:
        res_dir = os.path.join(dir_path, directory)
        print('Directory: ' + res_dir)
    for filename in filenames:
        res = os.path.join(dir_path, filename)
        print('File: ' + res)
