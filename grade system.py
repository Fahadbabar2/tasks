import random

number = random.randint(1, 100)
guess = None

while guess != number:
    guess = int(input("Guess a number between 1 and 100: "))
    if guess < number:
        print("very low")
    elif guess > number:
        print("To high")
    else:
        print("Correct its right")
