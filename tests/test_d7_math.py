# test_mathematics.py
from src.pythontraining.d7_math import multiply, divide, round_up, hypotenuse, count_registrations, create_attendee_list
import pytest


def test_multiplication():
    assert multiply(4, 5) == 20


def test_division():
    assert divide(4, 5) == 0.8
    assert divide(2, 3) == 0.7


def test_round_up():
    assert round_up(2.4) == 3


def test_hypotenuse():
    """Returns the longest side of a right-angled triangle.

    Pythagorean Theorem: a² + b² = c²

    3² + 4² = 5²
    9  + 16 = 25
    Hypotenuse (c) = 5.0
    """
    assert hypotenuse(3, 4) == 5


@pytest.fixture
def registrations():
    return [
        {'first_name': 'John', 'last_name': 'Doe'},
        {'first_name': 'Jane', 'last_name': 'Smith'},
        {'first_name': 'Diana', 'last_name': 'Rogers'}
    ]


def test_count_registrations(registrations):
    count = count_registrations(registrations)
    assert count == 3


def test_create_attendee_list(registrations):
    attendees = create_attendee_list(registrations)
    assert attendees == ['John Doe', 'Jane Smith', 'Diana Rogers']
