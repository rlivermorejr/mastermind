import modules.menu as m
import modules.checkGuess as checkGuess

# for api calls
import requests
# for pausing between prints
import time

# for cool banner and used for the menu
from pyfiglet import figlet_format

# import sys


__author__ = "Russell Livermore"


def getNumbers(param):
    # gets the numbers from the api
    # param 1 is for initializing numbers variable
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


# initialization for variables
# numbers = getNumbers(1)
attempts = 10
guessHist = []
count1 = 0
count2 = 0
help = "help"
quit = "quit"
restart = "restart"
continueCommand = "continue"
history = "history"
start = "start"
difficultyString = "difficulty"
startBold = "\033[1m"
endBold = "\033[0m"

# initilize game at the startGame dont pass anything
# initilize player at startGame (input name)
# at the end I can define each variable in the class
# give that player the game


class Game:
    # class for storing game variables
    def __init__(self, name, attempts, difficulty, guessHist):
        self.attempts = attempts
        self.difficulty = difficulty
        self.guessHist = guessHist


class Player:
    # class for storing player variables
    def __init__(self, name):
        self.name = name
        self.games = []


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


def askGuess(numbers, player):
    # asks for guess and checks for validity
    # as well as looks for commands
    global attempts
    print(numbers)
    if attempts == 0:
        # game = Game(attempts, difficulty, guessHist)
        print("\nOH NO!")
        time.sleep(1)
        print("\nYou have run out of attempts!")
        time.sleep(1)
        print("The correct answer was: " + str("".join(numbers)))
        print("Thanks for playing!")
        time.sleep(1)
        secondary(player)
    guess = input("\nEnter your guess...\n" +
                  "attempts remaining: " + str(attempts) + "\n" +
                  "> ")
    guess = guess.lower()
    if guess == help:
        m.commands(numbers, player)
    elif guess == history and len(guessHist) > 0:
        print(guessHist)
        time.sleep(1)
        askGuess(numbers, player)
    elif guess == history:
        print("\nno history yet!")
        time.sleep(1)
        askGuess(numbers, player)
    elif guess == quit:
        print("Goodbye!")
        time.sleep(1)
        exit()
    elif not guess.isnumeric():
        print("!!!!!! Invalid command !!!!!!\n")
        time.sleep(1)
        askGuess(numbers, player)
    checkGuess.checkGuess(guess, numbers, player)


def startGame():
    # starts the game and checks difficulty level
    global attempts
    global guessHist
    guessHist = []
    attempts = 10
    # api call depending on difficulty
    if m.difficulty == "easy":
        numbers = getNumbers(2)
    elif m.difficulty == "medium":
        numbers = getNumbers(3)
    elif m.difficulty == "hard":
        numbers = getNumbers(4)
    # starts the game
    player = Player(input("\nEnter your name...\n> "))
    print("\nHere are the rules:")
    print(f"You have to guess the {len(numbers)}-digit code.\n" +
          "You have 10 tries to do it.\n" + "The code is made up of numbers 0-7.\n")
    # time.sleep(3)
    print("The numbers can be" + startBold + " repeated." + endBold)
    # time.sleep(2)
    print("The numbers can be in" + startBold + " any order." + endBold)
    # time.sleep(2)
    print("You can enter" + startBold + " quit" + endBold +
          " at anytime to exit the game.")
    # time.sleep(2)
    print("or you can enter" + startBold + " help" + endBold +
          " at anytime for the menu.")
    # time.sleep(2)
    print("Difficulty is set to: " + m.difficulty)
    print("Good luck!")
    print("numbers" + ": " + str(numbers))
    # time.sleep(2)
    askGuess(numbers, player)

# input ask for name
# compare input to names of Player class
# if existing continue instance of player


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
    if usr == help:
        m.preStart()
    if usr == quit:
        print("Goodbye!")
        time.sleep(1)
        exit()
    if usr == start:
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
    # time.sleep(1)
    print(mind)
    # time.sleep(1)
    welcome = ("Welcome to Master Mind!\nhelp = game menu\nquit = \
exit game\nstart = start game")
    print(welcome)
    # 'types' out welcome message
    # for letter in welcome:
    #     time.sleep(0.1)
    #     sys.stdout.write(letter)
    #     sys.stdout.flush()
    usr = input("\n> ")
    usr = usr.lower()
    if usr == help:
        m.preStart()
    if usr == quit:
        print("Goodbye!")
        time.sleep(1)
        exit()
    if usr == start:
        startGame()
    else:
        print("\n!!!!!! Invalid command !!!!!!\n")
        time.sleep(1)
        secondary()


if __name__ == '__main__':
    main()
