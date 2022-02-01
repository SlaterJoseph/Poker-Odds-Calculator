from probability_helper import process_flushes, truncate

def calculate_straight_flush(hand, table, round):
    if round == 'preflop':
        probability = [flop(hand), turn(hand), river(hand), flop(hand) + turn(hand) + river(hand)]

    elif round == 'flop':
        if turn(hand, table[0:3]) == 100: #If the probabilty is 100, we found a three of a kind on the flop
            probability = [flop(hand), 100, 100, 100] #no need to check the what the likelyhood is for future rounds

        else: #if there isn't a three of a kind, we pass the table's first 3 cards and the hand to the methods
            probability = [flop(hand), turn(hand, table[0:3]), river(hand, table[0:3]),\
                 turn(hand, table[0:3]) + river(hand, table[0:3])]
    
    elif round == 'turn':
        if turn(hand, table[0:3]) == 100: #checks if the flop contained threes
            probability = [flop(hand), 100, 100, 100]

        elif river(hand, table[0:4]) == 100:#checks if the turn contained threes
            probability = [flop(hand), turn(hand, table[0:3]), 100, 100]

        else:
            probability = [flop(hand), turn(hand, table[0:3]), river(hand, table[0:4]), river(hand, table[0:4])]

    else:
        if turn(hand, table[0:3]) == 100: #checks if the flop contained threes
            probability = [flop(hand), 100, 100, 100] 

        elif river(hand, table[0:4]) == 100: #checks if the turn contained threes
            probability = [flop(hand), turn(hand, table[0:3]), 100, 100] 

        elif final_check(hand, table) == 100: #to see if by the end of the game there is threes
            probability = [flop(hand), turn(hand, table[0:3]), river(hand, table[0:4]), 100]

        else:
            probability = [flop(hand), turn(hand, table[0:3]), river(hand, table[0:4]), 0]

    return probability
    
def flop(hand):
    ranks = {hand[0].get_value(), hand[1].get_value()}
    return truncate(flop_threes)

def turn(hand, table = 'n/a'):
    if table == 'n/a': #No flop is available yet
        
    else:
        
    return truncate(turn_threes)

def river(hand, table = 'n/a'):
    if table == 'n/a':

    elif len(table) == 3:
        
    else:
        
    return truncate(river_threes)

def final_check(hand, table = 'n/a'):
    suits = dict({'heart':0, 'spade':0, 'diamond':0, 'club':0})
    suits[hand[0].get_suit] += 1
    suits[hand[1].get_suit] += 1
    suits[table[0].get_suit] += 1
    suits[table[1].get_suit] += 1
    suits[table[2].get_suit] += 1
    suits[table[3].get_suit] += 1
    suits[table[4].get_suit] += 1
    return 100 if process_flushes(suits, 2) >= 1 else 0 
