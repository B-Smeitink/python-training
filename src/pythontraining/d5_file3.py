"""
This is an exercise to get familiar with Pylint.

You can install pylint with:
pip install pylint

To use pylint, run the following in the terminal/commandline:
pylint pylint_exercise.py
"""


def main():
    """Function to ask for your name as input."""
    name = input("What is your name? ")
    greet(name)


def greet(name):
    """Function to greet the user."""
    print(f"Hello {name}, how are you?")


def make_percentage(number):
    """Function to make a percentage of a number."""
    percentage = number / 100
    return f"{percentage}%"


if __name__ == "__main__":
    main()
