import random
import os
import sys

VALID_CHOICES = ['rock', 'paper', 'scissors', 'lizard', 'spock']
DISPLAY_CHOICES = ['rock (or r)', 'paper (or p)', 'scissors (or sc)',
                'lizard (or l)', 'spock (or sp)']

def welcome():
    print('**** Welcome to Rock, Paper, Scissors, Lizard Spock**** \n'
           '*The rules are: \n'
           '    Scissors cut Paper \n'
           '    Paper covers Rock \n'
           '    Rock crushes Lizard \n'
           '    Lizard poisons Spock \n'
           '    Spock smashes Scissors \n'
           '    Scissors decapitate Lizard \n'
           '    Lizard eats Paper \n'
           '    Paper disproves Spock \n'
           '    Spock caporizes Rock \n'
           '    And as it always has, Rock crushes Scissors \n'
           '>>The match is best of 5.  First player to 3 wins the match!<<')

def clear():
    os.system('clear')
def prompt(message):
    print(f'++++ {message}')
def prompt_winner(message):
    print(f'=====> {message} <=====')

result = "You win!"
def display_winner(choice, computer_choice):
    prompt(f"You chose {choice}, computer chose {computer_choice}")
    global result
    match choice:
        case "rock":
            if computer_choice in ("scissors", "lizard"):
                result = "You win!"
            elif computer_choice in ("paper", "spock"):
                result = "Computer wins!"
            else:
                result = "It's a tie!"
        case "paper":
            if computer_choice in ("rock", "spock"):
                result = "You win!"
            elif computer_choice in ("scissors", "lizard"):
                result = "Computer wins!"
            else:
                result = "It's a tie!"
        case "scissors":
            if computer_choice in ("paper", "lizard"):
                result = "You win!"
            elif computer_choice in ("rock", "spock"):
                result = "Computer wins!"
            else:
                result = "It's a tie!"
        case "spock":
            if computer_choice in ("rock", "scissors"):
                result = "You win!"
            elif computer_choice in ("lizard", "paper"):
                result = "Computer wins!"
            else:
                result = "It's a tie!"
        case "lizard":
            if computer_choice in ("spock", "paper"):
                result = "You win!"
            elif computer_choice in ("rock", "scissors"):
                result = "Computer wins!"
            else:
                result = "It's a tie!"
    prompt(result)

def get_choice():
    prompt(f'Choose one: {", ".join(DISPLAY_CHOICES)}')
    global choice
    choice = input()
    if choice in ('r', 'rock'):
        choice = "rock"
    elif choice in ('p', 'paper'):
        choice = "paper"
    elif choice in ('sc', 'scissors'):
        choice = "scissors"
    elif choice in ('sp', 'spock'):
        choice = "spock"
    elif choice in ('l', 'lizard'):
        choice = "lizard"

    while choice not in VALID_CHOICES:
        prompt("That's not a valid choice")
        choice = input()
        if choice in ('r', 'rock'):
            choice = "rock"
        elif choice in ('p', 'paper'):
            choice = "paper"
        elif choice in ('sc', 'scissors'):
            choice = "scissors"
        elif choice in ('sp', 'spock'):
            choice = "spock"
        elif choice in ('l', 'lizard'):
            choice = "lizard"

def get_computer_choice():
    global computer_choice
    computer_choice = random.choice(VALID_CHOICES)

def play_again():
    prompt("Do you want to play again (y/n)?")
    answer = input().lower()

    match answer:
        case "y":
            clear()
        case "n":
            clear()
            sys.exit()
        case _:
            prompt('Invalid choice.  Choose "y" or "n"')
            play_again()

clear()

welcome()
while True:
    PLAYER_SCORE = 0
    COMPUTER_SCORE = 0
    while PLAYER_SCORE < 3 and COMPUTER_SCORE < 3:
        prompt(f'Score is Player: {PLAYER_SCORE} Computer: {COMPUTER_SCORE}')
        get_choice()

        get_computer_choice()

        display_winner(choice, computer_choice)
        if result == "You win!":
            PLAYER_SCORE += 1

        elif result == "Computer wins!":
            COMPUTER_SCORE += 1

        else:
            PLAYER_SCORE += 0
            COMPUTER_SCORE += 0

    if PLAYER_SCORE == 3:
        prompt(f'Score is Player: {PLAYER_SCORE} Computer: {COMPUTER_SCORE}')
        prompt_winner("PLAYER WINS THE MATCH!!!")
        prompt_winner("   CONGRATULATIONS!!!   ")
    elif COMPUTER_SCORE == 3:
        prompt(f'Score is Player: {PLAYER_SCORE} Computer: {COMPUTER_SCORE}')
        prompt_winner("COMPUTER WINS THE MATCH!!!")
        prompt_winner("    TOO BAD.  SO SAD.     ")

    play_again()

    clear()
    