import time
from typing import Callable

def time_it(func: Callable):
    def wrapper(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        work = time.time() - start
        print(f"Execution time of '{func.__name__}': {int(work)} seconds")
        return res
    return wrapper

def add_point(original_list: list, value):
    time.sleep(2)
    return original_list[:].append(value)

@time_it
def add_point_with_timer(original_list: list, value):
    add_point(original_list, value)

add_point_with_timer([1, 2, 3, 4, 5], 6)