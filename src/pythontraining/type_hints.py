"""
Type hinting exercise
"""

def main():
    """Simple program for illustrative purposes"""
    age = ask_user_age()
    print_age(age)


def ask_user_age():
    """Return user input"""
    age: int = int(input("What is your age in years? "))
    return age


def print_age(age: int):
    """Print full sentence"""
    age_in_months: int = age * 12
    print(f"You are {age_in_months} months old.")


y: list[int | float] = [1, 2.0]

z: dict[int, dict[str, str]] = {1: {"name": "Jane"}, 2: {"name": "John"}}

if __name__ == "__main__":
    main()
