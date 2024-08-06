#%%

import random

words = ["apple", "banana", "cherry", "date", "fig", "grape", "kiwi"]

secret_word = random.choice(words)

def check_guess(guess):
    """
    Checks if the guessed letter is in the secret word.

    Parameters:
    guess (str): The guessed letter

    Returns:
    None
    """

    guess = guess.lower()

    if guess in secret_word:
        print(f"Good guess! '{guess}' is in the word.")
    else:
        print(f"Sorry, '{guess}' is not in the word. Try again.")


def ask_for_input():
    """
    Prompts the user to guess a letter and validates the input.

    Returns:
    None
    """
    while True:
        guess = input("Guess a letter: ").strip().lower()

        if guess.isalpha() and len(guess) == 1:
            print("Valid letter!")

       
            check_guess(guess)
            break  
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")
ask_for_input()



# %%
