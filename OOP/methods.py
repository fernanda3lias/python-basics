# Methods in Python class instances
# Hard coded - It is something that was written directly in the code
# Class - template (without data)
# Instance of the class (object) - Has the data
# A class can generate multiple instances.
# In the class, 'self' is the instance itself.
class Car:
    def __init__(self, name='None'):
        self.name = name

    def accelerate(self): # Method
        print(f"{self.name} is accelerating...")

beatle = Car('Beatle')
beatle.accelerate()
