# Creating Exceptions in Object-Oriented Python
# To create an exception in Python, you just
# need to inherit from some language exception.
# The recommendation from the documentation is to inherit from Exception.
# https://docs.python.org/3/library/exceptions.html
# Creating exceptions (common to end with Error)
# Raising exceptions
# Re-raising exceptions
# Adding notes to exceptions (3.11.0)
class MyError(Exception):
    ...


class AnotherError(Exception):
    ...


def raise_():
    exception_ = MyError('a', 'b', 'c')
    exception_.add_note('First note.')
    raise exception_


try:
    raise_()
except (MyError, ZeroDivisionError) as error:
    print(error.__class__.__name__)
    print(error.args)
    print()
    exception_ = AnotherError('Raising again.')
    exception_.__notes__ = error.__notes__.copy()
    exception_.add_note('One more note.')
    raise exception_ from error