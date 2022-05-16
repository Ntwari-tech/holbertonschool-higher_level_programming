#!/usr/bin/python3
""" this module is for add_integer function """


def add_integer(a, b=98):
    """
    value a added to value b, return sum
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    add_int = a + b
    if type(add_int) is float:
        return int(add_int)
    return add_int
