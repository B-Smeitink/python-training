"""
Type hinting exercise with classes
"""
from typing import Generator


def main() -> None:
    """Simple program for illustrative purposes"""
    name = ask_name()
    my_account = BankAccount(name)
    my_account.deposit(10_000)
    my_account.withdraw(5_000)
    my_account.print_balance()


def ask_name():
    """Return user input"""
    name: str = input("What is your name? ")
    return name


class BankAccount:
    """Simple class for bank accounts"""

    def __init__(self, owner: str):
        """Initialise account (balance 0)"""
        self.owner = owner
        self.balance = 0

    def deposit(self, amount: int):
        """Add money to the account"""
        self.balance += amount

    def withdraw(self, amount: int):
        """Withdraw money from the account"""
        self.balance -= amount

    def print_balance(self):
        """Prints full sentence"""
        print(f"Your account has €{self.balance:,}")


# Exercise 5
def my_sum(numbers: list) -> int:
    total = 0
    for n in numbers:
        total += n
    return total


# Exercise 6
def infinite_stream(start: int) -> Generator:
    while True:
        yield start
        start += 1


if __name__ == "__main__":
    main()
