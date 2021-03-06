import time
from functools import wraps


def fn_timer(function):
    @wraps(function)
    def function_timer(*args, **kwargs):
        t0 = time.time()
        result = function(*args, **kwargs)
        t1 = time.time()
        print("%s: %s sec." % (function.__name__, str(t1-t0)))
        return result
    return function_timer
