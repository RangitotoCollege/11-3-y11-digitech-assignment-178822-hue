import random, time, os


def play_guess_the_number():
    print(
        """ 
        WELCOME TO GUESS THE NUMBER!!!

        You have to guess the random number between 1 and 100!
        
        You only have 5 attempts, but you will be told whether your guess is higher or lower than the target number.
        
        Best of luck, player!   
        """
    )
    while True:
        win = False
        guess_value = 1
        lowest_allowed = 1
        highest_allowed = 100
        number = random.randint(lowest_allowed, highest_allowed)
        guesses = 0
        guesses_allowed = 5
        time.sleep(2)
        while guesses < guesses_allowed:
            try:
                guess = int(input("Enter your guess: "))
                if guess == number:
                    print(f"You guessed correctly! The number was {number}!")
                    guesses += guess_value
                    win = True
                    break
                elif guess < number and guess >= lowest_allowed:
                    print("Too low. Try again.")
                    guesses += guess_value
                elif guess > number and guess <= highest_allowed:
                    print("Too high. Try again.")
                    guesses += guess_value
                else:
                    print("Not in range. It should be from 1 to 100")
            except ValueError:
                print("Invalid input.")
        if win:
            print(f"Awesome job! You guessed it in {guesses} guesses.")
        else:
            print(
                f"You lost because you exceeded the {guesses_allowed} guesses allowed, the number was {number}. Better luck next time!"
            )
        again = input("Play again? (y/n): ").lower()
        if again != "y":
            break


def play_anagramma():
    def get_random_word():
        script_dir = os.path.dirname(__file__)
        file_path = os.path.join(script_dir, "words.txt")
        with open(file_path) as f:
            words_in_file = f.read().splitlines()
        return random.choice(words_in_file)

    def scramble_word(unshuffled_word):
        chars = list(unshuffled_word)
        random.shuffle(chars)
        return "".join(chars)

    print(
        """ 
        WELCOME TO ANAGRAMMA!!!

        You will receive a word, but all jumbled up!
        
        You have to guess what the unscrambled word actually is, and you have 2 attempts per word. 
        
        Best of luck, player!   
        """
    )

    while True:
        right_guess = False
        attempts_allowed = 2
        attempts_used = 0

        unscrambled_word = get_random_word()
        scrambled = scramble_word(unscrambled_word)

        print(f"The scrambled word is {scrambled}.")
        while attempts_used < attempts_allowed and not right_guess:
            guess = input("Take a guess at the unscrambled word: ")
            attempts_used += 1
            if guess == unscrambled_word:
                right_guess = True
                print(f"Congrats, that is correct! The word was {unscrambled_word}")
            else:
                print("Nope, try again!")

        if right_guess:
            print("You win, player. Well done!")
        else:
            print(f"Unlucky! The word was {unscrambled_word}.")

        again = input("Play again? (y/n): ").lower()
        if again != "y":
            break


def play_psr():
    print(
        """ 
            WELCOME TO PAPER SCISSORS ROCK!!!

            Both you and the computer will pick between paper, scissors, and rock!
            
            Paper beats rock, rock beats scissors, and scissors beat paper, and you want to get as many consecutive wins as you can.
            
            Best of luck, player!   

        """
    )

    while True:
        consecutive_wins = 0
        options = ["paper", "scissors", "rock"]
        finished = False

        while not finished:
            user_choice = input("Choose paper, scissors, or rock: ").lower()
            while user_choice not in options:
                print("Choose a valid option.")
                user_choice = input("Choose paper, scissors, or rock: ").lower()

            comp_choice = random.choice(options)

            if user_choice == comp_choice:
                print(f"Both chose {user_choice}. It's a tie.")
            elif (
                (user_choice == "paper" and comp_choice == "rock")
                or (user_choice == "rock" and comp_choice == "scissors")
                or (user_choice == "scissors" and comp_choice == "paper")
            ):
                print(f"You won! {user_choice} beats {comp_choice}.")
                consecutive_wins += 1
            else:
                print(f"You lost. {comp_choice} beats {user_choice}.")
                finished = True

        print(f"Game over. You had {consecutive_wins} consecutive wins!")
        again = input("Play again? (y/n): ").lower()
        if again != "y":
            break


def play_blackjack():
    print(
        """
        WELCOME TO BLACKJACK!!!

        Try to get as close to 21 as you can without going over. 
        
        Face cards are worth 10, Aces are 11, and numbers keep their value. 
        
        You’ll start with two cards and can choose to hit (take another card) 
        or stand (stick with what you have). The dealer will play after you. 
        
        Best of luck, player!
        """
    )

    def card_value(card):
        if card[0] in ["Jack", "Queen", "King"]:
            return 10
        elif card[0] == "Ace":
            return 11
        else:
            return int(card[0])

    while True:
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
        random.shuffle(deck)

        player_card = [deck.pop(), deck.pop()]
        dealer_card = [deck.pop(), deck.pop()]

        def score(hand):
            return sum(card_value(c) for c in hand)

        while True:
            player_score = score(player_card)
            dealer_score = score(dealer_card)
            print(
                f"Your cards: {', '.join([f'{r} of {s}' for r,s in player_card])} (score {player_score})"
            )

            choice = input("Hit or stand? (h/s): ").lower()
            if choice == "h":
                new_card = deck.pop()
                player_card.append(new_card)
                if score(player_card) > 21:
                    print("BUST! Dealer wins.")
                    break
            elif choice == "s":
                while dealer_score < 17:
                    dealer_card.append(deck.pop())
                    dealer_score = score(dealer_card)
                print(
                    f"Dealer's cards: {', '.join([f'{r} of {s}' for r,s in dealer_card])} (score {dealer_score})"
                )
                if dealer_score > 21 or player_score > dealer_score:
                    print("Player wins!")
                elif dealer_score > player_score:
                    print("Dealer wins!")
                else:
                    print("It's a tie.")
                break
        again = input("Play again? (y/n): ").lower()
        if again != "y":
            break


def show_menu():
    print(
        """   
        Choose a game:
        gtn - Guess the Number
        a   - Anagramma
        psr - Paper Scissors Rock
        bj  - Blackjack
        quit - Exit PlayTopia
        """
    )
    return input("Your choice: ").lower()


games = {
    "gtn": play_guess_the_number,
    "a": play_anagramma,
    "psr": play_psr,
    "bj": play_blackjack,
}
print(
    """ 
        WELCOME TO PLAYTOPIA!
        
        We have a range of games to offer for you!
        
        Give some a go and don't forget to have fun!    
    """
)
while True:
    choice = show_menu()
    if choice in games:
        pick = games[choice]
        pick()
    elif choice == "quit":
        print("Thanks for playing PlayTopia!")
        break
    else:
        print("Invalid choice. Try again.")
