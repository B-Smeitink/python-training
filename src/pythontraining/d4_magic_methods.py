from functools import total_ordering


@total_ordering
class Person:
    def __init__(self, name, height):
        self.height = height
        self.name = name

    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return f'Person("{self.name}")'

    def __gt__(self, other):
        return self.height > other.height

    def __ge__(self, other):
        return self.height >= other.height

    def __eq__(self, other):
        return self.height == other.height


john = Person("John", 180)
jane = Person("Jane", 170)

print(jane != john)
