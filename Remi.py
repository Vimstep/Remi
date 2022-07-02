import time
import random

player_card = {'1': 0, '2': 0, '3': 0, '4': 0,'5': 0,
               '6': 0, '7':0, '8':0, '9': 0, 'king': 0,
               'joker': 0, 'queen':0}
player_wins = 0

card_types = ["B","S","D","L"]

computer_cards = {'1': 0, '2': 0, '3': 0, '4': 0,'5': 0,
               '6': 0, '7':0, '8':0, '9': 0, 'king': 0,
               'joker': 0, 'queen': 0}

computer_wins = 0

print("Welcome to remi. Press q to start")
answer = input()



def print_cards(cards, cardtype):
    for i in range(7):
        if card is card[joker]:
            print("("+ str(card[joker])+ str(random.choice(list(cards.values()))))
        elif card is card[queen]:
            print("("+ str(card[queen])+ str(random.choice(list(cards.values()))))
        elif card is card[king]:
            print("("+ str(card[king])+ str(random.choice(list(cards.values()))))
        else:
             print(str("("+card_types[random.randint(0, 3)]) +""+ str(random.choice(list(cards.keys())))+""+ str(random.choice(list(cards.values()))) + ")" , end="")
def check_number(cards):
    value = sum(cards)
    if value < 7:
        print("david")






if 'q' in answer:
    #start game
    print_cards(player_card, card_types)
    



    
