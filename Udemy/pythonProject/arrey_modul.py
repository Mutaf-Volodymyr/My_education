from array import array

my_int_array = array('i', [4, 5, 5, 6, 10, 56]) # i ist nur int
# my_int_array.append(7)
# print(my_int_array)
# # my_int_array.append('fhdndc') # not add
# print(my_int_array.count(5))
# print(my_int_array.index(56))



with open("arrey_modul.bin", "wb") as arrey_file:
    my_int_array.tofile(arrey_file)


imported_arrey = array("i")

with open("arrey_modul.bin", "rb") as arrey_file:
    imported_arrey.fromfile(arrey_file, 3)
    print(imported_arrey)

imported_arrey.reverse()
print(imported_arrey)