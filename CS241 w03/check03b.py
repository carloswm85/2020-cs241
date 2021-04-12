''' COMPLEX NUMBERS '''

class Complex:
    def __init__(self):
        self.real = 0
        self.imaginary = 0
    
    def prompt(self):
        self.real = input('\nPlease enter the real part: ')
        self.imaginary = input('Please enter the imaginary part: ')
    
    def display(self):
        print(str(self.real) + ' + ' + str(self.imaginary) + 'i')
        
def main():
    complex_a = Complex()
    complex_b = Complex()
    print("The values are:")
    complex_a.display()
    complex_b.display()
    complex_a.prompt()
    complex_b.prompt()
    print("\nThe values are:")
    complex_a.display()
    complex_b.display()
        

if __name__ == "__main__":
    main()