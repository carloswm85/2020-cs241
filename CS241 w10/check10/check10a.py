"""
File: sorting.py
Original Author: Br. Burton, designed to be completed by others.

Sorts a list of numbers.
"""


def sort(numbers):
    """
    Fill in this method to sort the list of numbers
    # BUBBLE SORT METHOD
    """
    for number_pass in range(len(numbers) - 1, 0, -1):
        # start: 9 - 1 = 8
        # end: 0
        # step: -1
        # print('number_pass: {} of {}'.format(number_pass, len(numbers) - 1))
        for iteration in range(number_pass):
            # from 0 to 7
            # print('iteration: {}'.format(iteration))
            if numbers[iteration] > numbers[iteration + 1]:
                temp = numbers[iteration]
                numbers[iteration] = numbers[iteration + 1]
                numbers[iteration + 1] = temp

    # print(numbers)


def prompt_for_numbers():
    """
    Prompts the user for a list of numbers and returns it.
    :return: The list of numbers.
    """

    numbers = []
    print("Enter a series of numbers, with -1 to quit")

    num = 0

    while num != -1:
        num = int(input())

        if num != -1:
            numbers.append(num)

    return numbers


def display(numbers):
    """
    Displays the numbers in the list
    """
    print("The list is:")
    for num in numbers:
        print(num)


def main():
    """
    Tests the sorting process
    """
    numbers = prompt_for_numbers()
    sort(numbers)
    display(numbers)


if __name__ == "__main__":
    main()
