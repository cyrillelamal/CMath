PRECISION = 10**(-3)

A = -10
B = 10
START_X = 9.9


def func(x):
    """Return function value"""
    return 3 * x**4 - 8 * x**3 - 18 * x**2 + 2


def derived(x):
    """Return function derive value"""
    return 12 * x**3 - 24 * x**2 - 36 * x


def newton():
    prev_x = START_X
    cur_x = prev_x - func(prev_x) / derived(prev_x)
    while abs(prev_x - cur_x) >= PRECISION:
        prev_x = cur_x
        cur_x = prev_x - func(prev_x) / derived(prev_x)
    print(f'Newton: {cur_x}')


def chord():
    prev_x = A
    cur_x = B

    while abs(cur_x - prev_x) >= PRECISION:
        x = cur_x - ((cur_x - prev_x)*func(cur_x)) / (func(cur_x) - func(prev_x))
        prev_x = cur_x
        cur_x = x
    print(f'Chord: {cur_x}')


def dichotomy():
    left = A
    right = B
    x = START_X

    while abs(left - right) >= PRECISION:
        x = (left + right) / 2
        left, right = (left, x) if func(x) > 0 else (x, right)
    print(f'Dichotomy: {x}')


dichotomy()
