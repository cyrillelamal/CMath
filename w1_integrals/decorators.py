from functools import wraps


def with_steps(steps):
    """Append to the function parameter with number of steps"""
    def decorator(func):
        @wraps(func)
        def new_func(*args, **kwargs):
            for n in steps:
                result = func(n)
            return result
        return new_func
    return decorator


def with_print(func):
    """Print result returned by the function"""
    @wraps(func)
    def new_func(*args, **kwargs):
        i, n = func(*args, **kwargs)
        print(f'For {n}: {i:.5f}')
    return new_func
