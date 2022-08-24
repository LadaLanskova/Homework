"""
Напишите программу, которая найдёт произведение пар чисел списка.
Парой считаем первый и последний элемент, второй и предпоследний и т.д.
Пример:
[2, 3, 4, 5, 6] => [12, 15, 16];
[2, 3, 5, 6] => [12, 15]
"""


def mult(a):
    d = len(lst) / 2
    if d % 2 != 0:
        d = int(len(lst) / 2 + 1)
    else:
        d = int(len(lst) / 2)
    lst1 = []
    for i in range(int(d)):
        p = lst[i]*lst[len(lst)-i-1]
        lst1.append(p)
    return lst1


lst = list(map(int, input("Введите элементы списка (целые числа) через пробел:\n").split()))
print(mult(lst))
