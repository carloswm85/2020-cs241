error = True

while error:
    try:
        number = int(input('Enter a number: '))
        print('The result is: {}'.format(number * 2))
        error = False
    except ValueError:
        print('The value entered is not valid')