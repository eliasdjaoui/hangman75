#%%
import random
words = ["apple", "banana", "cherry", "date", "fig", "grape", "kiwi"]
secret_word = random.choice(words)

correct_guesses = set()
incorrect_guesses = set()
max_attempts = 5

def display_progress():
    displayed_word = ''.join([letter if letter in correct_guesses else '_' for letter in secret_word])
    print(f"Current word: {displayed_word}")
    
def check_guess(guess):
    guess = guess.lower()

    if guess in secret_word:
        correct_guesses.add(guess)
        print(f"Good guess! '{guess}' is in the word.")
        display_progress()  
    else:
        incorrect_guesses.add(guess)
        print(f"Sorry, '{guess}' is not in the word. Try again.")


def ask_for_input():
    while len(incorrect_guesses) < max_attempts:
        guess = input("Guess a letter: ").strip().lower()
        if guess.isalpha() and len(guess) == 1:
            print("Valid letter!")
            check_guess(guess)

            if set(secret_word) == correct_guesses:
                print(f"Congratulations! You've guessed the word '{secret_word}'!")
                break

            remaining_attempts = max_attempts - len(incorrect_guesses)
            print(f"You have {remaining_attempts} attempts left.")
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")

    if len(incorrect_guesses) == max_attempts:
        print(f"You've run out of attempts! The secret word was '{secret_word}'.")

ask_for_input()
# %%
