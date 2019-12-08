from math import pi


EPSILON = 10**(-5)


def logarithm(x=0.5):  # 0.405465
    def log_generator(n=1):
        while True:
            yield x**n / n
            n += 1
            yield -(x**n / n)
            n += 1

    gen = log_generator()
    yp = next(gen)  # precedent
    yc = next(gen)  # current
    s = yp + yc  # sum

    while abs(yc - yp) >= EPSILON:
        yp = yc
        yc = next(gen)
        s += yc

    print(f'ln(x) = {s}, x = 0,5')


def arctan(x=pi/6):  # 0.48234
    def arctan_generator(n=1):
        while True:
            yield x**n / n
            n += 2
            yield -(x**n / n)
            n += 2

    gen = arctan_generator()
    yp = next(gen)  # precedent
    yc = next(gen)  # current
    s = yp + yc  # sum

    while abs(yc - yp) >= EPSILON:
        yp = yc
        yc = next(gen)
        s += yc

    print(f'arctg(x) = {s}; x=pi/6')
    return s
