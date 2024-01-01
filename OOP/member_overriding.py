# super() and member overriding - Object-Oriented Python
# Main class (Person)
#   -> super class, base class, parent class
# Subclasses (Client)
#   -> sub class, child class, derived class

# class MyString(str):
#     def upper(self):
#         return super(MyString, self).upper()

# string = MyString('Charles')
# print(string.upper())

class A:
    a_attribute = 'value'

    def method(self):
        print('A')

class B(A):
    b_attribute = 'value'

    def method(self):
        print('B')

class C(B):
    c_attribute = 'value'

    def method(self):
        super().method()
        print('C')

c = C()
print(c.a_attribute, c.b_attribute, c.c_attribute)
c.method()