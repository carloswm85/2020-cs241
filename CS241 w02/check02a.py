def main():
    addition = 0
    addition = compute_sum()
    print("The sum is:", addition)
    
def prompt_number():
    number = -1
    while(number < 0):
        number = int(input("Enter a positive number: "))
        if number < 0:
            print("Invalid entry. The number must be positive.")
            return prompt_number()
        else:
            print()
            return number

def compute_sum():
    numbers = 0
    addition = 0
    while numbers < 3:
        addition += prompt_number()
        numbers += 1
    return addition

main()
    