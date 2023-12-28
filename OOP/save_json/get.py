import json
from pathlib import Path

class Person:
    current_year = 2023
    def __init__(self, name, surename, age):
        self.name = name
        self.surename = surename
        self.age = age

def get_data_from_json():
    ROOT_PATH = Path(__file__).parent
    FILE_NAME = ROOT_PATH / 'data.json'
    with open(FILE_NAME, 'r', encoding='utf8') as file:
        data = json.load(file)
        return data

data = get_data_from_json()
person_one = Person(**data)
print(person_one.__dict__)
    
