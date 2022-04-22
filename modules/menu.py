import time

# for cool banner and used for the menu
from pyfiglet import figlet_format
# for the cool menu
from simple_term_menu import TerminalMenu
# import modules/objects
import mastermind as mm


def commands():
    # help menu for when game is already started
    print(figlet_format("Menu", font='smkeyboard'))
    options = [mm.quit, mm.history, mm.restart, mm.continueCommand]
    terminal_menu = TerminalMenu(options)
    menu_entry_index = terminal_menu.show()
    if options[menu_entry_index] == mm.quit:
        print("Goodbye!")
        time.sleep(1)
        exit()
    elif options[menu_entry_index] == mm.history:
        if len(mm.guessHist) == 0:
            print("\nno history yet!")
            time.sleep(1)
            commands()
        else:
            print("\n" + str(mm.guessHist) + "\n")
            time.sleep(1)
            commands()
    elif options[menu_entry_index] == mm.continueCommand:
        mm.askGuess()
    elif options[menu_entry_index] == mm.restart:
        mm.attempts = 10
        mm.startGame()


def preStart():
    # help menu for before the game is started
    print(figlet_format("Menu", font='smkeyboard'))
    options = [mm.start, mm.quit, mm.difficultyString]
    terminal_menu = TerminalMenu(options)
    menu_entry_index = terminal_menu.show()
    if options[menu_entry_index] == mm.start:
        print(mm.start)
        mm.startGame()
    elif options[menu_entry_index] == mm.quit:
        print("Goodbye!")
        time.sleep(1)
        exit()
    elif options[menu_entry_index] == mm.difficultyString:
        mm.setDifficulty()


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
        mm.secondary()
    elif options[menu_entry_index] == "medium":
        difficulty = "medium"
        print("\nDifficulty set to medium.")
        time.sleep(1)
        mm.secondary()
    elif options[menu_entry_index] == "hard":
        difficulty = "hard"
        print("\nDifficulty set to hard.")
        time.sleep(1)
        mm.secondary()
