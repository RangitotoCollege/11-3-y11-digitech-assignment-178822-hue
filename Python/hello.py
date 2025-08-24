# GUESS THE NUMBER

import random
import time

win = False
lowest_allowed = 1
highest_allowed = 100
number = random.randint(lowest_allowed, highest_allowed)
guesses = 0
guesses_allowed = 5
print(
    """ 
      WELCOME TO GUESS THE NUMBER!!!

      You have to guess the random number between 1 and 100!
      
      You only have 5 attempts, but you will be told whether your guess is higher or lower than the target number
      
      Best of luck, player!   

      """
)  # welcome message for the player

time.sleep(4)  # pausing between the message display and the beggining of the game.
while guesses < guesses_allowed:
    try:
        guess = int(input("Enter your guess: "))
        if guess == number:
            print(f"You guessed correctly! The number was {number}!")
            guesses += 1
            win = True  # enabling the winning message at the end
            break
        elif (
            guess < number and guess >= lowest_allowed
        ):  # making sure number is within boundaries
            print("Too low. Try again.")
            guesses += 1
        elif guess > number and guess <= highest_allowed:
            print("Too high. Try again.")
            guesses += 1
        else:
            print("Not in range. It should be from 1 to 100")
    except ValueError:  # catching value errors
        print("Invalid input.")
if win:
    print(f"Awesome job! You guessed it in {guesses} guesses.")  # win
else:
    print(
        f"You lost because you exceeded the {guesses_allowed} guesses allowed, the number was {number}. Better luck next time!"
    )  # loss
time.sleep(4)
# ANAGRAMMA

words = [
    "television",
    "parachute",
    "champagne",
    "complete",
    "landscape",
    "fisherman",
    "substitute",
    "experience",
    "employee",
    "psychology",
]

print(
    """ 
      WELCOME TO ANAGRAMMA!!!

      You will receive a word, but all jumbled up!
      
      You have to guess what the unscrambled word actually is, and you have 2 attempts per word. 
      
      Best of luck, player!   

      """
)  # welcome message for the player
right_guess = False
attempts_allowed = 2
attempts_used = 0


def scramble_word(unshuffled_word):
    chars = list(unshuffled_word)
    random.shuffle(chars)
    return "".join(chars)


unscrambled_word = random.choice(words)
word = scramble_word(unscrambled_word)
unscramble_attempt = ""
attempt = 1
time.sleep(4)
print(f"The scrambled word is {word}.")
time.sleep(2)
while unscramble_attempt != unscrambled_word and attempts_used < attempts_allowed:
    try:
        unscramble_attempt = input("Take a guess at the unscrambled word: ")
        if unscramble_attempt == unscrambled_word:
            attempts_used += attempt
            right_guess = True
            print(f"Congrats, that is correct! The word was {unscrambled_word}")
        else:
            attempts_used += attempt
    except ValueError:
        print("Invalid input.")
if right_guess:
    print("You win, player. Well done!")
else:
    print("Unlucky player, give it another go!")
