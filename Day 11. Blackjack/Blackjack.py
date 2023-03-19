import random
import blackjack_art
import time
import os

def BLACKJACK_game_start ():
    if input("Do you want to play blackjack? type 'y' or 'n': ") == 'y':
        for i in range(10):
            print('\n')
        BLACKJACK()
        return
    else:
        print('Good bye')
        return
def BLACKJACK():
    time_sec = 1

    def card_distribution(number_of_cards):
        card_deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        card_list = []
        for card in range(number_of_cards):
            card_value = random.choice(card_deck)
            card_list.append(card_value)
        return card_list

    def score_counter(cards):
        score = 0
        for index, item in enumerate(cards):
            if score >21:
                if item == 11:
                    cards[index] = 1
            score += item
        if cards[0] + cards[1] == 21:
            score = 0
        return score

    def user_turn_func(cards):
        answer = input("do you need one more card? type 'y' or 'n': ")
        if answer == 'y':
            cards += card_distribution(1)
            return [True, cards]
        elif answer == 'n':
            return [False, cards]

    def dealer_turn_func(cards):
        if dealer_score < 17:
            cards += card_distribution(1)
            print('dealer cards: ', end='')
            time.sleep(time_sec)
            print(*cards)
            return [True, cards]
        else:
            return [False, cards]

    print(blackjack_art.logo)

    user_cards = []
    user_score = 0
    user_turn = True

    dealer_cards = []
    dealer_score = 0
    dealer_turn = True

    # add two cards to user and check blackjack
    user_cards += card_distribution(2)
    user_score = score_counter(user_cards)
    if user_score == 0:
        user_turn = False
        dealer_turn = False
    print(f'your cards is: ', end='')
    time.sleep(time_sec)
    print(*user_cards)
    time.sleep(time_sec)

    # add two cards to dealer and check blackjack
    dealer_cards += card_distribution(2)
    dealer_score = score_counter(dealer_cards)
    print(f'Dealer cards is: {dealer_cards[0]} X')
    if dealer_score == 0:
        dealer_turn = False


    # User turn:
    while user_turn == True:
        if user_score > 21:
            user_turn = False
            print('Your score is more than 21')
        else:
            user_turn_list = user_turn_func(user_cards)
            user_turn = user_turn_list[0]
            user_cards = user_turn_list[1]
            user_score = score_counter(user_cards)
            time.sleep(time_sec)
            print('your cards:', end='')
            print(*user_cards)

    # dealer_turn
    while dealer_turn == True:
        print(f'Dealer cards is: ', end='')
        time.sleep(time_sec)
        print(*dealer_cards)
        if dealer_turn > 21:
           dealer_turn == False
        elif dealer_score == 0:
            time.sleep(time_sec)
            print('Dealer has a Blackjack')
        else:
            dealer_turn_list = dealer_turn_func (dealer_cards)
            dealer_turn = dealer_turn_list[0]
            dealer_cards = dealer_turn_list[1]
            dealer_score = score_counter(dealer_cards)


    # score comparison
    def score_compare(user_scr, dealer_scr):
        if dealer_scr == 0:
            return 'Dealer has a Blackjack. Player lose'
        elif user_scr < 22 and (dealer_scr < user_scr or dealer_scr > 21):
            return 'Player win'
        elif user_scr > 21:
            return 'Player lose'
        elif user_scr == dealer_scr:
            return 'draw'

    time.sleep(time_sec)
    print(f'Player score is: {user_score}', f'Dealer score is: {dealer_score}', sep='\n')
    time.sleep(time_sec)
    print(score_compare(user_score, dealer_score))
    time.sleep(time_sec)
    BLACKJACK_game_start()



BLACKJACK_game_start()


