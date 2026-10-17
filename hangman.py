
import random

# List of 5 predefined words
words = ["python", "computer", "developer", "program", "hangman"]

# Select a random word
secret_word = random.choice(words)

# Store correctly guessed letters
guessed_letters = []

# Maximum incorrect guesses
max_attempts = 6
incorrect_guesses = 0

print("=" * 35)
print("       WELCOME TO HANGMAN!")
print("=" * 35)
print("Guess the hidden word one letter at a time.")
print("You have 6 incorrect guesses available.\n")

# Main game loop
while incorrect_guesses < max_attempts:

    # Display the current word
    displayed_word = ""

    for letter in secret_word:
        if letter in guessed_letters:
            displayed_word += letter + " "
        else:
            displayed_word += "_ "

    print("Word:", displayed_word)
    print("Incorrect guesses:", incorrect_guesses)
    print("Attempts remaining:", max_attempts - incorrect_guesses)

    # Check if the player has guessed the word
    if all(letter in guessed_letters for letter in secret_word):
        print("\nCongratulations! You guessed the word:", secret_word)
        print("You win!")
        break

    # Take input from the player
    guess = input("\nGuess a letter: ").lower().strip()

    # Validate the input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single alphabet letter.\n")
        continue

    # Check for repeated guesses
    if guess in guessed_letters:
        print("You have already guessed that letter. Try again.\n")
        continue

    # Store the guessed letter
    guessed_letters.append(guess)

    # Check whether the guess is correct
    if guess in secret_word:
        print("Correct guess!\n")
    else:
        incorrect_guesses += 1
        print("Wrong guess!\n")

else:
    print("\nGame over! You have used all 6 incorrect guesses.")
    print("The correct word was:", secret_word)

print("\nThanks for playing Hangman!")