# Class scope and class methods scope
class Animal:
    def __init__(self, name):
        self.name = name

        var = 'value'
        print(var)

    def eating(self, food):
        print(f'{self.name} is eating {food}.')
    
    def execute(self, *args, **kwargs):
        return self.eating(*args, **kwargs)
    
lion = Animal(name='Lion')
print(lion.name)
lion.execute('meat')