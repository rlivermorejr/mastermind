# for api calls
import requests
# for pausing between prints
import time
# for cool banner
from pyfiglet import figlet_format
# for the cool menu
from simple_term_menu import TerminalMenu

import sys


__author__ = "Russell Livermore"

# initializes difficulty variable
difficulty = "easy"


def getNumbers(param):
    # gets the numbers from the api
    # param 1 is for initializating numbers variable
    # 2, 3, and 4 are easy, medium, and hard respectively
    if param == 1:
        pass
    if param == 2:
        params = requests.get(
            "https://www.random.org/integers/?num=4&min=0&max=7&col=1&base=10&format=plain&rnd=new")
        num = params.text.split()
        return num
    if param == 3:
        params = requests.get(
            "https://www.random.org/integers/?num=6&min=0&max=7&col=1&base=10&format=plain&rnd=new")
        num = params.text.split()
        return num
    if param == 4:
        params = requests.get(
            "https://www.random.org/integers/?num=8&min=0&max=7&col=1&base=10&format=plain&rnd=new")
        num = params.text.split()
        return num


# initialization for rest of variables
numbers = getNumbers(1)
attempts = 10
guessHist = []
count1 = 0
count2 = 0


def commands():
    # help menu for when game is already started
    global attempts
    print(figlet_format("Menu", font='smkeyboard'))
    options = ["quit", "history", "restart", "continue"]
    terminal_menu = TerminalMenu(options)
    menu_entry_index = terminal_menu.show()
    if options[menu_entry_index] == "quit":
        print("Goodbye!")
        time.sleep(1)
        exit()
    elif options[menu_entry_index] == "history":
        if len(guessHist) == 0:
            print("\nno history yet!")
            time.sleep(1)
            commands()
        else:
            print("\n" + str(guessHist) + "\n")
            time.sleep(1)
            commands()
    elif options[menu_entry_index] == "continue":
        askGuess()
    elif options[menu_entry_index] == "restart":
        attempts = 10
        startGame()


def preStart():
    # help menu for before the game is started
    print(figlet_format("Menu", font='smkeyboard'))
    options = ["start", "quit", "difficulty"]
    terminal_menu = TerminalMenu(options)
    menu_entry_index = terminal_menu.show()
    if options[menu_entry_index] == "start":
        print("start")
        startGame()
    elif options[menu_entry_index] == "quit":
        print("Goodbye!")
        time.sleep(1)
        exit()
    elif options[menu_entry_index] == "difficulty":
        setDifficulty()


def setDifficulty():
    # menu for setting difficulty
    global difficulty
    options = ["easy", "medium", "hard"]
    terminal_menu = TerminalMenu(options)
    menu_entry_index = terminal_menu.show()
    if options[menu_entry_index] == "easy":
        difficulty = "easy"
        print("\nDifficulty set to easy.")
        time.sleep(1)
        secondary()
    elif options[menu_entry_index] == "medium":
        difficulty = "medium"
        print("\nDifficulty set to medium.")
        time.sleep(1)
        secondary()
    elif options[menu_entry_index] == "hard":
        difficulty = "hard"
        print("\nDifficulty set to hard.")
        time.sleep(1)
        secondary()


def checkForDupe(num1, num2):
    # checks for a double count
    # only implemented for easy atm
    global count1
    global count2
    if num1 == 3 and num2 == 1 and difficulty == "easy":
        count1 - 1
        count2 = 0


def countAttempts():
    # decrements attempts
    global attempts
    attempts -= 1
    return attempts


def countX(param):
    # counts the number of matching numbers
    # param 1 is for matching number with correct index
    # param 2 is for matching number but wrong index
    global count1
    global count2
    if param == 1:
        count1 += 1
        return count1
    if param == 2:
        count2 += 1
        return count2


def askGuess():
    # asks for guess and checks for validity
    # as well as looks for commands
    global attempts
    if attempts == 0:
        print("OH NO!")
        time.sleep(1)
        print("\nYou have run out of attempts!")
        time.sleep(1)
        print("The correct answer was: " + str(numbers))
        print("Thanks for playing!")
        time.sleep(1)
        secondary()
    guess = input("\nEnter your guess...\n" +
                  "attempts remaining: " + str(attempts) + "\n" +
                  "> ")
    guess = guess.lower()
    if guess == "help":
        commands()
    elif guess == "history" and len(guessHist) > 0:
        print(guessHist)
        time.sleep(1)
        askGuess()
    elif guess == "history":
        print("\nno history yet!")
        time.sleep(1)
        askGuess()
    elif guess == "quit":
        print("Goodbye!")
        time.sleep(1)
        exit()
    elif not guess.isnumeric():
        print("!!!!!! Invalid command !!!!!!\n")
        time.sleep(1)
        askGuess()
    checkGuess(guess)


def checkGuess(guess):
    # logic for checking guess
    global attempts
    global guessHist
    global count1
    global count2
    global numbers
    count1 = 0
    count2 = 0
    arrGuess = list(guess)
    arrNums = list(numbers)
    # correct length check
    if len(guess) != len(numbers):
        print("Incorrect amount of numbers entered!")
        time.sleep(1)
        askGuess()
    # check for duplicate guess
    if guess in guessHist:
        print("You already guessed that!")
        time.sleep(1)
        askGuess()
    # immediate win check
    if (attempts == 10 and arrGuess == arrNums):
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
        secondary()
    # check for win
    if (arrGuess == arrNums):
        print("You guessed the code correctly!")
        time.sleep(1)
        print("Only took you " + str(10 - attempts) + " attempt(s)!")
        time.sleep(1)
        secondary()
    else:
        for i in range(0, len(arrGuess)):
            if arrGuess[i] == "8" or arrGuess[i] == "9":
                print("The random number cannot have an 8 or 9!")
                time.sleep(1)
                print("Only numbers from 1 to 7 are allowed!")
                time.sleep(1)
                print("Please try again!")
                time.sleep(1)
                askGuess()
            if arrGuess[i] in arrNums and arrGuess[i] != arrNums[i]:
                # if the guess is in the code and is not in the correct index
                countX(2)
            if arrGuess[i] == arrNums[i]:
                # if the guess is in the code and is in the correct index
                countX(1)
        # append to history, decrement attempts, and check for duplicate count
        guessHist.append(guess)
        countAttempts()
        checkForDupe(count1, count2)
        # prints the correct message depending on
        # the amount of matching numbers
        # and depending on if any match the correct index
        if count1 == 0 and count2 == 0:
            print("You guessed incorrectly!")
        if count2 == 1 and count1 == 0:
            # one number right, incorrect index
            print("You guessed a number correctly!")
        if count2 > 1 and count1 == 0:
            # multiple numbers right, incorrect index
            print("You guessed a few numbers correctly!")
        if count1 > 0 and count2 == 0:
            # multiple numbers right, correct index
            print("You guessed a number correctly and at the correct index!")
            print("Number(s) at correct index: " + str(count1))
            print("Number(s) at incorrect index: " + str(count2))
        if count1 > 0 and count2 > 0:
            # multiple numbers right, some correct index and some incorrect index
            print("You guessed a number correctly and at the correct index!")
            print("Number(s) at correct index: " + str(count1))
            print("Number(s) at incorrect index: " + str(count2))
        askGuess()


def startGame():
    # starts the game and checks difficulty level
    global numbers
    global difficulty
    global attempts
    global guessHist
    guessHist = []
    attempts = 10
    if difficulty == "easy":
        numbers = getNumbers(2)
    elif difficulty == "medium":
        numbers = getNumbers(3)
    elif difficulty == "hard":
        numbers = getNumbers(4)
    # starts the game
    print("\nHere are the rules:")
    print(f"You have to guess the {len(numbers)}-digit code.\n" +
          "You have 10 tries to do it.\n" + "The code is made up of numbers 0-7.\n")
    time.sleep(3)
    print("The numbers can be" + "\033[1m" + " repeated." + "\033[0m")
    time.sleep(2)
    print("The numbers can be in" + "\033[1m" + " any order." + "\033[0m")
    time.sleep(2)
    print("You can enter" + "\033[1m" +
          " quit" + "\033[0m" + " at anytime to exit the game.")
    time.sleep(2)
    print("or you can enter" + "\033[1m" +
          " help" + "\033[0m" + " at anytime for the menu.")
    time.sleep(2)
    print("Good luck!")
    time.sleep(2)
    askGuess()


def secondary():
    # secondary main function
    # this is for when you are sent back to the main menu
    # and avoid the begining 'animations' replaying
    print("\nWelcome to Master Mind!")
    print("help = game menu")
    print("quit = exit game")
    print("start = start game")
    usr = input("\n> ")
    usr = usr.lower()
    if usr == "help":
        preStart()
    if usr == "quit":
        print("Goodbye!")
        time.sleep(1)
        exit()
    if usr == "start":
        startGame()
    else:
        print("\n!!!!!! Invalid command !!!!!!\n")
        time.sleep(1)
        secondary()


def main():
    # main function
    master = figlet_format("Master", font='isometric4', width=200)
    mind = figlet_format("Mind", font='isometric2')
    print(master)
    time.sleep(1)
    print(mind)
    time.sleep(1)
    welcome = "Welcome to Master Mind!\nhelp = game menu\nquit = exit game\nstart = start game"
    # 'types' out welcome message
    for letter in welcome:
        time.sleep(0.1)
        sys.stdout.write(letter)
        sys.stdout.flush()
    usr = input("\n> ")
    usr = usr.lower()
    if usr == "help":
        preStart()
    if usr == "quit":
        print("Goodbye!")
        time.sleep(1)
        exit()
    if usr == "start":
        startGame()
    else:
        print("\n!!!!!! Invalid command !!!!!!\n")
        time.sleep(1)
        secondary()


if __name__ == '__main__':
    main()
