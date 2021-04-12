
class NegativeNumberError(Exception):
    def __init__(self, message):
        super().__init__(message)


def get_inverse(n):
    number = int(n)
    if number == 0:
        raise ZeroDivisionError('n is 0')
    elif number < 0:
        raise NegativeNumberError('n is less than 0')
    elif type(number) is not int:
        raise ValueError('n is not a number')
    else:
        return 1 / number


def main():
    value = input('Enter a number: ')
    try:
        returned_value = get_inverse(value)
    except ValueError:
        print('Error: The value must be a number')
    except ZeroDivisionError:
        print('Error: Cannot divide by zero')
    except NegativeNumberError:
        print('Error: The value cannot be negative')
    else:
        print('The result is: {}'.format(returned_value))


if __name__ == '__main__':
    main()