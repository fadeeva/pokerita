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

    
with open('deck.pickle', 'rb') as f:
    deck = pickle.load(f)

deck_in_game = deck.copy()
random.shuffle(deck_in_game)

number_of_players, players = get_players(min=2, max=10)
stop_list_players = []


while True:
    
    if number_of_players != len(stop_list_players):
        command = input('Call(c), Fold(f), Raise(r[number]), All-In(a): ')
        if execute_command(command):
            continue
    
    break