try:
    print(undefined_variable)
except NameError:
    print("Variable 'undefined_variable' is not defined")

# Exercise 2
try:
    with open('no_file.txt') as f:
        text = f.read()
except FileNotFoundError as err:
    print(f"Problem trying to open file: {err}")
except Exception as error:
    print("Unexpected error:", type(error), error)

# Exercise 3
ingredients = ["spam", "ham", "eggs"]
try:
    print(ingredients[4])
except IndexError:
    print("Error: this index is out of range")
except Exception as error:
    print("Unexpected error:", type(error), error)


class InvalidEmailError(Exception):
    """Custom exception for invalid email addresses"""


def set_email_address(email):
    if "@" not in email:
        raise InvalidEmailError("Not a valid e-mail address")


try:
    set_email_address("john-at-example.com")
except InvalidEmailError:
    print("Please provide a valid e-mail address")
