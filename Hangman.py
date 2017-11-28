'''
Scott B.
Hangman
'''

import random

def show_start_screen():
    print(" /$$   /$$                                                                ")
    print("| $$  | $$                                                                ")
    print("| $$  | $$  /$$$$$$  /$$$$$$$   /$$$$$$  /$$$$$$/$$$$   /$$$$$$  /$$$$$$$ ")
    print("| $$$$$$$$ |____  $$| $$__  $$ /$$__  $$| $$_  $$_  $$ |____  $$| $$__  $$")
    print("| $$__  $$  /$$$$$$$| $$  \ $$| $$  \ $$| $$ \ $$ \ $$  /$$$$$$$| $$  \ $$")
    print("| $$__  $$  /$$$$$$$| $$  \ $$| $$  \ $$| $$ | $$ | $$ /$$$$$$$ | $$   \$$")
    print("|__/  |__/ \_______/|__/  |__/ \____  $$|__/ |__/ |__/ \_______/|__/   |__/")
    print("                               /$$  \ $$                                  ")
    print("                              |  $$$$$$/                        ")
    print("                               \______/                         ")
    print()
    print("You have 7 strikes and then you're out")
    

def get_puzzle():
    rand_puzzle = ["Dab", "Whip", "NaeNae", "BilboBaggins", "Frodo", "Tom Cruise", "MrCooper", "Coding", "Alligator", "LilPump", "Holygrail", "DipLow"]
    puzzlechoice = random.randint(0, 11)
    return rand_puzzle[puzzlechoice]

def get_solved(puzzle, guesses):
    solved = ""

    for letter in puzzle:
        if letter in guesses:
            solved += letter
        else:
            solved += "-"

    return solved


def get_strikes(puzzle, guesses,  strikes):
    if guesses[-1] in puzzle:
        return strikes
    strikes += 1
    return strikes

def get_guess(strikes, name, guesses):
        print()
        print("You have " +   str(strikes)   + " strikes")
        print()
        letter = input("Guess a letter " + name + ": ")
        print()
        print("You have guessed " + guesses + ".")
        
        if len(letter) > 1:
            print("Type one letter goofball!!!")
            letter = get_guess(strikes)
            return letter
        else:
            return letter

        
def display_board(solved):
    print()
    print(solved)


def show_credits():
    print("  ___    __    __  __  ____    _____  _  _  ____  ____ ")
    print(" / __)  /__\  (  \/  )( ___)  (  _  )( \/ )( ___)(  _ \ ")
    print("( (_-. /(__)\  )    (  )__)    )(_)(  \  /  )__)  )   /")
    print(" \___/(__)(__)(_/\/\_)(____)  (_____)  \/  (____)(_)\_)")
    print("")
    print("")
    print("This game was created by yours truly Scott on Nov.27/2017.") 


def get_name():
    print()
    name = input("What is your name?")
    return name
          



def show_result(strikes, limit, solved, puzzle, name):

    if strikes == limit and solved != puzzle:
        print()
        print("Game Over, you are out of guesses")
    else:
        print()
        print("Congrats you did it " + name + "!")


def play_again():
    while True:
        print()
        decision = input("Would you like to play again? (y/n) ")

        if decision == 'y' or decision == 'yes':
            return True
        elif decision == 'n' or decision == 'no':
            return False
        else:
            print()
            print("I don't understand. Please enter 'y' or 'n'.")
  
def play():
    name = get_name()
    strikes = 0
    limit = 7
    puzzle = get_puzzle()
    guesses = ""
    solved = get_solved(puzzle, guesses)
    display_board(solved)

    while solved != puzzle and strikes != limit:
        if strikes != limit:
            guesses += get_guess(strikes, name, guesses)
            solved = get_solved(puzzle, guesses)
            strikes = get_strikes(puzzle, guesses, strikes)
            display_board(solved)
        else:
            print("You are out of guesses!")
            print()
    show_result(strikes, limit, solved, puzzle, name)

    
show_start_screen()


playing = True

while playing:
    play()
    playing = play_again()

show_credits()
