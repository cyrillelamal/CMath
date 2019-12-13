from math import pi, pow


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
    s = round(s, 5)
    print(f'ln(x) = {s}, x = 0,5')


def logarithm_cheb(x=0.5):
    # Коэффициенты Чебышева
    a = [0.9974442, -0.471289, 0.2256685, -0.0587527]

    s = sum(
        a[n] * pow(x, n+1) for n in range(len(a))
    )
    s = round(s, 5)

    print(f'ln(x) = {s}, x=0.5 (Чебышев)')
    return s


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
    s = round(s, 5)

    print(f'arctg(x) = {s}; x=pi/6')
    return s


def arctan_cheb(x=pi/6):
    a = [
        0.9999999953, -0.3333329248, 0.199989259, -0.1427243942, 0.1101791217,
        -0.0867899197, 0.0647029924, -0.0411720745, 0.0197433754, -0.0060738765,
        0.0008766095
    ]

    s = sum(a[n] * pow(x, 2*n+1) for n in range(len(a)))
    s = round(s, 5)

    print(f'arctg(x) = {s}; x=pi/6 (Чебышев)')
    return s
