import math


A = 0
B = 1
X0 = A
Y0 = 1

NUM_OF_STEP = [10, 50, 150]


def euler():
    def f(x, y):
        return y * (1 - x)

    a = 0
    b = 1

    for n in NUM_OF_STEP:
        h = (b - a) / n
        xi = a  # [0; 1]
        yi = 1  # y(0)=1
        print(f'Шаг интегрирования: {h}')
        print(f'x0={xi:.5f}; y0={yi:.5f}')
        for _ in range(n):
            yi += h * f(xi, yi)
            xi += h
            print(f'x={xi:.5f}; y={yi:.5f}')


def rk():
    def f(x, y):
        return y * (1 - x)

    a = 0
    b = 1

    for n in NUM_OF_STEP:
        h = (b - a) / n
        xi = a
        yi = 1
        print(f'Шаг интегрирования: {h}')
        print(f'x0={xi:.5f}; y0={yi:.5f}')
        for _ in range(n):
            k1 = h * f(xi, yi)
            k2 = h * f(xi+h/2, yi+k1/2)
            k3 = h * f(xi+h/2, yi+k2/2)
            k4 = h * f(xi+h, yi+k3)
            yi += ((k1 + 2*k2 + 2*k3 + k4) / 6)
            xi += h
            print(f'x={xi:.5f}; y={yi:.5f}')


def double():
    h = 0.1

    def y1(y, z):
        return y + h*z

    def z1(x, y, z):
        return z + h * (-(z/x + y))

    xi = 1
    yi = 0.77
    zi = -0.44  # y'
    print(f'x0={round(xi, 5)}; y0={round(yi, 5)}; z0={round(zi, 5)}')
    while xi <= 1.5:
        zi = z1(xi, yi, zi)
        yi = y1(yi, zi)
        xi += h
        print(f'x={round(xi, 5)}; y={round(yi, 5)}; z={round(zi, 5)}')


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
