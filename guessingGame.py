import random

name = "Number guessing game"
no = random.randint(1,9)
chances = 0 

print(name)
print("Guess The No between 1 and 9")

while chances < 5:
    guess = int(input ("Enter ur guess"))

    if guess == no:
        print("Congratulation You Won!!")
        break

    elif guess > no:
        print("Your guess is grater than the no")
        
    else:
        print("Your guess is lower than the no")

    chances = chances+1

if not chances < 5:
        print("You Lose!! The Number is", no)