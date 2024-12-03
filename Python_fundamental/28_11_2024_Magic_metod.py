

# 'name' + 1 # can only concatenate str (not "int") to str

# 1 + 'name' # unsupported operand type(s) for +: 'int' and 'str'

print(dir('name'))
print(dir(1))


class NewInteger(int):
    def __init__(self, value):
        self.value = value
        self.haha = 5

    def __add__(self, other):
        return self.value + len(other)

    def __radd__(self, other):
        return self.value + len(other)

    def __eq__(self, other):
        return

    def __len__(self):
        return 5


a = NewInteger(6)
b = NewInteger(6)
print(a != b)


