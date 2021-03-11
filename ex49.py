
from functools import wraps


def upper_case(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.__original = func
        args = [ f'{v}'.upper() for v in args]
        return func(*args, **kwargs)
    return wrapper




@upper_case
def concat(*args,**kwargs):
    """Concatenate list of elements with separator sep"""
    sep = kwargs.get('sep',';')
    return sep.join(args)

if __name__ == '__main__':
    users = ['anna','maria','markus','jane','florian']

    print(concat(*users, sep = ' | '))
    print(concat(11,12,14,45))
    
    print(concat.__original(*users, sep = ' | '))
    # print(concat.__original(11,12,14,45))

    concat = concat.__original
    print(concat(*users, sep = ' | '))

    print('hello python')

    print = upper_case(print)
    print('hello python')
    print = print.__original
    print('hello python')

    