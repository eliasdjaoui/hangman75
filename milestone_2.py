import random

fruit_list = ['Apple', 'Pear', 'Banana', 'Peach', 'Kiwi']
# print(fruit_list)
random_fruit = random.choice(fruit_list)

def guess_checker():
    guess = input("Guess a random letter: ")
    if len(guess) == 1 and guess.isalpha() == True:
        print("Good guess!")
    else:
        print("Oops! That is not a valid input.")
    
    