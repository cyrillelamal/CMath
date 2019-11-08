import math


A = 0
B = 1
X0 = A
Y0 = 1

NUM_OF_SEP = [10, 50, 150]


def f(x, y):
    return y * (1 - x)


def euler():
    for n in NUM_OF_SEP:
        h = (B - A) / n
        x = X0  # x0
        y = Y0  # y0
        print(f'Шаг интегрирования: {h}')
        print(f'x0={x:.5f}; y0={y:.5f}')
        for _ in range(n):
            y += h * f(x, y)
            x += h
            print(f'{x:.5f}; {y:.5f}')


def rk(a=A, b=B, x=X0, y=Y0, h=None, func=f):
    for n in NUM_OF_SEP:
        if h is None:
            h = (b - a) / n

        print(f'Шаг интегрирования: {h}')
        print(f'x0={x:.5f}; y0={y:.5f}')
        for _ in range(n):
            k1 = h * func(x, y)
            k2 = h * func(x+h/2, y+k1/2)
            k3 = h * func(x+h/2, y+k2/2)
            k4 = h * func(x+h, y+k3)
            y += ((k1 + 2*k2 + 2*k3 + k4) / 6)
            x += h
            print(f'{x:.5f}; {y:.5f}')
        return x, y


def double():
    h = 0.1

    def y1(y, z):
        return y + h*z

    def z1(x, y, z):
        return z + h * (-(z/x + y))

    xi = 1
    yi = 0.77
    z = -0.44  # y'
    print(f'x0={round(xi, 5)}; y0={round(yi, 5)}')
    while xi <= 1.5:
        yi = y1(yi, z)
        z = z1(xi, yi, z)
        xi += h
        print(f'x={round(xi, 5)}; y={round(yi, 5)}; z={round(z, 5)}')


def system():
    def dx_dy(x, z):
        return -2*x + 5*z

    def dy_dt(t, x, y, z):
        return math.sin(t-1)*x - y - 3*z

    def dz_dt(x, z):
        return -x + 2*z

    xi = 2
    yi = 1
    zi = 1


