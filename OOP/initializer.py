# Introduction to the __init__ method (attribute initializer)
class Person: # Class
    def __init__(self, name, surename): # Method with parameters
        self.name = name # Class attribute
        self.surename = surename

person_one = Person("Charles", "Leclerc") # Object/instance

print(person_one.name)