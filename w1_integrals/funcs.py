import math

from decorators import with_steps, with_print


STEPS = [10**2, 10**3, 10**4]
A = 0
B = 1


def func(x):
    """Integrated function"""
    # return math.exp(-x**2)
    return math.sin(x)


@with_steps(STEPS)
@with_print
def left_triangles(n):
    h = (B - A) / n  # h
    x = A
    i = 0  # sum
    while x < B:
        i += func(x)
        x += h
    i *= h
    return i, n


@with_steps(STEPS)
@with_print
def right_triangles(n):
    h = (B - A) / n  # h
    x = A + h
    i = 0  # sum
    while x <= B:
        i += func(x)
        x += h
    i *= h
    return i, n


@with_steps(STEPS)
@with_print
def trapezium(n):
    h = (B - A) / n  # h
    sum_ = 0
    x = A + h
    while x <= B - h:
        sum_ += func(x)
        x += h
    i = h * ((func(A) + func(B)) / 2 + sum_)
    return i, n


@with_steps(STEPS)
@with_print
def parable(n):  # Simpson
    if n % 2 == 1:
        raise ValueError('N must be even')
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
    i = sum_ * (h/3)
    return i, n


def alg1():
    print('will be soon 1')


def alg2():
    print('will be soon 2')
