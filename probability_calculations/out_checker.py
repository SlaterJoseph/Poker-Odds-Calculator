from ..poker_components.card import Card

def total_outs(cards, round):
    return 

def matching_outs(cards, round): #this method calculates all outs for a pair, 2 pair, 3 of a kind, full house, and 4 of a kind
    if round == 'river': #the game is over, your hand cannot improve anymore
        return 0
    size = size_getter(round)
    set_of_cards = set(cards[i].get_value() for i in cards) #making a set so any doubles a removed, indicating a pair or more
    total_outs = size * 3 #every rank has 4 cards, so if one is on the table 3 remain
    outs_lost = (size - len(set_of_cards)) * 4 #
    return total_outs - outs_lost

def flush_outs(cards, round):
    if round == 'river':#the game is over, your hand cannot improve anymore
        return 0
    size = size_getter(round)

def straight_outs(cards, round):
    if round == 'river':#the game is over, your hand cannot improve anymore
        return 0
    size = size_getter(round)

#this method is so I don't need to copy this chain of if else a lot. It returns the amount of cards in play
def size_getter(round): 
    if round == 'preflop':
        return 2   
    elif round == 'flop':
        return 5
    elif round == 'turn':
        return 6
    else:
        return 7