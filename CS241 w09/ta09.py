class BalanceError(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.overage_amount =


class OutOfChecksError(Exception):
    def __init__(self, message):
        super().__init__(message)


class CheckingAccount:
    def __init__(self, starting_balance: float, num_checks: int):
        self.balance = starting_balance
        self.check_count = num_checks

        if self.balance < 0:
            raise BalanceError('Your initial balance cannot be less than 0.')
        if self.check_count < 0:
            raise OutOfChecksError('You cannot open an account with less than 0 checks.')

    '''
    @property
    def balance(self):
        return self.balance

    @balance.setter
    def balance(self, balance):
        if balance < 0:
            raise BalanceError('You cannot do that.')
    '''


    def deposit(self, amount):
        if amount < 0:
            raise ValueError('You cannot add a negative amount.')
        else:
            self.balance += amount

    def write_check(self, amount):
        self.balance -= amount
        self.check_count -= 1

        if self.balance < 0:
            raise BalanceError("Your balance is below 0.")
        elif self.check_count == 0:
            raise OutOfChecksError("You are out of checks.")

    def display(self):
        print('Balance: {}; Check count: {}'.format(self.balance, self.check_count))

    def apply_for_credit(self, amount):
        raise NotImplementedError('This functionality has not been implemented yet.')


def display_menu():
    """
    Displays the available commands.
    """
    print()
    print("Commands:")
    print(" (q)  quit - Quit")
    print(" (n)  new - Create new account")
    print(" (d)  display - Display account information")
    print(" (dd) deposit - Desposit money")
    print(" (c)  check - Write a check")
    print(" (a)  credit - Apply for credit")
    print(" (b)  balance - Change your balance")

def main():
    """
    Used to test the CheckingAccount class.
    """
    acc = None
    command = ""

    while command != "q":
        display_menu()
        command = input("Enter a command: ")

        if command == "n":
            balance = float(input("Starting balance: "))
            num_checks = int(input("Numbers of checks: "))

            acc = CheckingAccount(balance, num_checks)
        elif command == "d":
            acc.display()
        elif command == "dd":
            amount = float(input("Amount: "))
            acc.deposit(amount)
        elif command == "c":
            amount = float(input("Amount: "))

            try:
                acc.write_check(amount)
            except BalanceError as e:
                print(e)
                print('Add more balance.')
                amount = float(input("Amount: "))
                acc.deposit(amount)
            except OutOfChecksError as e:
                loop = True
                while loop:
                    answer = input("You run out of checks. Would you would like more checks? (y/n) ")
                    if answer == 'y':
                        acc.check_count += 25
                        acc.balance -= 5
                        print('25 checks have been added to your account.')
                        print('5 USD have been deducted from your balance.')
                        loop = False
                    elif answer == 'n':
                        print(e)
                        print('You cannot procede without checks on your account.')
                        print('The program will end.')
                        command = 'q'
                        loop = False
                    else:
                        print('Try again.')
            acc.display()
        elif command == "a":
            try:
                amount = float(input("Amount: "))
                acc.apply_for_credit(amount)
            except NotImplementedError as e:
                print('Try again.')
                print(e)
            except AttributeError as e:
                print(e)
                print('There is no account created. Try again.')
        elif command == 'q':
            print('The program has finished.')
        elif command == 'b1':
            print(acc.balance)
        elif command == 'b2':
            acc.balance(200)
        else:
            print('Try again.')

'''
Handle the exceptions you raised above in main so that the program does not crash. If an BalanceError is caught, display the message. If an OutOfChecks error is caught. Ask the user if they would like to buy more checks. If so, add 25 checks and deduct $5.00 from the balance.

Verify that the these exceptions are properly handled.

'''

if __name__ == "__main__":
    main()