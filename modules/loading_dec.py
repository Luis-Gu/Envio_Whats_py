"""
    Just a module to generate a "frufruzin" decorator
"""
import time
import threading
from functools import wraps

# Decorador para simular um loading durante a execução da função
def loading_decorator(func):
    """
        Basically a decorator that adds a loading signal to functions

    Args:
        func : Function
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        stop_loading : bool | str = False

        def loading_animation():
            chars = "⠋⠙⠹⠸⠼⠴⠦⠧⠇⠏"
            while stop_loading is False:
                for char in chars:
                    print('\r\033[34m'
                          f'Trying to run "{func.__name__}" {char} '
                          '\033[0m', flush=True, end='')
                    time.sleep(0.1)
            if stop_loading == "Success":
                print('\r\033[32m'
                    f'Function "{func.__name__}" executed successfully'
                    '\033[0m', flush=True)
            else:
                print('\r\033[31m'
                  f'Function "{func.__name__}" encountered an unexpected error'
                  '\033[0m', flush=True)
        loading_thread : threading.Thread = threading.Thread(target=loading_animation)
        loading_thread.start()
        try:
            result = func(*args, **kwargs)
            stop_loading = 'Success'
        except:
            result = 'Fail'
            stop_loading = 'Fail'
        loading_thread.join()
        return result

    return wrapper
