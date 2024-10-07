# Напишите программу, которая принимает список слов и возвращает список, содержащий только анаграммы.

def anogramm_filter(li:list):
    li_sort = list({''.join(sorted(i)) for i in li})
    res = [[] for i in range(len(li_sort))]
    for el in li:
        k = ''.join(sorted(el))
        i = li_sort.index(k)
        res[i].append(el)
    return res

print(anogramm_filter(['cat', 'dog', 'tac', 'god', 'act']))


# Решение здорового человека (без множеств)
def anogramm_filter2(li:list):
    li_sort = {}
    for el in li:
        key = ''.join(sorted(el))
        li_sort[key] = li_sort.get(key, []) + [el]
    return [i for i in li_sort.values()]

print(anogramm_filter2(['cat', 'dog', 'tac', 'god', 'act']))


# Напишите функцию is_subset, которая принимает два множества set1 и set2 и проверяет,
# является ли set1 подмножеством set2. Функция должна возвращать True, если все элементы
# из set1 содержатся в set2, и False в противном случае. Функция должна быть реализована
# без использования встроенных методов issubset или <=.

def is_subset(set1, set2):
    for i in set1:
        if i not in set2:
            return False
    return True


print(is_subset({'a', 'b', 'c'}, {'a', 'b', 'c', 'd', 'e'}))


