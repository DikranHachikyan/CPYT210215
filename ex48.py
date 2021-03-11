
from functools import wraps


def upper_case(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # args = [ v.upper() for v in args]
        args = [ f'{v}'.upper() for v in args]
        return func(*args, **kwargs)
    return wrapper

def add_brackets(left='[', right = ']'):
    def decorator(func):
        @wraps(func)
        def wrapper(*args,**kwargs):
            args = [ f'{left}{v}{right}' for v in args]
            return func(*args,**kwargs)
        return wrapper
    return decorator

@add_brackets(left='<', right = '>')
@upper_case
def concat(*args,**kwargs):
    """Concatenate list of elements with separator sep"""
    sep = kwargs.get('sep',';')
    return sep.join(args)

if __name__ == '__main__':
    users = ['anna','maria','markus','jane','florian']

    print(concat(*users, sep = ' | '))
    print(concat(11,12,14,45))