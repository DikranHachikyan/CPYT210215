
from time import  time, sleep
from functools import wraps

def measure(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        t = time()
        func(*args, **kwargs)
        print(f'wrapper:{func.__name__}:{func.__doc__}')
        print(f'{func.__name__}:{time()-t:.4f}')
    return wrapper

@measure
def foo(sleep_time = 0.3):
    """Function foo, sleeps sleep_time seconds"""
    sleep(sleep_time)

@measure
def show_message(msg):
    """Print msg in standard output"""
    print(msg)

if __name__ == '__main__':
    
    foo()
    foo(0.5)
    print(f'{foo.__name__}:{foo.__doc__}')


    show_message('Hello Python')