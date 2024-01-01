# Simple Inheritance - Relationships between classes
# Association - uses, Aggregation - has
# Composition - Owns, Inheritance - Is a
#
# Inheritance vs Composition
#
# Main class (Person)
#   -> super class, base class, parent class
# Subclasses (Client)
#   -> sub class, child class, derived class
class Person:
    def __init__(self, name, surename) -> None:
        self.name = name
        self.surename = surename

    def display_class_name(self):
        print(self.name, self.surename, self.__class__.__name__)

class Customer(Person):
    ...

person_one = Customer('Charles', 'Leclerc')
person_one.display_class_name()