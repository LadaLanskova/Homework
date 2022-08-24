"""
Дано число. Составить список чисел Фибоначчи,
в том числе для отрицательных индексов

Пример:
- для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
"""


def get_fibonacci(n):
    fibo_plus = []
    a, b = 1, 1
    for i in range(n):
        fibo_plus.append(a)
        a, b = b, a + b
    fibo_minus = []
    a, b = 0, 1
    for i in range(n+1):
        fibo_minus.append(a)
        a, b = b, a - b
    fibo_minus.reverse()
    fibo_minus.extend(fibo_plus)
    return fibo_minus

n = int(input("Введите число: \n"))
print("Список чисел Фибоначи: ", get_fibonacci(n))
