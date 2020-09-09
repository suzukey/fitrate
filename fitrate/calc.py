import math
import operator
from functools import reduce


def calc(sizes, max_volume, dimension=2, is_int=True):
    """
    Calculate the length of the sides that fit into the maximum volume
    """
    divisor = gcd(*sizes)

    weights = [(size / divisor) for size in sizes]
    total_weights = prod(*weights)

    x_nth_power = max_volume / total_weights
    x_nth_root = math.pow(x_nth_power, 1 / dimension)

    sides_length = [
        int(weight * x_nth_root) if is_int else (weight * x_nth_root)
        for weight in weights
    ]

    return tuple(sides_length)


def prod(*numbers):
    """
    Calculate the total product from numbers
    """
    return reduce(operator.mul, numbers)


def gcd(*numbers):
    """
    Calculate the greatest common divisor from numbers
    """
    return reduce(math.gcd, numbers)
