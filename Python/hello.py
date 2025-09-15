import random, time, os

scores = {
    "gtn": 0,
    "a": 0,
    "psr": 0,
    "bj": 0,
}


# GUESS THE NUMBER
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
                    print(
                        f"Not in range. It should be from {lowest_allowed} to {highest_allowed}."
                    )
            except ValueError:
                print("Invalid input.")
        if win:
            print(f"Awesome job! You guessed it in {guesses} guesses.")
            if scores["gtn"] == 0 or guesses < scores["gtn"]:
                scores["gtn"] = guesses
                print(f"🎉 New best score: {guesses} guesses!")
            else:
                print(f"Your best so far is {scores["gtn"]} guesses.")
        else:
            print(
                f"You lost because you exceeded the {guesses_allowed} guesses allowed, the number was {number}. Better luck next time!"
            )
            print(f"Your best so far is {scores["gtn"]} guesses.")
        again = input("Play again? (y/n): ").lower()
        if again != "y":
            break


# ANAGRAMMA
def play_anagramma():
    def get_random_word():
        script_dir = os.path.dirname(
            __file__
        )  # getting folder where hello.py is located
        file_path = os.path.join(
            script_dir, "words.txt"
        )  # made path to words.txt so python can always find it
        with open(
            file_path
        ) as f:  # open words.txt and read all lines (each word) into a list
            words_in_file = f.read().splitlines()
        return random.choice(words_in_file)  # choose word

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
        attempt_value = 1
        unscrambled_word = get_random_word()
        scrambled = scramble_word(unscrambled_word)

        print(f"The scrambled word is {scrambled}.")
        while attempts_used < attempts_allowed and not right_guess:
            guess = input("Take a guess at the unscrambled word: ")
            attempts_used += attempt_value
            if guess == unscrambled_word:
                right_guess = True
                print(f"Congrats, that is correct! The word was {unscrambled_word}")
            else:
                print("Nope, try again!")

        if right_guess:
            print("You win, player. Well done!")
            scores["a"] += 1
            print(f"Your current Anagramma score: {scores["a"]}")
        else:
            print(f"Unlucky! The word was {unscrambled_word}.")
            print(f"Your current Anagramma score: {scores["a"]}")

        again = input("Play again? (y/n): ").lower()
        if again != "y":
            break


# PAPER SCISSORS ROCK
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
        point_value = 1

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
                consecutive_wins += point_value
            else:
                print(f"You lost. {comp_choice} beats {user_choice}.")
                finished = True

        print(f"Game over. You had {consecutive_wins} consecutive wins!")
        if consecutive_wins > scores["psr"]:
            scores["psr"] = consecutive_wins
            print(f"🎉 New best streak: {consecutive_wins} wins!")
        else:
            print(f"Your best streak so far: {scores['psr']} wins.")
        again = input("Play again? (y/n): ").lower()
        if again != "y":
            break


# BLACKJACK
def play_blackjack():
    print(
        """
        WELCOME TO BLACKJACK!!!
        
        You start with $100. Make a bet. If you win it is doubled, if you lose, 
        that money is given to the dealer. 

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
        # giving player starting money
        player_money = 100

        while True:
            if player_money <= 0:
                print("You're out of money! Game over. No score saved.")
                return

            print(f"You have ${player_money}.")
            # get bet from player
            while True:
                try:
                    bet = int(input("Place your bet: $"))
                    if 1 <= bet <= player_money:
                        break
                    else:
                        print(f"Bet must be between $1 and ${player_money}.")
                except ValueError:
                    print("Enter a valid number.")

            top_num = 21
            dealer_must = 17
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
            deck = [
                (card, category) for category in card_categories for card in cards_list
            ]
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
                    if score(player_card) > top_num:
                        print(
                            f"Your cards: {', '.join([f'{r} of {s}' for r,s in player_card])} (score {player_score})"
                        )
                        print("BUST! Dealer wins.")
                        player_money -= bet
                        break
                elif choice == "s":

                    while dealer_score < dealer_must:
                        dealer_card.append(deck.pop())
                        dealer_score = score(dealer_card)
                    print(
                        f"Dealer's cards: {', '.join([f'{crd} of {sut}' for crd,sut in dealer_card])} (score {dealer_score})"
                    )
                    if dealer_score > top_num or player_score > dealer_score:
                        print("Player wins!")
                        player_money += bet
                    elif dealer_score > player_score:
                        print("Dealer wins!")
                        player_money -= bet
                    else:
                        print("It's a tie. (Push)")
                    break

            print(f"Your balance: ${player_money}")

            new_round = input("Play another hand? (y/n): ").lower()
            while new_round != "y" and new_round != "n":
                print("Invalid input. Try again")
                new_round = input("Play another hand? (y/n): ").lower()

            if new_round != "y":
                if player_money > 0:
                    if player_money > scores["bj"] or scores["bj"] == 0:
                        scores["bj"] = player_money
                        print(
                            f"Your new highest Blackjack score saved: ${player_money}"
                        )
                    else:
                        print(f"Your highscore remains {scores["blackjack"]}.")
                else:
                    print("No score saved because you went broke.")
                break

        again = input("Play again? (y/n): ").lower()
        if again != "y":
            break


# MENU
def show_menu():
    print(
        """   
        Choose a game:
        gtn - Guess the Number
        a   - Anagramma
        psr - Paper Scissors Rock
        bj  - Blackjack
        show - Show scoreboard
        quit - Exit PlayTopia
        """
    )
    return input("Your choice: ").lower()


# GAME FUNCTION NAME DICTIONARY
games = {
    "gtn": play_guess_the_number,
    "a": play_anagramma,
    "psr": play_psr,
    "bj": play_blackjack,
}


# ONE-OFF WELCOME MESSAGE
print(
    """ 
        WELCOME TO PLAYTOPIA!
        
        We have a range of games to offer for you!
        
        Give some a go and don't forget to have fun!    
    """
)

# GAME RUNNING LOOP
while True:
    choice = show_menu()
    if choice in games:
        pick = games[choice]
        pick()
    elif choice == "quit":
        print("Thanks for playing PlayTopia!")
        break
    elif choice == "show":
        print("\n--- SCOREBOARD ---")
        for game, score in scores.items():
            if score != 0:
                print(f"{game}: {score}")
        print("------------------\n")
    else:
        print("Invalid choice. Try again.")
