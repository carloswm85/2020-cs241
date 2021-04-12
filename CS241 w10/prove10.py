numbers = [12, 18, 128, 48, 2348, 21, 18, 3, 2, 42, 96, 11, 42, 12, 18]
print(numbers)

# Insert the number 5 to the beginning of the list.
numbers.insert(0, 5)
print(numbers)

# Remove the number 2348 based on its value (as opposed to a hard-coded index of 4) from the list.
numbers.remove(2348)
print(numbers)

# Create a second list of 5 different numbers and add them to the end of the list in one step. (Make sure it adds the
# numbers to the list such as: [1, 2, 3, 4, 5] not as a sub list, such as [1, 2, 3, [4, 5]] ).
more_numbers = [1, 2, 3, 4, 5]
numbers.extend(more_numbers)
print(numbers)

# Sort the list using the built in sorting algorithm.
numbers.sort()
print(numbers)

# Sort the list backwards using the built in sorting algorithm.
numbers.sort(reverse=True)
print(numbers)

# Use a built-in function to count the number of 12's in the list.
count = numbers.count(12)
print(count)

# Use a built-in function to find the index of the number 96.
index = numbers.index(96)
print(index)

# Use slicing to get the first half of the list, then get the second half of the list and make sure that nothing was
# left out or duplicated in the middle.
print(len(numbers))
middle = len(numbers) // 2
first_half = numbers[:middle]
# numbers[inclusive:exclusive]
print(len(first_half), first_half)
second_half = numbers[middle:]
print(len(second_half), second_half)

# Use slicing to create a new list that has every other item from the original list (i.e., skip elements,
# using the step functionality).
every_other = numbers[0:len(numbers) - 1:2]
print(every_other)

# Use slicing to get the last 5 items of the list. For this, please use negative number indexing.
print(numbers)
last_5 = numbers[:-6:-1]
print(last_5)

