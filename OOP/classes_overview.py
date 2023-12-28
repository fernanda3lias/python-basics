# Exercise with classes
# 1 - Create a class Car (Name)
# 2 - Create a class Engine (Name)
# 3 - Create a class Manufacturer (Name)
# 4 - Establish the relationship that a Car has an Engine
# Note: An engine can be used in multiple cars
# 5 - Establish the relationship that a Car has a Manufacturer
# Note: A manufacturer can produce multiple cars
# Display the name of the car, engine, and manufacturer on the screen
class Car:
    def __init__(self, name) -> None:
        self.name = name
        self._engine = None
        self._manufacturer = None

    @property
    def engine(self):
        return self._engine
    
    @engine.setter
    def engine(self, value):
        self._engine = value
    @property
    def manufacturer(self):
        return self._manufacturer
    
    @manufacturer.setter
    def manufacturer(self, value):
        self._manufacturer = value

    def use_engine(self):
        print(f"{self.manufacturer.name} {self.name} is using {self.engine.name} engine...")

class Engine:
    def __init__(self, name) -> None:
        self.name = name

class Manufacturer:
    def __init__(self, name) -> None:
        self.name = name

uno = Car('Uno')
evo = Engine('Evo 1.0')
fiat = Manufacturer('Fiat')
uno.engine = evo
uno.manufacturer = fiat

# print(uno.name, uno.engine.name, uno.manufacturer.name)
uno.use_engine()

