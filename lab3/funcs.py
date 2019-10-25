import math


A = 0
B = 1
X0 = A
Y0 = 1

NUM_OF_SEP = [10, 50, 150]


def equation(x, y):
    return y * (1 - x)


def euler():
    for n in NUM_OF_SEP:
        h = (B - A) / n
        x = X0  # x0
        y = Y0  # y0
        print(f'Шаг интегрирования: {h}')
        print(f'x0={x:.5f}; y0={y:.5f}')
        for _ in range(n):
            y += h * equation(x, y)
            x += h
            print(f'{y:.5f}')


def runge():
    pass
