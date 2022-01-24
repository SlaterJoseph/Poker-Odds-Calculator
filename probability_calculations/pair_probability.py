import poker_components
import probability
from ..poker_components import card

def calculate_pair_oods(hand, table, round):
    all_cards = []
    all_cards.extend(hand)
    all_cards.extend(table)

    ranks = set()
    ranks.add(hand[0].get_value())
    ranks.add(hand[1].get_value())


    if round == 'flop':
        total = 5
        ranks.add(table[0].get_value())
        ranks.add(table[1].get_value())
        ranks.add(table[2].get_value())
    elif round == 'turn':
        total = 6
        ranks.add(table[0].get_value())
        ranks.add(table[1].get_value())
        ranks.add(table[2].get_value())
        ranks.add(table[3].get_value())
    elif round == 'river':
        total = 7
        ranks.add(table[0].get_value())
        ranks.add(table[1].get_value())
        ranks.add(table[2].get_value())
        ranks.add(table[3].get_value())
        ranks.add(table[4].get_value())
    else:
        total = 2

    if len(ranks) < total:
        return 100
    elif len(ranks) == total and round == 'river':
        return 0
    else:
        

            
    
    