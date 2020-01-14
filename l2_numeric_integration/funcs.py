import math


NUMBERS_OF_STEPS = [10**2, 10**3, 10**4]

P = 5  # Precision
E = 10**(-P)  # Epsilon


# Integrated function
def func(x):
    return 2*x + 3/math.sqrt(x)  # 21


MAX = 19 / 2


def double_func(x, y):
    return math.sin(x+y)


# Deep dark backend
def trapezium_generator(a, b, h):
    # [x0; n-1]  range
    x = a + h
    while x <= b - h:
        yield func(x)
        x += h


def left_rectangles():
    a = 1
    b = 4
    for n in NUMBERS_OF_STEPS:
        s = 0
        h = (b - a) / n
        x = a
        while x <= b - h:
            s += round(func(x), P)
            x += h
        i = round(h * s, P)
        print(f'{i} для {n} шагов.')


def right_rectangles():
    a = 1
    b = 4
    for n in NUMBERS_OF_STEPS:
        s = 0
        h = (b - a) / n
        x = a + h
        while x <= b:
            s += round(func(x), P)
            x += h
        i = round(h * s, P)
        print(f'{i} для {n} шагов.')


def trapezium():
    a = 1
    b = 4
    for n in NUMBERS_OF_STEPS:
        s = 0
        h = (b - a) / n
        x = a + h
        while x <= b - h:
            s += round(func(x), P)
            x += h
        i = round(h * ((func(a) + func(b)) / 2 + s), P)
        print(f'{i} для {n} шагов.')


def parable():  # Simpson
    a = 1
    b = 4
    for n in NUMBERS_OF_STEPS:
        if n % 2 == 1:
            raise ValueError('Number of steps must be even')
        h = (a + b) / n
        h_inner = 2 * h
        odd_sum = 0
        x = a + h
        while x <= b - h:
            odd_sum += round(func(x), P)
            x += h_inner
        even_sum = 0
        x = a + h_inner
        while x <= b - h_inner:
            even_sum += round(func(x), P)
            x += h_inner
        i = round((h/3) * (func(a) + func(b) + 4*odd_sum + 2*even_sum), P)
        print(f'{i} для {n} шагов.')


def alg1():
    """Recount every integral"""
    a = 1
    b = 4
    # Остаточный член
    h = math.sqrt(E)
    n_init = int((b - a) / h)
    r = round(abs((b - a)**3 / (12 * n_init**2) * MAX), P)
    print(f'Остаточный член: {r}')

    prev_integral = h * sum(trapezium_generator(a, b, h))
    h /= 2
    n = 2 * n_init
    curr_integral = h * sum(trapezium_generator(a, b, h))

    while abs(curr_integral - prev_integral) >= E:
        # Integrate with a new step
        prev_integral = curr_integral
        h /= 2
        n *= 2
        curr_integral = h * sum(trapezium_generator(a, b, h))

    print(
        f'Начальное количество шагов: {n_init}.\n'
        f'Финальное количество шагов: {n}.\n'
        f'Результат: {round(curr_integral, P)}.'
    )


def alg2():
    a = 1
    b = 4
    # Остаточный член
    h = math.sqrt(E)
    n_init = int((b - a) / h)
    r = round(abs((b - a)**3 / (12 * n_init**2) * MAX), P)
    print(f'Остаточный член: {r}')

    # Trapezium's borders
    t_borders = (func(a) + func(b)) / 2

    hv = (b - a) / n_init  # Base step
    prev_i = round(
        hv * (t_borders + sum(trapezium_generator(a, b, hv))),
        P
    )

    hs = hv / 2  # Bias step
    hd = hv  # New step for sum: previous hv
    curr_i = round(
        hv * (t_borders + sum(trapezium_generator(a + hs, b, hd))),
        P
    )
    hv = hs  # new hv
    n = n_init * 2

    while abs(curr_i - prev_i) >= E:
        n *= 2
        prev_i = curr_i
        hs = hv / 2  # Bias step
        hd = hv  # New step for sum: previous hv
        curr_i = round(
            hv * (t_borders + sum(trapezium_generator(a + hs, b, hd)))
        )
        hv = hs  # new hv

    print(
        f'Начальное количество шагов: {n_init}.\n'
        f'Финальное количество шагов: {n}.\n'
        f'Результат: {round(curr_i, P)}.'
    )


def double_int():
    """Count multiple integral"""
    # Пределы интегрирования кратного интеграла
    a = 0
    b = math.pi / 2
    c = 0
    d = math.pi / 4
    nx = 10**3
    ny = 10**3
    hx = round((b - a) / nx, 5)
    hy = round((d - c) / ny, 5)
    print(f'Количество шагов по x={nx}, hx={hx}.\n'
          f'Количество шагов по y={ny}, hy={hy}.')
    sx = 0  # Sum for x
    x = a
    while x <= b - hx:
        sy = 0
        y = c
        while y <= d - hy:
            sy += double_func(x, y)
            y += hy
        iy = hy * sy
        sx += iy
        x += hx
    ix = round(hx * sx, 5)
    print(f'Двойной интеграл: {ix}')
