"""
File: ta10-solution.py
Author: Br. Burton

This file demonstrates the merge sort algorithm. There
are efficiencies that could be added, but this approach is
made to demonstrate clarity.
"""

# MERGE SORT!

from random import randint

MAX_NUM = 100


def merge_sort(items):
    """
    Sorts the items in the list
    :param items: The list to sort
    """
    print('Argument:', items)

    if len(items) > 1:
        print("SPLITTING")
        mid = len(items) // 2
        lefthalf = items[:mid]
        righthalf = items[mid:]
        print('Splitted')
        print('lefthalf is: ', lefthalf)
        print('righthalf is: ', righthalf)

        print()
        print('Entering LEFTsorting')
        merge_sort(lefthalf)
        print('→ end LEFT basecase reached')

        print()
        print('Entering RIGHTsorting')
        merge_sort(righthalf)
        print('→ end RIGHT basecase reached')
        print()

        print('Merging items:')
        i = 0  # left
        j = 0  # right
        k = 0  # items

        while i < len(lefthalf) and j < len(righthalf):
            print('- Entering LOOP #1')
            print('Overriding list[{}]'.format(k))
            if lefthalf[i] <= righthalf[j]:
                print('left <= right')
                print('Overriding list[{}] with lefthalf[{}] = {}'.format(k, i, lefthalf[i]))
                items[k] = lefthalf[i]
                i += 1
            else:
                print('left > right')
                print('Overriding list[{}] with righthalf[{}] = {}'.format(k, j, righthalf[j]))
                items[k] = righthalf[j]
                j += 1
            k += 1
            print('Merged', items)

        while i < len(lefthalf):
            print('- Entering LOOP #2')
            print('Overriding list[{}] with lefthalf[{}] = {}'.format(k, i, lefthalf[i]))
            items[k] = lefthalf[i]
            i += 1
            k += 1
            print('Merged', items)

        while j < len(righthalf):
            print('- Entering LOOP #3')
            print('Overriding list[{}] with righthalf[{}] = {}'.format(k, j, righthalf[j]))
            items[k] = righthalf[j]
            j += 1
            k += 1
            print('Merged', items)

    else:
        print('Base case reached. len(currentList) < 2')

    print('Return (end of method).')


def generate_list(size):
    """
    Generates a list of random numbers.
    """
    items = [randint(0, MAX_NUM) for i in range(size)]
    return items


def display_list(items):
    """
    Displays a list
    """
    for item in items:
        print(item)


def main():
    """
    Tests the merge sort
    """
    size = int(input("Enter size: "))
    print()

    items = generate_list(size)
    merge_sort(items)

    print('\nMAIN function.')
    print("The Sorted list is:")
    display_list(items)


if __name__ == "__main__":
    main()
