import random

class HangMan:
    def __init__(self, word_list=None, max_attempts=5):
        """
        Initializes a new instance of the HangMan game.

        Parameters:
        word_list (list): A list of words to choose from. If None, a default list is used.
        max_attempts (int): The maximum number of incorrect guesses allowed. Default is 5.

        Returns:
        None
        """
        if word_list is None:
            word_list = ["apple", "banana", "cherry", "date", "fig", "grape", "kiwi"]
        
        self.word_list = word_list
        self.secret_word = random.choice(self.word_list)
        self.correct_guesses = set()
        self.incorrect_guesses = set()
        self.max_attempts = max_attempts

    def display_progress(self):
        """
        Displays the current state of the secret word,
        showing correctly guessed letters and underscores for remaining letters.
        """
        displayed_word = ''.join(
            [letter if letter in self.correct_guesses else '_' for letter in self.secret_word]
        )
        print(f"Current word: {displayed_word}")

    def check_guess(self, guess):
        """
        Checks if the guessed letter is in the secret word.

        Parameters:
        guess (str): The guessed letter.

        Returns:
        None
        """
        guess = guess.lower()

        if guess in self.secret_word:
            self.correct_guesses.add(guess)
            print(f"Good guess! '{guess}' is in the word.")
            self.display_progress()
        else:
            self.incorrect_guesses.add(guess)
            print(f"Sorry, '{guess}' is not in the word. Try again.")

    def is_valid_guess(self, guess):
        """
        Checks if the guessed input is a valid single alphabetical character.

        Parameters:
        guess (str): The guessed letter input by the user.

        Returns:
        bool: True if the guess is valid, False otherwise.
        """
        return guess.isalpha() and len(guess) == 1

    def ask_for_input(self):
        """
        Prompts the user to guess a letter and validates the input.

        Returns:
        None
        """
        while len(self.incorrect_guesses) < self.max_attempts:
            guess = input("Guess a letter: ").strip().lower()

            if self.is_valid_guess(guess):
                print("Valid letter!")
                self.check_guess(guess)

                if set(self.secret_word) == self.correct_guesses:
                    print(f"Congratulations! You've guessed the word '{self.secret_word}'!")
                    return

                remaining_attempts = self.max_attempts - len(self.incorrect_guesses)
                print(f"You have {remaining_attempts} attempts left.")
            else:
                print("Invalid letter. Please, enter a single alphabetical character.")

        print(f"You've run out of attempts! The secret word was '{self.secret_word}'.")

# Run the game
if __name__ == "__main__":
    play_game = HangMan()
    play_game.ask_for_input()
