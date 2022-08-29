"""
Задача №32: Задайте последовательность чисел.
Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
"""


lst = list(map(int, input("Введите числа через пробел:\n").split()))
dct = {}
new_lst = []
for i in lst:
    a = lst.count(i)
    dct.update({i: a})

a = 0
keys = list(dct.keys())
for i in dct:
    if dct[i] == 1:
        new_lst.append(keys[a])
        a += 1
    else:
        a += 1

print(f"Список из неповторяющихся элементов: {new_lst}")
