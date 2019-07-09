import random
import turtle
import sys
import time


def welcome_message():
    player_name = input("Type your name: ")
    hangman_type = 'Ice-cream flavors'
    print(f"Hello {player_name}. You are going to play the {hangman_type} hangman game")

    print("""These are the rules of the game: 

        You play against the computer
        There's no limit of time, but there's a limit on attempts: 6
        The computer will print all the letters that have been told and are wrong

        GOOD LUCK! (:

    """)


def initialize():
    num_attempts = 5  # number of attempts
    missed_letters = []  # list of the missed letters
    guessed_letters = []  # list of guessed letters
    discovered_word = False  # the word has been discovered
    hidden_word = random_word()
    hidden_word_char = '_' * len(hidden_word)
    counter = 0  # counter to draw the hangman

    return hidden_word, num_attempts, missed_letters, guessed_letters, discovered_word, hidden_word_char, counter


def random_word():
    list_of_words = ['cookies', 'stracciatella', 'strawberry', 'chocolate', 'vanilla', 'milk', 'lemon', 'nutella',
                     'cheesecake', 'coffee', 'coconut', 'banana', 'pistachio', 'almond', 'caramel', 'tiramisu', 'brownie',
                     'blueberry', 'creme', 'peppermint', 'hazelnut', 'horchata', 'oreo']

    return random.choice(list_of_words)


def index_character(hidden_word, user_letter):
    letter_index = [index for index, letter in enumerate(hidden_word) if letter == user_letter]
    return letter_index


def print_word_status(hidden_word_char):
    print(*hidden_word_char.upper(), sep=" ")
    print("")


def initial_hint(hidden_word_char):
    print("HINT: You should discover the hidden ice-cream flavor")
    print_word_status(hidden_word_char)


def new_attempt(num_attempts):
    print(f"Remaining attemps: {num_attempts}")
    user_choice = input("Write the letter you want to guess: ")
    return user_choice.lower()

def valid_letter(letter,guessed_letters, missed_letters):
    validation = True
    if not letter.isalpha(): # not alphabetic value
        print('Please, enter only a LETTER')
        validation = False
    elif len(letter) != 1: #more than one character
        print('Please, enter only a SINGLE letter')
        validation = False
    elif letter in guessed_letters or letter in missed_letters: #letter has already been said
        print('You have already said this letter')
        validation = False
    return validation


def replace_char(hidden_word_char, letter_index, user_letter):
    for i in letter_index:
        hidden_word_char = hidden_word_char[0:i]+ user_letter + hidden_word_char[i+1:]
    return hidden_word_char


def print_letters( letter_list):
    print(f"Wrong letters:  {' '.join(letter_list)}")


def draw_Hangman(counter):
    def draw_Noose():
        turtle.speed(10)
        turtle.color("Black")
        turtle.forward(120)
        turtle.forward(-60)
        turtle.left(90)
        turtle.forward(150)
        turtle.right(90)
        turtle.forward(100)
        turtle.right(90)
        turtle.forward(30)
        turtle.right(90)

    def draw_Head():
        turtle.circle(15)
        turtle.circle(15, 180)  # draw a semicircle
        turtle.right(90)

    def draw_Arms():
        turtle.forward(5)
        turtle.left(90)
        turtle.forward(20)
        turtle.forward(-40)
        turtle.forward(20)
        turtle.right(90)

    def draw_Torso():
        turtle.forward(30)

    def draw_Legs():
        turtle.left(45)
        turtle.forward(30)
        turtle.forward(-30)
        turtle.right(90)
        turtle.forward(30)
        turtle.forward(-30)
        turtle.left(45)

    if counter == 1:
        draw_Noose()
    elif counter == 2:
        draw_Head()
    elif counter == 3:
        draw_Arms()
    elif counter == 4:
        draw_Torso()
    elif counter == 5:
        draw_Legs()


def winner_loser(discovered_word, num_attempts):
    if discovered_word == True:
        print("Congratulations! You've won!")
        time.sleep(4.0)
    elif num_attempts == 0 :
        print("I'm sorry, you're DEAD X(")
        time.sleep(4.0)