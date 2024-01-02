# __new__ and __init__ in Python classes
# __new__ is the method responsible for creating and
# returning the new object. Therefore, new receives cls.
# __new__ ❗️MUST return the new object❗️
# __init__ is the method responsible for initializing
# the instance. Therefore, init receives self.
# __init__ ❗️MUST NOT return anything (None)❗️
# object is the superclass of a class
class A:
    def __new__(cls, *args, **kwargs):
        print('Before')
        instance =  super().__new__(cls)
        print('After')
        instance.x = 123
        return instance

    def __init__(self, x) -> None:
        print('Init')

    def __repr__(self) -> str:
        return 'A()'
    
a = A(123)
print(a.x)
# a = object.__new__(A)
# a.__init__()
# print(a)