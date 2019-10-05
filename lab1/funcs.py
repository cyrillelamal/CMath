import math
from functools import wraps


# USER'S DEFINITIONS

# Edges
A = 1
B = 4


# Integrated function
def func(x):
    return 2*x + 3/math.sqrt(x)  # 21


# Function maximum
MAX = math.inf

# Constant steps
NUMBER_OF_STEPS = [10**2, 10**3, 10**4]

E = 10**(-5)
PRECISION = 5


# END OF USER"S DEFINITIONS

# Deep dark backends
def printable(gen):
    """Print result returned by the function"""
    @wraps(gen)
    def new_func(*args, **kwargs):
        for i, n in gen(*args, **kwargs):
            print(f'Для {n}: {i:.5f}')
    return new_func


def step_generator():
    """Yield step lengths"""
    for n in NUMBER_OF_STEPS:
        yield (B - A) / n


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
@printable
def left_rectangles():
    for n, h in zip(NUMBER_OF_STEPS, step_generator()):
        i = h * sum(left_rectangles_generator(h))
        yield i, h


@printable
def right_rectangles():
    for n, h in zip(NUMBER_OF_STEPS, step_generator()):
        i = h * sum(right_rectangles_generator(h))
        yield i, n


@printable
def trapezium():
    for n, h in zip(NUMBER_OF_STEPS, step_generator()):
        i = h * ((func(A) + func(B)) / 2 + sum(trapezium_generator(h)))
        yield i, n


@printable
def parable():  # Simpson
    for n, h in zip(NUMBER_OF_STEPS, step_generator()):
        if n % 2 == 1:
            raise ValueError('Number of steps must be even')

        h /= 2

        odd_sum = 0
        for i in range(1, n):
            odd_sum += func(2 * h * i + A)
        even_sum = 0
        for i in range(1, n + 1):
            even_sum += func(h * (-1 + 2 * i) + A)

        i = h/3 * (func(A) + func(B) + 2*odd_sum + 4*even_sum)
        yield i, n


def alg1():
    """Count at every step until the precision is attempted"""
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
    hv = (B - A) / NUMBER_OF_STEPS[0]  # Base step
    previous_integral = hv * sum(left_rectangles_generator(hv))

    hs = hv / 2  # Bias step
    hd = hv  # New step for sum: previous hv
    start_from = A + hs  # Bias from x0
    current_integral = hv * sum(left_rectangles_generator(hd, start_from))
    hv = hs  # new hv

    while abs(current_integral - previous_integral) >= E:
        previous_integral = current_integral
        hs = hv / 2  # Bias step
        hd = hv  # New step for sum: previous hv
        start_from = A + hs
        current_integral = hv * sum(left_rectangles_generator(hd, start_from))
        hv = hs  # new hv

    print(f'Результат: {round(current_integral, PRECISION)}')
