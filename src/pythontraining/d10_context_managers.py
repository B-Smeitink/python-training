"""
Refactor the program below (use a "with" statement).
"""
import time


class benchmark(object):
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        self.start = time.perf_counter()

    def __exit__(self, exc_type, exc_val, exc_tb):
        end = time.perf_counter()
        print("%s : %0.3f seconds" % (self.name, end - self.start))
        return False


def main():
    text = "Explicit is better than implicit."
    with benchmark("timing"):
        write_to_file(text)


def write_to_file(text):
    with open("exercise.txt", "w") as file:
        file.write(text)


if __name__ == "__main__":
    main()
