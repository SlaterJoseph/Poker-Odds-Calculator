from probability_helper import truncate
from probability_helper import process_dictionary

def calculate_threes(hand, table, round):
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
    if len(ranks) == 1: #checks if the player's hand is pocket pairs
        flop_threes = (2 * 1128) / 19600
    else: #if the two cards do not make a pair
        flop_threes = (2 * 3 * 48) / 19600

    return truncate(flop_threes)

def turn(hand, table = 'n/a'):
    if table == 'n/a': #No flop is available yet
        ranks = {hand[0].get_value(), hand[1].get_value()}
        if len(ranks) == 1: #player's hand is a pocket pair
            turn_threes = (17296 / 19600) * (2 / 47)
        else: #player's hand is not a pair
            turn_threes = ((2 * 3 * 1128) / 19600) * (2 / 47)

    else:
        ranks = dict({1:0 , 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0, 12:0, 13:0})
        ranks[hand[0].get_value()] += 1#adds all avialable cards to the ranks dictionary 
        ranks[hand[1].get_value()] += 1
        ranks[table[0].get_value()] += 1
        ranks[table[1].get_value()] += 1
        ranks[table[2].get_value()] += 1
        pair_count = process_dictionary(ranks, 2) #check how many pairs there are

        if pair_count == 2: #There are 2 pairs the player hass access to
            turn_threes = 4 / 47
        elif pair_count == 1: #There is 1 pair the player has access to
            turn_threes = 2 / 47
        else: #There are no pairs on the table, so a 3 of a kind is impossible
            turn_threes = 0

    return truncate(turn_threes)
    

def river(hand, table = 'n/a'):
    if table == 'n/a':
        ranks = {hand[0].get_value(), hand[1].get_value()}
        if len(ranks) == 1: #player's hand is a pocket pair
            river_threes = (17296 / 19600) * (46 / 47) * (2 / 46)
        else: #player's hand is not a pair
            river_threes = ((2 * 3 * 1128) / 19600) * (46 / 47) * (2 / 46) + \
                (17296 / 19600) * ((2 * 3) / 47) * (2 / 46)

    elif len(table) == 3:
        ranks = dict({1:0 , 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0, 12:0, 13:0})
        ranks[hand[0].get_value()] += 1#adds all avialable cards to the ranks dictionary 
        ranks[hand[1].get_value()] += 1
        ranks[table[0].get_value()] += 1
        ranks[table[1].get_value()] += 1
        ranks[table[2].get_value()] += 1
        pair_count = process_dictionary(ranks, 2) #check how many pairs there are

        if pair_count == 2: #There are 2 pairs
            river_threes = (43 / 47) * (4 / 46) + (3 / 47) * (2 / 46)
        elif pair_count == 1: #There is 1 pair
            river_threes = (45 / 47) * (2 / 46) + ((3 * 3) / 47) * (2 / 46)
        else: #There are no pairs
            river_threes = ((5 * 3) / 47) * (2 / 46)

    else:
        ranks = dict({1:0 , 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0, 12:0, 13:0})
        ranks[hand[0].get_value()] += 1#adds all avialable cards to the ranks dictionary 
        ranks[hand[1].get_value()] += 1
        ranks[table[0].get_value()] += 1
        ranks[table[1].get_value()] += 1
        ranks[table[2].get_value()] += 1
        ranks[table[3].get_value()] += 1
        pair_count = process_dictionary(ranks, 2) #check how many pairs there are

        if pair_count == 3: #There are 3 pairs
            river_threes = 6 / 46
        elif pair_count == 2: #There are 2 pairs
            river_threes = 4 / 46
        elif pair_count == 1: #There is 1 pair
            river_threes = 2 / 46
        else: #There are no pairs yet
            river_threes = 0
        


    return truncate(river_threes)

def final_check(hand, table = 'n/a'):
    ranks = dict({1:0 , 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0, 12:0, 13:0})
    ranks[hand[0].get_value()] += 1#adds all avialable cards to the ranks dictionary 
    ranks[hand[1].get_value()] += 1
    ranks[table[0].get_value()] += 1
    ranks[table[1].get_value()] += 1
    ranks[table[2].get_value()] += 1
    ranks[table[3].get_value()] += 1
    ranks[table[4].get_value()] += 1
    return 100 if process_dictionary(ranks, 3) >= 1 else 0
