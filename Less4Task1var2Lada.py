"""
1 Вычислить число π c заданной точностью d

*Пример:*

- при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$
"""

# Вариант 2


def nikalant_row(e):
    pi, sign, m = 3, 1, 2
    while abs(pi - (pi + sign*4/(m**3+3*m**2+2*m))) > 10**(-d-1):
        pi = pi + sign*4/(m**3+3*m**2+2*m)
        sign = -1*sign
        m = m+2
    return (pi + (pi + sign*4/(m**3+3*m**2+2*m)))/2


d = int(input("Введите точность (до 15ти знаков после запятой включительно), c которой хотите получить число Пи:\n"))
mypi = nikalant_row(d)
print(f"Число Пи с заданной точностью {d} равно {round(mypi, d)}")
