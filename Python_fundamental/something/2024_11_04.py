from functools import reduce
d = {23:1, 65:2, 45:56, 43:36}
print(reduce(lambda x, y: x * y[1], d.items(), 0))

