"""
Purpose: This file is a starting point to help you practice list comprehensions.
"""


def get_part1_list():
    """
    Returns a list of the squares of the numbers [0-99], e.g., 0, 1, 4, 9, 16, 25 ...]
    """
    # TODO: Change this line to be a list comprehension
    numbers = list_1 = [n ** 2 for n in range(100)]

    return numbers


def get_part2_list():
    """
    Returns a list of the the numbers [0-99] that are divisible by either 5 or 7
    """
    # TODO: Change this line to be a list comprehension
    numbers = [n for n in range(100) if n % 5 == 0 or n % 7 == 0]

    return numbers


def get_part3_list():
    """
    Filters a list of words to return only those that are at least 4 letters long and contain an 'e'
    """
    old_words = ["tacos", "knowledge", "water", "on", "the", "I", "is", "hilarious", "tie", "coat", "white", "covenants", "phone", "rubric", "send", "restrictions"]

    # TODO: Change this line to be a list comprehension
    new_words = [word for word in old_words if len(word) > 3 and word.count('e') > 0]
    # AS A FOR LOOP
    # new_words = []
    # for word in old_words:
    #     if len(word) > 3 and word.count('e') > 0:
    #         new_words.append(word)

    return new_words


def main():
    """
    This function calls the above functions and displays their result.
    """
    print(get_part1_list())
    print(get_part2_list())
    print(get_part3_list())


if __name__ == "__main__":
    main()
