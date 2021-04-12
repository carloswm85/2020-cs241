import random
from random import randint

print("Welcome to the number guessing game!")
seed = input("Enter random seed: ")

random.seed(seed)
play = True

while play:
    guessed = False
    tries = 1
    num_random = randint(1, 100)

    while not guessed:
        print()
        user_guess_input = input("Please enter a guess: ")
        user_guess_int = int(user_guess_input)
        if user_guess_int > num_random:
            print("Lower")
        elif user_guess_int < num_random:
            print("Higher")
        else:
            print("Congratulations. You guessed it!")
            print("It took you " + str(tries) + " guesses.")
            guessed = True
        tries += 1
    print()
    answer = input("Would you like to play again (yes/no)? ")
    if answer == 'no':
        play = False
        
print("Thank you. Goodbye.")