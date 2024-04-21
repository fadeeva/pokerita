import random
import pickle
from typing import List, Set, Dict, Tuple


def get_players(min=2, max=10)->List:
    number_of_players = int(input('Enter number of players 2-10: '))
    if number_of_players > 10 or number_of_players < 2:
        number_of_players = 2
    players = [[] for i in range(number_of_players)]
    
    return [number_of_players, players]


def execute_command(command: str)->bool:
    return False


def get_card(amount: int)->List[str]:
    cards = []
    for n in amount:
        cards.append(deck_in_game[random.randint(0, len(deck_in_game)-1)])
    
    return cards 


def play_stage(stage: str):
    
    if stage == 'preflop':
        get_card(2)
    elif stage == 'flop':
        get_card(1)
    elif stage == 'turn':
        get_card(1)
    else:
        get_card(1)


with open('deck.pickle', 'rb') as f:
    deck = pickle.load(f)

deck_in_game = deck.copy()
random.shuffle(deck_in_game)

number_of_players, players = get_players(min=2, max=10)
stop_list_players = []

stages = ['preflop', 'flop', 'turn', 'river']

while True:
    
    for s in stages:
        print('----------------------')
        print(f'----- {s} -----')
        print('----------------------')
        
        play_stage(s)
        
        if number_of_players != len(stop_list_players):
            command = input('Call(c), Fold(f), Raise(r[number]), All-In(a): ')
            if execute_command(command):
                continue
    
    break