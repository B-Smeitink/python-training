# mathematics.py
import math


def multiply(x, y):
    return x * y


def divide(x, y):
    return round(x / y, 1)  # should be return round(x / y, 1)


def round_up(x):
    rounded = math.ceil(x)
    return rounded


def hypotenuse(x, y):
    return math.sqrt(x ** 2 + y ** 2)


def count_registrations(registrations):
    return len(registrations)


def create_attendee_list(registrations):
    return [f"{r['first_name']} {r['last_name']}"
            for r in registrations]


def create_attendee_list2(registrations):
    return [f"{r['first_name']} {r['last_name']}"
            for r in registrations]
