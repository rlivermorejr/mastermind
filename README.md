# THE MASTERMIND GAME

## Instructions
- This program is written in python, it is made to run in the terminal, you'll need a python interpretor or run a venv (virtual environment).
- Once you have a venv running you can continue to the next step.
- You will need to install the modules listed in requirements.txt or pyproject.toml
- Once all modules are installed, you can run the program by typing "python code.py" into the terminal.

## Thought process
- I started out by making sure I could get the api call to work and that it would be in the easiest format to work with.
- I then set up the basic structure of the game. IE: main function, variables needed, inputs, etc.
- I then began to work on the logic of the game. I figured I could pass the input into a function and then determined which characters matched.
- I ran into my first issue with the way I was actually thinking about how to match the numbers up. I was over thinking it a little bit and was storing the users input into a list.
- I then realized I didn't need to store the users input into a list. I could just use a for loop to check each character in the input.
- From then I added a counter to keep track of the numbers that matched the index and ones that didn't.
- After I was able to get the counter working I was able to get the correct outputs to display.
- After I was able to actually play the game, I then began on the menus and look of the game.
- I added a basic input menu with commands and then I changed that to a menu where you select the options with arrow keys on your keyboard. This was done by adding simple-term-menu to the modules and the implementation was pretty easy from there.
- I then added a nice banner for the start up of the game with pyfiglet and the cool typing effect to the main menu.
- After I was happy with the look of the game, I started to try and 'break' different parts of the game where I suspected vulnerabilities might be in my code.
- Once fixing the minor bugs, mainly to the output and counting matches, I was happy with what I had, but I wanted to add sounds.
- I tried to get sounds working, but most of the modules did not work, I think because I am using a virtual environment, or they required a seperate download of something and I didn't want that.
- I decided I would add a dificulty setting and menu to the game which I found to be quite enjoyable.