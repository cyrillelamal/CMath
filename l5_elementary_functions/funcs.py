from math import pi


EPSILON = 10**(-5)


def logarithm(x=0.5):
    def func(n):
        return (-1)**(n+1) * x**n / n

    s = 0  # Sum
    i = 1  # n (outer)

    add1 = func(i)
    i += 1
    add2 = func(i)

    s += add1 + add2

    while abs(add2 - add1) >= EPSILON:
        add1 = add2
        i += 1
        add2 = func(i)
        s += add2

    print(f'ln(x+1) = {s}; x=0.5')
    return s


def arctan(x=pi/6):  # 0.48234
    def arctan_generator(n=1):
        while True:
            yield x**n / n
            n += 2
            yield -(x**n / n)
            n += 2

    gen = arctan_generator()
    add1 = next(gen)
    add2 = next(gen)
    s = add1 + add2

    while abs(add2 - add1) >= EPSILON:
        add1 = add2
        add2 = next(gen)
        s += add2

    print(f'arctg(x) = {s}; x=pi/6')
    return s
