"""This is a guessing game where the computer has a number and the user has to guess the number."""
import random
guessing = True
random_number = random.randint(1, 17)
while guessing:
    number = int(input("Guess the number: "))
    if number != random_number:
        print(f'Oops...wrong guess try again!')
    elif number == random_number:
        guessing = False
        print("You guessed the number right!")