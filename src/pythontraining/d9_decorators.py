"""
This is an exercise to get familiar with decorators.
"""


import time
from functools import wraps

#
# # Exercise
# def timer(func):
#     def wrapper():
#         start = time.perf_counter()
#         result = func()
#         stop = time.perf_counter()
#         print(f"Run time was {stop-start} seconds")
#         return result
#     return wrapper
#
#
# @timer
# def do_something():
#     """Toy function to keep Python busy"""
#     return "-".join(str(n) for n in range(1000000))
#
#
# do_something()


# Exercise 2
def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        stop = time.perf_counter()
        print(f"Run time was {stop-start} seconds")
        return result

    return wrapper


@timer
def do_something(number):
    """Toy function to keep Python busy"""
    return "-".join(str(n) for n in range(number))


print(do_something.__name__)
print(do_something.__doc__)
do_something(1_000_000)
