# Exercise - Save your class to JSON
# Save the data from your class to JSON
# and then recreate instances of the class
# with the saved data
# Do it in separate files.
import json
from pathlib import Path

class Person:
    current_year = 2023
    def __init__(self, name, surename, age):
        self.name = name
        self.surename = surename
        self.age = age

person_one = Person("Charles", "Leclerc", 26)
person_one_data = person_one.__dict__

def save_to_json():
    ROOT_PATH = Path(__file__).parent
    FILE_NAME = ROOT_PATH / 'data.json'
    with open(FILE_NAME, 'w', encoding='utf8') as file:
        json.dump(person_one_data, file, indent=2, ensure_ascii=False)
        return

save_to_json()
print(person_one_data)