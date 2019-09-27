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
    f = func(prev_x)
    d = derived(prev_x)
    cur_x = prev_x - f / d
    while abs(prev_x - cur_x) > PRECISION:
        prev_x = cur_x
        f = func(prev_x)
        d = derived(prev_x)
        cur_x = prev_x - f / d
    print(f'Newton: {cur_x}')


def chord():
    pass


def dichotomy():
    a = A
    b = B
    x = (a + b) / 2
    fa = func(A)  # Left
    fx = func(x)  # Center
    while abs(b - a) > PRECISION:
        if (fa < 0 and fx < 0) or (fa > 0 and fx > 0):
            # Not changed
            # Move left to the center
            a = x
        else:
            # Changed
            # Move right to the center
            b = x
        x = x = (a + b) / 2
        fa = func(a)
        fx = func(x)
    print(x)


dichotomy()
