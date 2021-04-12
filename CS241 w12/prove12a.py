"""
Purpose: This file is a starting point to help you practice using lambda functions.
Use functions: filter, map, reduce.
"""

import functools
from functools import reduce


# FILTER
def get_part1_list():
    """
    Filters a list to return even numbers greater than 33.
    """
    numbers = [x for x in range(100)]

    # TODO: Write a line here that uses filter and a lambda function to filter
    # the list so that it only contains even numbers greater than 33.
    new_numbers = list(filter(lambda x: x % 2 != 0 and x > 33, numbers))

    # list([iterable])
    # The list() constructor returns a list in Python.

    return new_numbers


# MAP
def get_part2_list():
    """
    Maps a lambda function to a list to square each number and add one.
    """
    numbers = [x for x in range(100)]

    # TODO: Write a line here than uses map and a lambda function to go through
    # each number in the list, square it and then add one to the result
    new_numbers = list(map(lambda x: x**2 +1, numbers))

    return new_numbers


# REDUCE
def get_part3_list():
    """
    Reduces a list to its product
    """
    numbers = [x for x in range(1, 100)]

    # TODO: Write a line here that uses reduce and a lambda function to
    # multiply all the numbers in the list together and return the product
    product = reduce(lambda x, y: x * y, numbers)

    return product


def main():
    """
    This function calls the above functions and displays their result.
    """
    print(get_part1_list())
    print(get_part2_list())
    print(get_part3_list())


if __name__ == "__main__":
    main()
