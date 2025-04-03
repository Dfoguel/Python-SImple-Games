import random
from words import words
import string

def get_valid_word(list_of_words):
    word_choice = random.choice(list_of_words)
    while '-' in word_choice or ' ' in word_choice: #Remove words with hyphens(-) or spaces( )
        word = random.choice(list_of_words)
    return word_choice.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    lives = 6

    while len(word_letters) > 0 and lives > 0:
        #show the letters used
        print("You have", lives, "lives left and you have used this letters: ", ' '.join(used_letters))

        #show the current word
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print("Current word: ", " ".join(word_list))

        #Get the letter from user
        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters: #Condition that dont' let the user try letters already used
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives = lives - 1
                print("Letter is not in the word")
        
        elif user_letter in used_letters:
            print("You've already tried this one...")

        else:
            print("Invalid character! Try another one")

    if lives == 0:
        print("Sorry you lost, the word was", word)
    else:
        print("You guessed the word", word, "correctly!!")


hangman()