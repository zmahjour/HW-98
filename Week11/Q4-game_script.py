import argparse
import random


parser = argparse.ArgumentParser()

parser.add_argument('-s', type=int, default=0)
parser.add_argument('-e', type=int, default=100)
parser.add_argument('-g', type=int, default=5)

args = parser.parse_args()

correct_num = random.randint(args.s, args.e)
guess = None

for i in range(args.g):
    guess = int(input("What is your guess? "))

    if guess < correct_num:
        print("Your number is small")
    elif guess > correct_num:
        print("Your number is large")
    else:
        print("Congratulations; you won!")
        break

if guess != correct_num:
    print("Sorry; you lost the game")