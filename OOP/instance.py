# __dict__ and vars for instance attributes
class Person:
    current_year = 2023

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_birth_year(self):
        return Person.current_year - self.age

# person_one = Person('Charles', 26)
# person_one.name = 'Leclerc'
# print(person_one.name)
# person_one.__dict__['name'] = 'Leclerc'
# print(person_one.__dict__)
# print(vars(person_one))
# print(person_one.name)
    
data = {'age': 26, 'name': 'Charles'}
person_one = Person(**data)

print(person_one.get_birth_year())