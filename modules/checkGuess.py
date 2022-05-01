# import modules/objects
import mastermind as mm
# for cool banner and used for the menu
from pyfiglet import figlet_format

import time


def checkGuess(guess, numbers, player):
    # logic for checking guess
    global attempts
    global guessHist
    global count1
    global count2
    mm.count1 = 0
    mm.count2 = 0
    arrGuess = list(guess)
    arrNums = list(numbers)
    # correct length check
    if len(guess) != len(numbers):
        print("Incorrect amount of numbers entered!")
        time.sleep(1)
        mm.askGuess(numbers, player)
    # check for duplicate guess
    if guess in mm.guessHist:
        print("You already guessed that!")
        time.sleep(1)
        mm.askGuess(numbers, player)
    # immediate win check
    if (mm.attempts == 10 and arrGuess == arrNums):
        print("You guessed the code correctly and in one attempt!")
        youre = figlet_format("You're a", font='larry3d')
        master = figlet_format("Master", font='larry3d', width=200)
        mind = figlet_format("Mind", font='larry3d')
        print(youre)
        time.sleep(2)
        print(master)
        time.sleep(1)
        print(mind)
        time.sleep(1)
        mm.secondary()
    # check for win
    if (arrGuess == arrNums):
        print("You guessed the code correctly!")
        time.sleep(1)
        print("Only took you " + str(10 - mm.attempts) + " attempt(s)!")
        time.sleep(1)
        mm.secondary()
    else:
        for i in range(0, len(arrGuess)):
            if arrGuess[i] == "8" or arrGuess[i] == "9":
                print("The random number cannot have an 8 or 9!")
                time.sleep(1)
                print("Only numbers from 1 to 7 are allowed!")
                time.sleep(1)
                print("Please try again!")
                time.sleep(1)
                mm.askGuess(numbers, player)
            if arrGuess[i] == arrNums[i]:
                # if the guess is in the code and is in the correct index
                mm.countX(1)
            else:
                if arrGuess[i] in arrNums and arrGuess[i] != arrNums[i]:
                    # if the guess is in the code and is not in the correct index
                    mm.countX(2)
        # append to history, decrement attempts, and check for duplicate count
        mm.guessHist.append(guess)
        mm.countAttempts()
        # prints the correct message depending on
        # the amount of matching numbers
        # and depending on if any match the correct index
        if mm.count1 == 0 and mm.count2 == 0:
            print("You guessed incorrectly!")
        if mm.count2 == 1 and mm.count1 == 0:
            # one number right, incorrect index
            print("You guessed a number correctly!")
        if mm.count2 > 1 and mm.count1 == 0:
            # multiple numbers right, incorrect index
            print("You guessed a few numbers correctly!")
        if mm.count1 > 0 and mm.count2 == 0:
            # multiple numbers right, correct index
            print("You guessed a number correctly and at the correct index!")
            print("Number(s) at correct index: " + str(mm.count1))
            print("Number(s) at incorrect index: " + str(mm.count2))
        if mm.count1 > 0 and mm.count2 > 0:
            # multiple numbers right, some correct index and some incorrect index
            print("You guessed a number correctly and at the correct index!")
            print("Number(s) at correct index: " + str(mm.count1))
            print("Number(s) at incorrect index: " + str(mm.count2))
        mm.askGuess(numbers, player)
