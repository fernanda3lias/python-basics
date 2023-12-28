# @staticmethod (static methods) are useless in Python =)
# Static methods are methods within the class but have no access
# to self or cls. In summary, they are functions that exist
# within your class.
class Class:
    @staticmethod
    def class_function(*args, **kwargs):
        print('Hey, world!', args, kwargs)

class_one = Class()
class_one.class_function(1, 2, 3, named=1)