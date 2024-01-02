# Context Manager with classes - Creating and Using Context Managers
# You can implement your own protocols
# by just implementing the dunder methods that Python will use.
# This is called Duck typing. A concept
# related to dynamic typing where Python is not
# concerned about the type, but if certain methods exist
# in your object so that it works properly.
# Duck Typing:
# When I see a bird that walks like a duck, swims like
# a duck, and quacks like a duck, I call that bird a duck.
# To create a context manager, the __enter__ and __exit__
# methods must be implemented.
# The __exit__ method will receive the exception class, the exception, and the
# traceback. If it returns True, exceptions in the with statement will be
# suppressed.
#
# Example:
# with open('lesson149.txt', 'w') as file:
#     ...
from contextlib import contextmanager
from pathlib import Path

# class MyOpen:
#     def __init__(self, file_path, mode) -> None:
#         ROOT_PATH = Path(__file__).parent
#         self.file_path = ROOT_PATH / file_path
#         self.mode = mode
#         self._file = None
        
#     def __enter__(self):
#         print('Opening file...')
#         self._file = open(self.file_path, self.mode, encoding='utf8')
#         return self._file
    
#     def __exit__(self, class_exception, exception_, traceback_):
#         print('Closing file...')
#         self._file.close()

#         # raise class_exception(*exception_.args).with_traceback

#         # print(class_exception)
#         # print(exception_)
#         # print(traceback_)

#         # exception_.add_note('Notes.')

#         raise ConnectionError('Could not connect.')

#         # return True # Handled the exception

# # instance = MyContextManager()

# with MyOpen('text.txt', 'w') as file:
#     file.write('First line', 123)
#     print('WITH', file)

@contextmanager
def my_open(file_path, mode):
    try:
        print('Opening file...')
        ROOT_PATH = Path(__file__).parent
        file_path = ROOT_PATH / file_path
        file = open(file_path, mode, encoding='utf8')
        yield file
    except Exception as e:
        print('Error', e)
    finally:
        print('Closing file...')
        file.close()

with my_open('text.txt', 'w') as file:
    file.write('First line', 123)
    print('WITH', file)