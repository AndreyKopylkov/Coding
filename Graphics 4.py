from math import pow, abs

def f(x):
    x = (a + b) / 2
    R = f(x) = pow(x, 2) + 2 * x

# ввод значений
a = float(input('Введите начало отрезка: '))
b = float(input('Введите конец отрезка: '))
eps = float(input('Введите точность: '))
# Вычисляем значения функций f(x1), f(x2)
x1 = a + 0.382 * (b - a)
x2 = b - 0.382 * (b - a)
f(x1) = pow(x1, 2) + 2 * x1
f(x2) = pow(x2, 2) + 2 * x2
while (True):
    if (f(x1) < f(x2)):
        b = x2
    else:
        a = x1
        if (math.abs(b - a) < eps):
            return x
            return R
            print(x, R)
        else:
            if b:
                x2 = x1
                f(x2) = f(x1)
                x1 = a + 0.382 * (b - a)
                f(x1) = pow(x1, 2) + 2 * x1

            if a:
                x1 = x2
                f(x1) = f(x2)
                x2 = b - 0.382 * (b - a)
                f(x2) = pow(x2, 2) + 2 * x2