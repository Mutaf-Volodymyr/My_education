import argparse, os


parser = argparse.ArgumentParser() # создание экземпляра класса
parser.add_argument('-a', type=int, help='not help') # добавление ключа -a, с типом int
parser.add_argument('--bababa', type=int, help='not help') # добавление ключа --bababa, с типом int
args = parser.parse_args() # распаковка ключей в одну переменную
first = args.a # считывание данных переданных в ключ -a
second = args.bababa  # считывание данных переданных в ключ --bababa
res = str(first * second)
os.system('echo ' + res) # передача команды непосредственно в командную строку
