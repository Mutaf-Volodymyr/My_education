Запуск файла пайтон в командной строке
> python print.py -a 3 -b 4
- `python` - это язык программирования который должен запустить файл
- `print.py`  - путь к файлу (относительный или абсолютный)
- `-a` - ключ который мы заранее задали в самом файле `print.py`
- `-b` - ключ который мы заранее задали в самом файле `print.py`
- `3 и 4` - свободные данный, которые примет программа для дальнейшей обработки
> все что указано после названия файла называется "Аргументы командной строки"

сам файл `print.py` имеет следующее содержание:
    
    import argparse, os

    parser = argparse.ArgumentParser()      # создание экземпляра класса
    parser.add_argument('-a', type=int, help='not help')        # добавление ключа -a, с типом int
    parser.add_argument('--bababa', type=int, help='not help')      # добавление ключа --bababa, с типом int
    args = parser.parse_args()      # распаковка ключей в одну переменную
    first = args.a      # считывание данных переданных в ключ -a
    second = args.bababa        # считывание данных переданных в ключ --bababa
    res = str(first * second) 
    os.system('echo ' + res)    # передача команды непосредственно в командную строку 

этот код соберет все "Аргументы командной строки" в один список

    import sys 
    print(sys.argv)


