import math

class Rational:
    def __init__(self):
        self.numerator = 0
        self.denominator = 1
    def prompt(self):
        self.numerator = int(input("Enter the numerator:"))
        self.denominator = int(input("Enter the denominator:"))
    def display(self):
        # print("{}/{}".format(self.numerator, self.denominator))
        if self.numerator > self.denominator:
            # Improper fraction
            coefficient = self.numerator / self.denominator
            remainder = self.numerator % self.denominator
            print(str(math.floor(coefficient)) + ' ' + str(remainder) + '/' + str(self.denominator))
        elif self.numerator < self.denominator:
            # Proper fraction
            print(str(self.numerator) + '/' + str(self.denominator))
        else:
            # No fraction
            print(self.numerator)  
    def display_decimal(self):
        decimal = self.numerator / self.denominator
        print("{:.2f}".format(decimal))
    def multiply_by(self, rational_factor):
        self.numerator = self.numerator * rational_factor.numerator
        self.denominator = self.denominator * rational_factor.denominator

def main():
    fraction = Rational()
    fraction.display()
    fraction.prompt()
    fraction.display()
    fraction.display_decimal()
    fraction_2 = Rational()
    fraction_2.prompt()
    fraction_2.display()
    fraction_2.display_decimal()
    print('Time to multiply!')
    fraction.multiply_by(fraction_2)
    fraction.display()
    
# If this is the file being run, call our main function
if __name__ == "__main__":
    main()