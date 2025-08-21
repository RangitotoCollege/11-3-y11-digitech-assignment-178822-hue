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
