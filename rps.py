"""We are going to create a rock paper and scissors game."""
import random
user = input("What is your choice? 'r' for rock, 'p' for paper or 's' for sissor - ")
computer = random.choice(['r', 'p', 's'])

if user == computer:
    print(f'It is a tie!')
elif (user == 'r' and computer == 'p') or (user == 'p' and computer == 'r') or (user == 's' and computer == 'p'):
    print("You won!")
elif(computer == 'r' and user == 'p') or (computer == 'p' and user == 'r') or (computer == 's' and computer == 'p'):
    print("The computer won!")