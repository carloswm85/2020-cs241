"""
File: ta10-solution.py
Author: Br. Burton

This file demonstrates the merge sort algorithm. There
are efficiencies that could be added, but this approach is
made to demonstrate clarity.
"""

from random import randint

MAX_NUM = 100


def quick_sort(items):
    print('QUICK SORT')
    print('items → ', items)
    """
    Sorts the items in the list
    :param items: The list to sort
    """
    print('len(items)       → {}'.format(len(items)))
    print('len(items) - 1   → {}'.format(len(items) - 1))
    quickSortHelper(items, 0, len(items) - 1)
    print()
    print('End QUICK SORT.')


def quickSortHelper(items, first, last):
    print()
    print('QUICK SORT HELPER')
    print('items → {}'.format(items))
    print('first: {}'.format(first))
    print('last: {}'.format(last))
    print('first < last')
    if first < last:
        print('Entering BaseCase → GO Partition')
        split_point = partition(items, first, last)

        print()
        print('len(items) - 1 → {}'.format(split_point - 1))
        print('len(items) + 1 → {}'.format(split_point + 1))
        quickSortHelper(items, first, split_point - 1)
        quickSortHelper(items, split_point + 1, last)
    else:
        print('BaseCase reached: first is NOT less than last')
    print('Return QUICK SORT HELPER.')


def partition(items, first, last):
    print()
    print('PARTITION')
    print('items → {}'.format(items))
    print('first: {}'.format(first))
    print('last: {}'.format(last))
    pivot_value = items[first]
    print('pivot_value: {}'.format(pivot_value))

    left_mark = first + 1
    right_mark = last
    print('left_mark: {}'.format(left_mark))
    print('right_mark: {}'.format(right_mark))

    done = False
    while not done:
        print('- MAIN WHILE')

        print('→ WHILE #1')
        print('left_mark <= right_mark AND items[left_mark] <= pivot_value')
        print(left_mark, ' <=', right_mark, ' AND ', items[left_mark], ' <= ', pivot_value)
        while left_mark <= right_mark and items[left_mark] <= pivot_value:
            print('while #1')
            left_mark = left_mark + 1

        print('→ WHILE #2')
        print('items[right_mark] >= pivot_value AND right_mark >= left_mark')
        print(items[right_mark], ' >= ', pivot_value, ' AND ', right_mark, ' <= ', left_mark)
        while items[right_mark] >= pivot_value and right_mark >= left_mark:
            print('while #2')
            right_mark = right_mark - 1
            print(items[right_mark], ' >= ', pivot_value, ' AND ', right_mark, ' <= ', left_mark)

        if right_mark < left_mark:
            print('→ DONE condition: right_mark < left_mark')
            print('left_mark: {}'.format(left_mark))
            print('right_mark: {}'.format(right_mark))
            done = True
        else:
            print('else:')
            temp = items[left_mark]
            items[left_mark] = items[right_mark]
            items[right_mark] = temp

    temp = items[first]
    items[first] = items[right_mark]
    items[right_mark] = temp

    print('Return PARTITION, and rigth_mark: {}.'.format(right_mark))
    return right_mark


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

    items = generate_list(size)
    quick_sort(items)

    print("\nThe Sorted list is:")
    display_list(items)


if __name__ == "__main__":
    main()
