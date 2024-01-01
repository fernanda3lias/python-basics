# Multiple Inheritance - Object-Oriented Python
# It means that in Python, a class can inherit
# from multiple other classes.
# Single Inheritance:
# Animal -> Mammal -> Human -> Person -> Client
# Multiple Inheritance and Mixins
# Log -> FileLog
# Animal -> Mammal -> Human -> Person -> Client
# Client(Person, FileLog)
#
# A, B, C, D
# D(B, C) - C(A) - B(A) - A
#
# method -> speak
#           A
#         /   \
#        B     C
#         \   /
#           D
#
# Python 3 uses C3 superclass linearization
# to generate the MRO (Method Resolution Order).
# You don't need to study this (it's complex)
# https://en.wikipedia.org/wiki/C3_linearization
#
# To find out the method resolution order
# Use the class method Class.mro()
# Or the attribute __mro__ (Dunder - Double Underscore)
class A:
    ...

    def who(self):
        print('A')

class B(A):
    ...

    def who(self):
        print('B')

class C(A):
    ...

    def who(self):
        print('C')

class D(B, C):
    ...

    # def who(self):
    #     print('D')

d = D()
d.who()
print(D.mro())