import argparse
import random


parser = argparse.ArgumentParser()

parser.add_argument('-s', type=int, default=0)
parser.add_argument('-e', type=int, default=100)
parser.add_argument('-g', type=int, default=5)

args = parser.parse_args()

correct_num = random.randint(0, 100)
guess = None

for i in range(5):
    guess = int(input("What is your guess? "))

    if guess < correct_num:
        print("Enter Higher Number")
    elif guess > correct_num:
        print("Enter Lower Number")
    else:
        print("Congratulations; you won!")
        break

if guess != correct_num:
    print("Sorry; you lost the game")