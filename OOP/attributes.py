# Class attributes
class Person:
    current_year = 2023

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_birth_year(self):
        return Person.current_year - self.age
    
person_one = Person('Charles', 26)
person_two = Person('Lewis', 38)

print(person_one.get_birth_year())
print(person_two.get_birth_year())