code_for_anagramma = "a"
code_for_GTN = "gtn"
code_for_PSR = "psr"
code_for_blackjack = "bj"
game = input(
    "What game do you want to play? (Guess the number: gtn, Anagramma: a, Paper Scissors Rock: psr, Blackjack (21): bj)"
).lower()
# GUESS THE NUMBER

import random
import time

if game == code_for_GTN:
    win = False
    guess_value = 1
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
                guesses += guess_value
                win = True  # enabling the winning message at the end
                break
            elif (
                guess < number and guess >= lowest_allowed
            ):  # making sure number is within boundaries
                print("Too low. Try again.")
                guesses += guess_value
            elif guess > number and guess <= highest_allowed:
                print("Too high. Try again.")
                guesses += guess_value
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
if game == code_for_anagramma:
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

# PAPER SCISSORS ROCK

if game == code_for_PSR:
    consecutive_wins = 0
    win_point = 1
    finished = False
    options = ["paper", "scissors", "rock"]

    while not finished:
        user_choice = input("Choose paper, scissors, or rock: ").lower()
        while user_choice not in options:
            print("Choose a valid option.")
            user_choice = input("Choose paper, scissors, or rock: ").lower()
            time.sleep(1)

        comp_choice = random.choice(options)

        if user_choice == comp_choice:
            print(f"Oooh, you both chose {user_choice}. It is a tie.")
        elif user_choice == "paper":
            if comp_choice == "scissors":
                finished = True
                print(
                    f"You lose. You chose {user_choice} and the computer chose {comp_choice}."
                )
            else:
                print(
                    f"You won. You chose {user_choice} and the computer chose {comp_choice}."
                )
                consecutive_wins += win_point
        elif user_choice == "rock":
            if comp_choice == "paper":
                finished = True
                print(
                    f"You lose. You chose {user_choice} and the computer chose {comp_choice}."
                )
            else:
                print(
                    f"You won. You chose {user_choice} and the computer chose {comp_choice}."
                )
                consecutive_wins += win_point
        elif user_choice == "scissors":
            if comp_choice == "rock":
                finished = True
                print(
                    f"You lose. You chose {user_choice} and the computer chose {comp_choice}."
                )
            else:
                print(
                    f"You won. You chose {user_choice} and the computer chose {comp_choice}."
                )
                consecutive_wins += win_point

# BLACKJACK
if game == code_for_blackjack:
    game_over = False

    card_categories = ["Hearts", "Diamonds", "Clubs", "Spades"]
    cards_list = [
        "Ace",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "10",
        "Jack",
        "Queen",
        "King",
    ]
    deck = [(card, category) for category in card_categories for card in cards_list]

    def card_value(card):
        if card[0] in ["Jack", "Queen", "King"]:
            return 10
        elif card[0] == "Ace":
            return 11
        else:
            return int(card[0])

    random.shuffle(deck)
    player_card = [deck.pop(), deck.pop()]
    dealer_card = [deck.pop(), deck.pop()]

    while True:
        player_score = sum(card_value(card) for card in player_card)
        dealer_score = sum(card_value(card) for card in dealer_card)

        print(
            f"Cards Player Has: {', '.join([f'{rank} of {suit}' for rank, suit in player_card])}"
        )
        time.sleep(2)
        print(f"Score of the Player: {player_score}")
        time.sleep(3)
        print("\n")

        choice = input("Do you want to hit or stand? h/s: ").lower()
        if choice not in ["h", "s"]:  # error control
            print("Please enter one of the valid options.")
            continue

        if choice == "h":
            new_card = deck.pop()
            print(f"Your new card: {new_card[0]} of {new_card[1]}")
            time.sleep(1)
            player_card.append(new_card)
            player_score = sum(card_value(card) for card in player_card)
        elif choice == "s":
            break

        if player_score == 21:
            print("Nice! You're on 21.")
            print(
                f"Your cards: {', '.join([f'{rank} of {suit}' for rank, suit in player_card])}"
            )
            game_over = True
            break

        if player_score > 21:
            print(
                f"Cards Dealer Has: {', '.join([f'{rank} of {suit}' for rank, suit in dealer_card])}"
            )
            print(f"Score of the Dealer: {dealer_score}")
            print(
                f"Cards Player Has: {', '.join([f'{rank} of {suit}' for rank, suit in player_card])}"
            )
            print(f"Score of the Player: {player_score}")
            print("BUST! Dealer wins")
            game_over = True
            break

    time.sleep(2)
    if game_over == False:
        while dealer_score < 17:
            new_card = deck.pop()
            dealer_card.append(new_card)
            dealer_score += card_value(new_card)

        print(
            f"Cards Dealer Has: {', '.join([f'{rank} of {suit}' for rank, suit in dealer_card])}"
        )
        print(f"Score of the Dealer: {dealer_score}")
        print("\n")

        if dealer_score > 21:
            print(
                f"Cards Dealer Has: {', '.join([f'{rank} of {suit}' for rank, suit in dealer_card])}"
            )
            print(f"Score of the Dealer: {dealer_score}")
            print(
                f"Cards Player Has: {', '.join([f'{rank} of {suit}' for rank, suit in player_card])}"
            )
            print(f"Score of the Player: {player_score}")
            print("Player wins (Dealer score is exceeding 21)")
        elif player_score > dealer_score:
            print(
                f"Cards Dealer Has: {', '.join([f'{rank} of {suit}' for rank, suit in dealer_card])}"
            )
            print(f"Score of the Dealer: {dealer_score}")
            print(
                f"Cards Player Has: {', '.join([f'{rank} of {suit}' for rank, suit in player_card])}"
            )
            print(f"Score of the Player: {player_score}")
            print("Player wins (Player has higher score than Dealer)")
        elif dealer_score > player_score:
            print(
                f"Cards Dealer Has: {', '.join([f'{rank} of {suit}' for rank, suit in dealer_card])}"
            )
            print(f"Score of the Dealer: {dealer_score}")
            print(
                f"Cards Player Has: {', '.join([f'{rank} of {suit}' for rank, suit in player_card])}"
            )
            print(f"Score of the Player: {player_score}")
            print("Dealer wins (Dealer has higher score than Player)")
        else:
            print(
                f"Cards Dealer Has: {', '.join([f'{rank} of {suit}' for rank, suit in dealer_card])}"
            )
            print(f"Score of the Dealer: {dealer_score}")
            print(
                f"Cards Player Has: {', '.join([f'{rank} of {suit}' for rank, suit in player_card])}"
            )
            print(f"Score of the Player: {player_score}")
            print("It's a tie.")
