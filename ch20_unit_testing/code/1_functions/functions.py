"""
    Testing functions
"""
from typing import Tuple, Union


def divide(dividend: Union[int, float], divisor: Union[int, float]):
    """divide function"""
    if divisor == 0:
        raise ValueError("The divisor cannot be zero.")

    return dividend / divisor


def multiply(*args: Tuple[Union[int, float]]):
    """multiply function"""
    if len(args) == 0:
        raise ValueError("At least one value to multiply must be passed.")
    total = 1
    for arg in args:
        total *= arg

    return total
