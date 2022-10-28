"""
Multithreading
"""


import time
from concurrent.futures import ThreadPoolExecutor
from functools import wraps
from pathlib import Path

ZEN = """The Zen of Python, by Tim Peters

    Beautiful is better than ugly.
    Explicit is better than implicit.
    Simple is better than complex.
    Complex is better than complicated.
    Flat is better than nested.
    Sparse is better than dense.
    Readability counts.
    Special cases aren't special enough to break the rules.
    Although practicality beats purity.
    Errors should never pass silently.
    Unless explicitly silenced.
    In the face of ambiguity, refuse the temptation to guess.
    There should be one-- and preferably only one --obvious way to do it.
    Although that way may not be obvious at first unless you're Dutch.
    Now is better than never.
    Although never is often better than right now.
    If the implementation is hard to explain, it's a bad idea.
    If the implementation is easy to explain, it may be a good idea.
    Namespaces are one honking great idea -- let's do more of those!
    """


def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        print(f'\nRun time was {end_time - start_time} seconds.')
        return result

    return wrapper


def write_one(file: Path):
    file.write_text(ZEN)


@timer
def write_many(files):
    for file in files:
        write_one(file)
    # with ThreadPoolExecutor() as executor:
    #     executor.map(write_one, files)


if __name__ == "__main__":
    path = Path("temp_exercise_multithreading")
    path.mkdir(exist_ok=True)
    all_files = [path.joinpath(f"File {i}.txt")
                 for i in range(10000)]
    write_many(all_files)