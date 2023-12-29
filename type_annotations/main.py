# Type annotations

# a_string: str = 'value'
# a_integer: int = 123
# a_float_number: float = 1.23
# a_boolean: bool = True
# a_set: set = {1, 2, 3} 
# a_list: list = [1, 2, 3]
# a_tuple: tuple = 1, 2, 3
# a_dict: dict = {}

# def sum(x: int, y: int, z: float) -> float:
#     return x + y + z


# print(sum(1, 2, 3))

# int_list: list[int] = [1, 2, 3, 4]
# str_list: list[str] = ['a', 'b', 'c']

# a_dict: dict[str, int] = {
#     "A": 0,
#     "B": 0,
# }

# a_int_set: set[int] = {1, 2, 3}

# IntegerList = list[int]  # Type alias
# int_list: IntegerList = [1, 2, 3]

# lista: list[int | str] = [1, 2, 3, "a"]

# def sum(x: int, y: float | None = None) -> float:
#     if isinstance(y, float | int):
#         return x + y
#     return x

# from collections.abc import Callable

# IntSum = Callable[[int, int], int]


# def run(func: IntSum, a: int, b: int) -> int:
#     return func(a, b)


# def sum(a: int, b: int) -> int:
#     return a + b


# print(run(sum, 1, 2))

# from typing import TypeVar

# T = TypeVar('T')


# def get_item(list: list[T], index: int) -> T:
#     return list[index]


# int_list = get_item([1, 2, 3], 1)  # int
# str_list = get_item(['a', 'b', 'c'], 1)  # str


class Person:
    def __init__(self, firstname, lastname) -> None:
        self.firstname = firstname
        self.lastname = lastname

    @property
    def full_name(self):
        return f"{self.firstname} {self.lastname}"


def say_my_name(person: Person) -> str:
    return person.full_name


print(say_my_name(Person('Charles', 'Leclerc')))
