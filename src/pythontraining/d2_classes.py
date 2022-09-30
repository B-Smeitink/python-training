from datetime import datetime


class Person:
    def __init__(self, name, dob):
        self.name = name
        self.dob = dob

    def say_hello(self):
        print(f"{self.name} says hello")

    def age(self):
        dob_date = datetime.strptime(self.dob, '%Y-%m-%d')
        return datetime.today() - dob_date


p1 = Person("John", 42)
print(p1.name)

p2 = Person("Jane", 42)
p2.say_hello()


class Student(Person):
    def learn(self, language):
        print(f"{self.name} is learning {language}")


s1 = Student('John', 42)
s1.say_hello()
s1.learn('Java')

p1 = Person("John", "1978-01-01")
print(p1.name)
print(p1.age())
