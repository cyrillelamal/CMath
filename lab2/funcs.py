E = 10 ** (-3)

A = -10
B = 10

N_X0 = 9.9  # Newton
D_X0 = 2  # Dichotomy


def func(x):
    """Return function value"""
    return 3 * x ** 4 - 8 * x ** 3 - 18 * x ** 2 + 2


def derived(x):
    """Return function derive value"""
    return 12 * x ** 3 - 24 * x ** 2 - 36 * x


def newton():
    prev_x = N_X0
    cur_x = prev_x - func(prev_x) / derived(prev_x)
    while abs(cur_x - prev_x) >= E:
        prev_x = cur_x
        cur_x = prev_x - func(prev_x) / derived(prev_x)
    print('Newton: {:.5}'.format(cur_x))


def chord():
    prev_x = A
    cur_x = B
    while abs(cur_x - prev_x) >= E:
        x = cur_x - ((cur_x - prev_x) * func(cur_x)) / (func(cur_x) - func(prev_x))
        prev_x = cur_x
        cur_x = x
    print('Chord: {:.5}'.format(cur_x))


def dichotomy():
    """Half divide method"""
    a = D_X0
    b = B
    x = (a + b) / 2
    while abs(func(x)) >= E:
        x = (a + b) / 2
        a, b = (a, x) if func(a) * func(x) < 0 else (x, b)
    result = (a + b) / 2
    print('Dichotomy: {:.5}'.format(result))
