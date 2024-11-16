from argparse import ArgumentParser
import os


def convert_bytes(size):
    if size < 1000:
        return f'{size} B'
    elif 1000 <= size < 1000000:
        return f'{round(size / 1024)} KB'
    elif 1000000 <= size < 1000000000:
        return f'{round(size / 1048576)} MB'
    else:
        return f'{round(size / 1073741824)} GB'


parser = ArgumentParser()  # создание экземпляра класса
parser.add_argument('--path', '-p', help='input path to find')
parser.add_argument('--type', '-t', help='input type (.py)', default='py')
parser.add_argument('--size', '-s', type=int, help='input min size', default=0)
args = parser.parse_args()  # распаковка ключей в одну переменную

total = 0

for root, directories, files in os.walk(args.path):
    for filename in files:
        if filename.endswith(args.type):
            full_path = os.path.join(root, filename)
            size = int(os.path.getsize(full_path))
            if size >= args.size:
                total += size
                print(f'{convert_bytes(size)} : {full_path}')

print(f'Total size: {convert_bytes(total)}')
