import Blackjack_art
import random

user_cards = []
dealer_cards = []
game_over = False


def deal_card():
    """Returns a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    """Take a list of cards and return the score calculated from the cards"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare(user_score, dealer_score):
    if user_score == dealer_score:
        return ("\n\n\t\t\t DRAW!\n\tYour cards: {user_cards}, score: {user_score}\n\tDealer cards: {"
                "dealer_cards}, score: {dealer_score}")
    elif dealer_score == 0:
        return ("\n\n\t\t\t DEALER BLACKJACK! YOU LOSE.\n\tYour cards: {user_cards}, score: {user_score}\n\tDealer "
                "cards: {dealer_cards}, score: {dealer_score}")
    elif user_score == 0:
        return ("\t\t\t\nBLACKJACK! YOU WIN!\n\tYour cards: {user_cards}, score: {user_score}\n\tDealer cards: {"
                "dealer_cards}, score: {dealer_score}")
    elif user_score > 21:
        return (f"\n\t\t\t\tBUST!\n\tYour cards: {user_cards}, score: {user_score}\n\tDealer cards: {dealer_cards}, "
                f"score: {dealer_score}")
    elif dealer_score > 21:
        return f"\n\n\t\t\t DEALER BUST. YOU WIN!\n\tYour cards: {user_cards}, score: {user_score}\n\tDealer cards: {dealer_cards}, score: {dealer_score}"
    elif user_score > dealer_score:
        return f"\n\n\t\t\t\tYOU WIN!\n\tYour cards: {user_cards}, score: {user_score}\n\tDealer cards: {dealer_cards}, score: {dealer_score}"
    else:
        return f"\n\n\t\t\t\tYOU LOSE.\n\tYour cards: {user_cards}, score: {user_score}\n\tDealer cards: {dealer_cards}, score: {dealer_score}"


def blackjack():
    global game_over, dealer_cards, user_cards
    game_over = False
    for _ in range(2):
        user_cards.append(deal_card())
        dealer_cards.append(deal_card())

    while not game_over:
        user_score = calculate_score(user_cards)
        dealer_score = calculate_score(dealer_cards)
        print(f"\tYour cards: {user_cards}, score: {user_score}\n\tDealers card: {dealer_cards[0]}")

        if user_score == 0 or dealer_score == 0 or user_score > 21:
            game_over = True

        else:
            hit_or_stand = input("Type 'y' to HIT, or 'n' to STAND: ").lower()
            if hit_or_stand == 'y':
                user_cards.append(deal_card())  # PLAYER HIT
                user_score = calculate_score(user_cards)
            else:
                game_over = True

    while dealer_score != 0 and dealer_score < 17:
        dealer_cards.append(deal_card())
        dealer_score = calculate_score(dealer_cards)

    print(compare(user_score, dealer_score))


while input("\n\nDo you want to play a hand of Blackjack?: 'y' or 'n'").lower() == 'y':
    print(Blackjack_art.logo)
    print("\t\t\t\tWELCOME!\n")
    user_cards.clear()
    dealer_cards.clear()
    blackjack()
else:
    print("\n\n\t\t\tGoodbye.")
