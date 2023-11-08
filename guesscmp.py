"""We, the user will have a secret number and the computer will try to guess the sectret number."""
import random
def computer_guess(x):
    low = 1
    high = 17
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        feedback = input(f"Is the {guess} too high(h), or too low(l) or correct(c)")
        if feedback == 'l':
            low = guess - 1
        elif feedback == 'h':
            high = guess + 1
        elif feedback == 'c':
            break
    print("The computer finally guessed the number!")

computer_guess(7)