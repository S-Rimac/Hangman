# Initialize variables
guesses = []
max_attempts = 6

# Get a word from the player to guess
word = input("Enter a word: ").lower()

# Loop until the player guesses the word or runs out of attempts
while max_attempts > 0:
    # Display the word with underscores for missing letters
    display_word = ""
    for letter in word:
        if letter in guesses:
            display_word += letter
        else:
            display_word += "_"
    print(display_word)
    
    # Get a guess from the player
    guess = input("Guess a letter: ").lower()
    
    # Check if the guess is correct
    if guess in word:
        print("Correct!")
        guesses.append(guess)
    else:
        print("Wrong!")
        max_attempts -= 1
    
    # Check if the player has guessed the word
    if set(word) <= set(guesses):
        print("You win!")
        break
    
# If the player runs out of attempts, they lose
if max_attempts == 0:
    print("You lose! The word was", word)
