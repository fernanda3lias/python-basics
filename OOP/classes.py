# class - Classes are blueprints for creating new objects
# Classes generate new objects (instances) that
# can have their own attributes and methods.
# Objects created by the class can use their internal data
# to perform various actions.
# By convention, we use PascalCase for class names.

class Person: # Class
    ...

person_one = Person() # Object/instance
person_one.name = 'Charles'
person_one.surename = 'Leclerc'
print(person_one.name, person_one.surename)
