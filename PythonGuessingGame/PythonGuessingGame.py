
# The python version of guessing game
# Completed by Ehan Masud on 1/7/2023
# Goal: Find the number in 5 or less guesses

import random

randomnumber = random.randint(0,100)
inputnumber = 0
guesses = 0
notplaying = False

print("Welcome to Guessing Game (Python edition)")
print("Your goal is to guess a number between 1-100 in only 5 guesses.")
print("Good luck!")
print("---------------------------------------------")

while notplaying != True:
    
    if guesses > 5:
        print("You lose....")
        print("Play again? (Y/N): ")
        again = input()
        if again == 'Y':
            randomnumber = random.randint(0,100)
            guesses = 0
            continue
        else:
            notplaying = True
            print("Thanks for playing!")

    print("Guess a number: ")
    inputnumber = int(input())
    guesses += 1

    if inputnumber < randomnumber:
        print("Too low!")
    elif inputnumber > randomnumber:
        print("Too high!")
    else:
        print("You got it! You win!")
        print("It took you " + str(guesses) + " guesses!")
        print("Play again? (Y/N): ")
        again = input()
        if again == 'Y':
            randomnumber = random.randint(0,100)
            guesses = 0
            continue
        else:
            notplaying = True
            print("Thank you for playing!")



