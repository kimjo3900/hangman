import random

# function to draw the hangman board after each guess
def draw_board():
    print("   ___")
    print("  |   |")
    if guesses_left > 5:
        print("      |")
    elif guesses_left == 5:
        print("  O   |")
    elif guesses_left == 4:
        print(" \O   |")
    else:
        print(" \O/  |")
    if guesses_left > 2:
        print("      |")
    else:
        print("  |   |")
    if guesses_left > 1:
        print("      |")
    elif guesses_left == 1:
        print(" /    |")
    else:
        print(" / \  |")
    print("      |")
    print("  ____|____")
    print("")

# list of all the available words the game can choose from
words = ["python", "programming", "fun"]

# choose a random word from the list
i = random.randint(0, len(words) - 1)
secret_word = words[i]

# keep track of the user's guesses
guesses = ''

guesses_left = 6

while guesses_left > 0:
    draw_board()

    hidden_letters = 0

    for char in secret_word:
        if char in guesses:
            print(char + " ", end='')
        else:
            print("_ ", end='')
            hidden_letters += 1

    print("")

    if hidden_letters == 0:
        print("Congratulations! You guessed the secret word!!")
        break

    while True:
        # prompt the user for a guess
        guess = input("Guess a letter: ")

        # Re-prompt the user if no input
        if len(guess) == 0:
            print("Please enter a character")
            continue
        # Or if input was already guessed
        elif guess in guesses:
            print("You've already guessed that letter")
            continue
        # Or if input contains more than one character
        elif len(guess) > 1:
            print("Enter only one character at a time")
        # Exit out of loop in all other cases
        else:
            guesses += guess
            break

    if guess not in secret_word:
        guesses_left -= 1

        if guesses_left == 0:
            draw_board()
            print("You lose! Better luck next time!!")

    print("")