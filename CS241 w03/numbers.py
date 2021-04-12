def main():
    odd_numbers = []
    even_numbers = list()
    run = True
    time = 0
    while run:
        user_input = input("\nEnter a number (0 to quit): ")
        if user_input.isdigit() and int(user_input) == 0:
            run = False
            print('\nEven numbers:')
            for even in even_numbers:
                print(even)
            print('\nOdd numbers:')
            for odd in odd_numbers:
                print(odd)
            print('\nEnd of program.')
        elif user_input.isdigit() and int(user_input) > 0:
            number = int(user_input)
            if number % 2 == 0:
                even_numbers.append(number)
            else:
                odd_numbers.append(number)
            print(int(user_input))
        else:
            print('The number is not an integer greater or equal to 0.')

if __name__ == '__main__':
    main()