# This imports the random module to facilitate random selection from a list.
import random
# Variables
guess = []
# This defines a list of words that can be used in the game.
word_bank = ['ruby', 'sapphire', 'platinum', 'heartgold', 'soulsilver', 'emerald', 'diamond']

# This randomly selects a word from the word bank for the player to guess.
chosen_word = random.choice(word_bank)

guess = ['_'] * len(chosen_word)

attempts = 10

print("What is the word?")


# Main game loop
while attempts > 0 and '_' in guess:
    print(f"Guess word: {' '.join(guess)}")
    
    user_guess = input('Enter a letter: ').lower()
    
    if len(user_guess) == 1:  # Ensure single character input
        if user_guess in chosen_word:
            for i in range(len(chosen_word)):
                if chosen_word[i] == user_guess:
                    guess[i] = user_guess
            print('Nice guess!')
        else:
            attempts -= 1
            print(f"Wrong guess. You have {attempts} attempts left.")
    else:
        print("Please enter a single letter")
        
    if '_' not in guess:
        print(f"Congratulations! You've guessed the word: {chosen_word}")
        break
else:
    if attempts == 0:
        print(f"Sorry, you've run out of attempts. The word was: {chosen_word}")