import math

from decorators import with_steps, with_print


PRECISION = 10**(-5)

NUMBER_OF_STEPS = [10**2, 10**3, 10**4]

BASE_NUMBER_OF_STEPS = 10  # Variable

A = 0
B = 1


def func(x):
    """Integrated function"""
    return math.sin(x)  # 0.45970


def left_rectangles_generator(h):
    x = A
    while x < B:
        yield func(x)
        x += h


def right_rectangles_generator(h):
    x = A + h
    while x <= B:
        yield func(x)
        x += h


def trapezium_generator(h):
    x = A + h
    while x < B - h:
        yield func(x)
        x += h


@with_steps(NUMBER_OF_STEPS)
@with_print
def left_rectangles(n):
    h = (B - A) / n  # h
    i = h * sum(left_rectangles_generator(h))
    return i, n


@with_steps(NUMBER_OF_STEPS)
@with_print
def right_rectangles(n):
    h = (B - A) / n  # h
    i = h * sum(right_rectangles_generator(h))
    return i, n


@with_steps(NUMBER_OF_STEPS)
@with_print
def trapezium(n):
    h = (B - A) / n  # h
    i = h * ((func(A) + func(B)) / 2 + sum(trapezium_generator(h)))
    return i, n


@with_steps(NUMBER_OF_STEPS)
@with_print
def parable(n):  # Simpson
    if n % 2 == 1:
        raise ValueError('Number of steps must be even')
    sum_ = func(A) + func(B)
    h = (B - A) / (2*n)

    odd_sum = 0
    for i in range(1, n):
        odd_sum += func(2*h*i + A)
    sum_ += 2*odd_sum

    even_sum = 0
    for i in range(1, n+1):
        even_sum += func(h*(-1+2*i)+A)
    sum_ += 4*even_sum
    sum_ *= (h/3)
    return sum_, n


@with_print
def alg1():
    """Count at every step until the precision is attempted"""
    base_h = (B - A) / BASE_NUMBER_OF_STEPS
    # A smaller integral in the integral
    previous_sum = 0
    h = base_h

    # Base small integral (do, while)
    current_sum = h * sum(left_rectangles_generator(h))

    while abs(current_sum - previous_sum) > PRECISION:
        # Integrate with a new step
        previous_sum = current_sum
        h /= 2

        current_sum = h * sum(left_rectangles_generator(h))

    return current_sum, h


def alg2():
    print('will be soon 2')
