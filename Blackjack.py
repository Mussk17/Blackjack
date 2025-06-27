import random
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# Returns random cards for user and computer
random_two_user = random.sample(cards, 2)
random_computer = random.choice(cards)

# Game starts (Round 1)
def deal_card():
    print(f"Your cards: {random_two_user}, current score: {sum(random_two_user)}")
    print(f"Computer's first card: {random_computer}")

# Round 2
def calculate_score():
    user_cards = []
    computer_cards = []

    # Append for user_cards
    user_cards.append(random_two_user)   # list of 2 cards

    # Flatten user_cards
    flat_cards_user = []
    for item in user_cards:
        if isinstance(item, list):
            flat_cards_user.extend(item)
        else:
            flat_cards_user.append(item)

    print(f"Your cards: {flat_cards_user}, current score: {sum(flat_cards_user)}")
    print(f"Computer's first card: {random_computer}")

    # Append for computer (no flattening needed)
    computer_cards.append(random_computer)
    computer_cards.append(random_computer)

    return  flat_cards_user, computer_cards


# Game
def blackjack_game():
    print(logo)

    choice_to_play = input("Do you want to play a game "
                           "of Blackjack? Type 'y' or 'n':").lower()

    if choice_to_play == 'y':
        print("\nGreat! Let's start the game.😄\n")
        deal_card()
    elif choice_to_play == 'n':
        print("\nMaybe next time. Goodbye!🙋🏻‍♀️")

    else:
        print("Invalid input. Please enter 'y' or 'n'.")
        choice_2 = input("Type 'y to get another card, type 'n to pass:").lower()

        if choice_2 == 'y':
            calculate_score()
        elif choice_2 == 'n':
            calculate_score()

            # Final Round - inner function
            def result(flat_cards_user, computer_cards):

                print("Result:\n")
                print(f"Your final hand: {flat_cards_user}, final score: {sum(flat_cards_user)}")
                print(f"Computer's final hand: {computer_cards}, final score: {sum(computer_cards)}")
                sum_user = sum(flat_cards_user)
                sum_comp = sum(computer_cards)

                result(sum_user, sum_comp)

blackjack_game()



"""that takes a List of cards as input and returns the sum of all the cards in the List as the score. Google the sum() function to help you do this."""
# calculate_score() t