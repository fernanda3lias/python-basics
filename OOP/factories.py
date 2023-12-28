# Class methods + factories
# These are methods where "self" becomes "cls," meaning,
# instead of receiving the instance as the first parameter,
# we receive the class itself.
class Person:
    current_year = 2023 # class attribute

    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    @classmethod
    def class_method(cls):
        print('Hey, world!')

    @classmethod
    def create_fifty_years(cls, name):
        return cls(name, 50)

person_one = Person('Charles', 26)
person_two = Person.create_fifty_years('John')
print(person_two.__dict__)

#print(Person.current_year)
Person.class_method()