"""
1 Вычислить число π c заданной точностью d

*Пример:*

- при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$
"""

# Вариант 1


from math import pi

d = int(input("Введите точность (до 15ти знаков после запятой включительно), c которой хотите получить число Пи:\n"))
# print(f'число Пи с заданной точностью {d} равно {round(pi, d)}')
my_str = str(pi)
my_lst = []
for i in range(d + 2):
    my_lst.append(my_str[i])
my_pi = "".join(my_lst)
print(f"число Пи с заданной точностью {d} равно {my_pi}")

