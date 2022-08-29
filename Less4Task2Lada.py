"""
Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
"""


num = int(input("Введите число: "))
i = 2
primfac = []
old = num
while i <= num:
    if not num % i:
        primfac.append(i)
        num //= i
        i = 2
    else:
        i += 1
print(f"Простые множители числа {old} приведены в списке: {primfac}")
