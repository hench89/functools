from functools import wraps


# example 1: a custom decorator applied for a function
# using wraps decorator it is possible to fix problems with function variables.


def decorator_without(f):
    def wrapper(*args, **kwargs):
        'wrapper docstring'
        print('wrapper called')
        return f(*args, *kwargs)
    return wrapper


def decorator_with(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        'wrapper docstring'
        print('wrapper called')
        return f(*args, *kwargs)
    return wrapper


@decorator_without
def fn_without_wraps():
    'myfunc docstring'
    print('my function called')


@decorator_with
def fn_with_wraps():
    'myfunc docstring'
    print('my function called')


print(f'function/docstring of function without wraps applied: {fn_without_wraps.__name__}, {fn_without_wraps.__doc__}')
print(f'function/docstring of function with wraps applied: {fn_with_wraps.__name__}, {fn_with_wraps.__doc__}')
