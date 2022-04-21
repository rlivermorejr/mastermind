import time

# for cool banner and used for the menu
from pyfiglet import figlet_format
# for the cool menu
from simple_term_menu import TerminalMenu
# import modules/objects
from mastermind import (quit, startGame, setDifficulty, difficultyString,
                        start, history, continueCommand, restart, guessHist,
                        askGuess)


def commands():
    # help menu for when game is already started
    global attempts
    print(figlet_format("Menu", font='smkeyboard'))
    options = [quit, history, restart, continueCommand]
    terminal_menu = TerminalMenu(options)
    menu_entry_index = terminal_menu.show()
    if options[menu_entry_index] == quit:
        print("Goodbye!")
        time.sleep(1)
        exit()
    elif options[menu_entry_index] == history:
        if len(guessHist) == 0:
            print("\nno history yet!")
            time.sleep(1)
            commands()
        else:
            print("\n" + str(guessHist) + "\n")
            time.sleep(1)
            commands()
    elif options[menu_entry_index] == continueCommand:
        askGuess()
    elif options[menu_entry_index] == restart:
        attempts = 10
        startGame()


def preStart():
    # help menu for before the game is started
    print(figlet_format("Menu", font='smkeyboard'))
    options = [start, quit, difficultyString]
    terminal_menu = TerminalMenu(options)
    menu_entry_index = terminal_menu.show()
    if options[menu_entry_index] == start:
        print(start)
        startGame()
    elif options[menu_entry_index] == quit:
        print("Goodbye!")
        time.sleep(1)
        exit()
    elif options[menu_entry_index] == difficultyString:
        setDifficulty()
