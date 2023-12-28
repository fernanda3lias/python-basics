# Encapsulation (access modifiers: public, protected, private)
# Python DOES NOT HAVE access modifiers
# But we can follow the following conventions
#   (no underscore) = public
#       can be used anywhere
# _ (one underscore) = protected
#       should not be used outside the class
#       or its subclasses.
# __ (two underscores) = private
#       "name mangling" in Python
#       _ClassName__name_attr_or_method
#       should only be used within the class where it was declared.
class Foo:
    def __init__(self):
        self.public = 'public'
        self._protected = 'protected'
        self.__private = 'private'

    def public_method(self):
        print(self.__private)
        return 'public method'
    
    def _protected_method(self):
        return 'protected method'
    
    def __private_method(self):
        return 'private method'

foo = Foo()
print(foo.public)
print(foo.public_method())