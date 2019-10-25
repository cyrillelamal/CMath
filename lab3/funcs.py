import math


A = 0
B = 1

X0 = A
Y0 = 1

NUM_OF_SEP = [10, 50, 150]


def func(x, y):
    return y * (1 - x)


def euler():
    for n in NUM_OF_SEP:
        h = (B - A) / n
        x = X0  # x0
        y = Y0  # y0
        print(f'Шаг интегрирования: {h}')
        print(f'x0={x:.5f}; y0={y:.5f}')
        for _ in range(n):
            y += h * func(x, y)
            x += h
            print(f'{x:.5f}; {y:.5f}')


def rk():
    for n in NUM_OF_SEP:
        h = (B - A) / n
        x = X0
        y = Y0
        print(f'Шаг интегрирования: {h}')
        print(f'x0={x:.5f}; y0={y:.5f}')
        for i in range(n):
            k1 = h * func(x, y)
            k2 = h * func(x+h/2, y+k1/2)
            k3 = h * func(x+h/2, y+k2/2)
            k4 = h * func(x+h, y+k3)
            y += ((k1 + 2*k2 + 2*k3 + k4) / 6)
            x += h
            print(f'{x:.5f}; {y:.5f}')
