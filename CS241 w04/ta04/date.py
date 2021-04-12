import datetime

class Date:
    def __init__(self):
        self.day = 1
        self.month = 1
        self.year = 2000
        
    def prompt(self):
        receiving_values = True
        while receiving_values:
            try:
                self.day = int(input("Day: "))
                self.month = int(input("Month: "))
                self.year = int(input("Year: "))
                while (self.month < 0 or self.month > 12) or self.year < 2001:
                    print('Enter correct values for months, and a year higher than 2000.')
                    try:
                        self.day = int(input("Day: "))
                        self.month = int(input("Month: "))
                        self.year = int(input("Year: "))
                    except ValueError:
                        print("That's not a number")
                receiving_values = False
            except ValueError:
                print("That's not a number. Try again prompting the values.")
                
    def display(self):
        print("{:02d}/{:02d}/{:d}".format(self.month, self.day, self.year))
        
    def display_long(self):
        long_date = datetime.datetime(self.year, self.month, self.day)
        long_date_display = long_date.strftime('%B %d, %Y')
        print(long_date_display)
