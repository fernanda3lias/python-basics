# Abstract Classes - Abstract Base Class (abc)
# ABCs are used as contracts for defining
# new classes. They can force other classes
# to create concrete methods. They can also have
# concrete methods themselves.
# @abstractmethods are methods without a body.
# The rules for abstract classes with abstract methods
# are that they CANNOT be instantiated directly.
# Abstract methods MUST be implemented
# in the subclasses (@abstractmethod).
# An abstract class in Python has its metaclass
# being ABCMeta.
# It's possible to create @property, @setter,
# @classmethod, @staticmethod, and @method as abstract.
# To do this, use @abstractmethod as the innermost decorator.
from abc import ABC, abstractmethod

# class Log(metaclass=ABCMeta):
#     ...

class Log(ABC):
    @abstractmethod
    def _log(self, message): ...
    
    def log_error(self, message):
        self._log(f'Error: {message}')

    def log_success(self, message):
        self._log(f'Success: {message}')

class LogPrintMixin(Log):
    def _log(self, message):
        print(f'{message} ({self.__class__.__name__})')

L = LogPrintMixin()
L.log_error('Hey')