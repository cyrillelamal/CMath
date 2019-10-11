import math


# USER'S DEFINITIONS

# Edges
A = 1
B = 4

A2 = 0
B2 = math.pi/2
C2 = 0
D2 = math.pi/4


# Integrated function
def func(x):
    return 2*x + 3/math.sqrt(x)  # 21


def double_func(x, y):
    return math.sin(x+y)


# Function maximum
MAX = 19 / 2

# Constant steps
X_NUMBER_OF_STEPS = [10**2, 10**3, 10**4]
Y_NUMBER_OF_STEPS = 10**3

E = 10**(-5)
PRECISION = 5


# END OF USER"S DEFINITIONS

# Deep dark backends
# Generators for sums
def left_rectangles_generator(h, start_from=None):
    x = A if start_from is None else start_from
    # x = A  # From 0
    while x <= B - h:  # To n-1
        yield func(x)
        x += h


def right_rectangles_generator(h):
    x = A + h  # From 1
    while x <= B:  # To n
        yield func(x)
        x += h


def trapezium_generator(h):
    x = A + h  # From x0
    while x <= B - h:  # To n-1
        yield func(x)
        x += h


# 'View' functions
def left_rectangles():
    for n in X_NUMBER_OF_STEPS:
        h = (B - A) / n
        i = round(h * sum(left_rectangles_generator(h)), PRECISION)
        print(f'Для {n} шагов: {i}')


def right_rectangles():
    for n in X_NUMBER_OF_STEPS:
        h = (B - A) / n
        i = round(h * sum(right_rectangles_generator(h)), PRECISION)
        print(f'Для {n} шагов: {i}')


def trapezium():
    for n in X_NUMBER_OF_STEPS:
        h = (B - A) / n
        i = round(
            h * ((func(A) + func(B)) / 2 + sum(trapezium_generator(h))),
            PRECISION
        )
        print(f'Для {n} шагов: {i}')


def parable():  # Simpson
    for n in X_NUMBER_OF_STEPS:
        if n % 2 == 1:
            raise ValueError('Number of steps must be even')
        h = (B - A) / n / 2

        odd_sum = 0
        for i in range(1, n):
            odd_sum += func(2 * h * i + A)
        even_sum = 0
        for i in range(1, n + 1):
            even_sum += func(h * (-1 + 2 * i) + A)

        i = round(
            h/3 * (func(A) + func(B) + 2*odd_sum + 4*even_sum),
            PRECISION
        )
        print(f'Для {n} шагов: {i}')


def alg1():
    """Recount every integral"""
    h = math.sqrt(E)
    n_init = int((B - A) / h)
    r = abs((B - A)**3 / (12 * n_init**2) * MAX)
    print('Остаточный член: {:.5f}'.format(r))

    current_integral = h * sum(trapezium_generator(h))
    previous_integral = current_integral
    h /= 2
    n = n_init * 2
    current_integral = h * sum(trapezium_generator(h))

    while abs(current_integral - previous_integral) >= E:
        # Integrate with a new step
        previous_integral = current_integral
        h /= 2
        n *= 2
        current_integral = h * sum(trapezium_generator(h))

    print(f'Начальное количество шагов: {n_init}. '
          f'Финальное количество шагов: {n}')
    print(f'Результат: {round(current_integral, PRECISION)}')


def alg2():
    n_init = X_NUMBER_OF_STEPS[0]  # 100
    r = abs((B - A)**3 / (12 * n_init**2) * MAX)
    print('Остаточный член: {:.5f}'.format(r))

    hv = (B - A) / n_init  # Base step
    previous_integral = hv * sum(left_rectangles_generator(hv))

    hs = hv / 2  # Bias step
    hd = hv  # New step for sum: previous hv
    start_from = A + hs  # Bias from x0
    current_integral = hv * sum(left_rectangles_generator(hd, start_from))
    hv = hs  # new hv
    n = n_init * 2

    while abs(current_integral - previous_integral) >= E:
        n *= 2
        previous_integral = current_integral
        hs = hv / 2  # Bias step
        hd = hv  # New step for sum: previous hv
        start_from = A + hs
        current_integral = hv * sum(left_rectangles_generator(hd, start_from))
        hv = hs  # new hv

    print(f'Начальное количество шагов: {n_init}. '
          f'Финальное количество шагов: {n}')
    print(f'Результат: {round(current_integral, PRECISION)}')


def double_int():
    """Count multiple integral"""
    nx = X_NUMBER_OF_STEPS[0]
    ny = Y_NUMBER_OF_STEPS
    hx = (B2 - A2) / nx
    hy = (D2 - C2) / ny
    print(f'Количество шагов по x: {nx}, hx={hx}.\n'
          f'Количество шагов по y: {ny}, hy={hy}.')
    sx = 0  # Sum for x
    x = A2
    while x <= B2 - hx:
        sy = 0
        y = C2
        while y <= D2 - hy:
            sy += double_func(x, y)
            y += hy
        iy = hy * sy
        sx += iy
        x += hx
    ix = round(hx * sx, PRECISION)
    print(f'Двойной интеграл: {ix}')
