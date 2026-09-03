# day 011
#Blackjack game

import random
# from art import logo

def deal_cards():
    """return a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def compare(u_score, c_score):
    if u_score == c_score:
        return "draw"
    elif u_score == 0:
        return "win with a BlackJack"
    elif c_score == 0:
        return "computer wins with a BlackJack"
    elif u_score > 21:
        return "you went over, you lose"
    elif c_score > 21:
        return "the computer went over, you win"
    elif u_score > c_score:
        return "you win"
    else:
        return "you lose"

def play_game():
    # print(logo)
    user_cards = []
    computer_cards = []
    computer_score = -1
    user_score = -1
    is_game_over = False

    def calculate_score(cards):
        if sum(cards) == 21 and len(cards) == 2:
            return 0 #blackjack
        if 11 in cards and sum(cards) > 21 :
            cards.remove(11)
            cards.append(1)

        return sum(cards)

    for _ in range(2):
        user_cards.append(deal_cards())
        computer_cards.append(deal_cards())


    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"your cards: {user_cards}, your score: {user_score}")
        print(f"computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("do you want to draw another card? type 'y' for yes and 'n' for no: ").lower()
            if user_should_deal == "y":
                user_cards.append(deal_cards())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_cards())
        computer_score = calculate_score(computer_cards)

    print(f"your final hand: {user_cards}, your final score: {user_score}")
    print(f"computer's final hand: {computer_cards}, computer's final score: {computer_score}")
    print(compare(user_score, computer_score))

while input("do you want to play BlackJack? type 'y' for yes and 'n' for no: ").lower() == "y":
    print("\n" * 20)
    play_game()
