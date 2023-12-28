# @property - a Pythonic way of creating a getter
# getter - a method to retrieve an attribute
# color -> get_color()
# Pythonic way - Pythonic way of doing things
# @property is an object property, it's a method
# that behaves like an attribute 🤯 🤯 🤯
# Typically used in the following situations:
# - as a getter
# - to avoid breaking client code
# - to enable a setter
# - to perform actions when getting an attribute
# Client code - the code that uses your code
class Pen:
    def __init__(self, colour):
        self.tint_colour = colour

    @property
    def colour(self):
        print('PROPERTY')
        return self.tint_colour
    
    @property
    def cap_colour(self):
        return 'white'

pen = Pen('blue')
print(pen.colour)
print(pen.cap_colour)

""" class Pen:
    def __init__(self, colour):
        # private, protected, public
        self.colour = colour

    def get_colour(self):
        print('GET COLOUR')
        return self.colour

pen = Pen('Blue')
print(pen.get_colour()) """