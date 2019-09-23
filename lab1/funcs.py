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

# Variable steps
VAR_NUMBER_OF_STEPS = 50
PRECISION = 10**(-5)


# END OF USER"S DEFINITIONS

# Deep dark backends
def printable(gen):
    """Print result returned by the function"""
    @wraps(gen)
    def new_func(*args, **kwargs):
        for i, n in gen(*args, **kwargs):
            print(f'For {n}: {i:.5f}')
    return new_func


def step_generator():
    """Yield step lengths"""
    for n in NUMBER_OF_STEPS:
        yield (B - A) / n


# Generators for sums
def left_rectangles_generator(h):
    x = A  # From 0
    while x <= B - h:  # To n-1
        yield func(x)
        x += h


def right_rectangles_generator(h):
    x = A + h  # From 1
    while x <= B:  # To n
        yield func(x)
        x += h


def trapezium_generator(h):
    x = A + h  # From 1
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


@printable
def alg1():
    """Count at every step until the precision is attempted"""
    h = math.sqrt(PRECISION)
    n = int((B - A) / h)
    r = abs((B - A)**3 / (12 * n**2) * MAX)
    print('Остаточный член: {:.10f}'.format(r))

    previous_sum = 0
    current_sum = h * sum(trapezium_generator(h))

    while abs(current_sum - previous_sum) > PRECISION:
        # Integrate with a new step
        previous_sum = current_sum
        h /= 2

        current_sum = h * sum(trapezium_generator(h))

    yield current_sum, n


def alg2():
    print('will be soon 2')
