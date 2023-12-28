# @property + @setter - Pythonic getter and setter
# - as a getter
# - to avoid breaking client code
# - to enable a setter
# - to perform actions when getting an attribute
# Attributes that start with one or two underscores
# should not be used outside the class.
# 🐍🤓🤯🤯🤯🤯
class Pen:
    def __init__(self, colour):
        self.colour = colour
        self._cap_colour = None

    @property
    def colour(self):
        print('GETTER')
        return self._colour
    
    @colour.setter
    def colour(self, value):
        print('SETTER')
        self._colour = value

    @property
    def cap_colour(self):
        return self._cap_colour
    
    @cap_colour.setter
    def cap_colour(self, value):
        self._cap_colour = value
    
    
pen = Pen('blue')
pen.colour = 'pink'

# getter -> get value
print(pen.colour)

print(pen.cap_colour)

pen.cap_colour = 'blue'
print(pen.cap_colour)