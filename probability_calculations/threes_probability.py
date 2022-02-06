from probability_helper import truncate, process_matches, build_ranks


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
    if len(ranks) == 1: #Our hand contains a pocket pair
        flop_threes = ((2 * 66 * 4 * 4) / 19600) + ((12 * 4) / 19600) * ((12 * 4) / 19600) \
        + ((2 * 12 * 6) / 19600)
    else:
        flop_threes = ((2 * 3 * 11 * 4) / 19600) + (2 / 19600) * ((11 * 4) / 19600) \
        + ((2 * 3 * 3) / 19600)
    return truncate(flop_threes)

def turn(hand, table = 'n/a'):
    if table == 'n/a': #No flop is available yet
        ranks = {hand[0].get_value(), hand[1].get_value()}
        if len(ranks) == 1: #Our hand contains a pocket pair
            turn_threes = (((220 * 4 * 4 * 4) / 19600) * (2 / 47)) + (((66 * 6 * 4) / 19600) * (4 / 47))
        else:
            turn_threes = (((2 * 3 * 55 * 4 * 4) / 19600) * (2 / 47)) + (((3 * 3 * 11 * 4) / 19600) * (4 / 47)) \
            + (((2 * 3 * 11 * 6) / 19600) * (4 / 47)) + (((55 * 6 * 4) / 19600) * (2 / 47))
    else:
        ranks = build_ranks(hand, table, 3)
        if process_matches(ranks, 3) >= 1:
            turn_threes = 100
        elif process_matches(ranks, 2) == 2:
            turn_threes = 4 / 47
        elif process_matches(ranks, 2) == 1:
            turn_threes = 2 / 47
        else:
            turn_threes = 0

    return truncate(turn_threes)

def river(hand, table = 'n/a'):
    if table == 'n/a':
        ranks = {hand[0].get_value(), hand[1].get_value()}
        if len(ranks) == 1: #Our hand contains a pocket pair
            river_threes = (((66 * 6 * 4) / 19600) * (3 / 47) * (6 / 46)) \
            + (((220 * 4 * 4 * 4) / 19600) * ((9 * 4) / 47) * (2 / 46))\
            + (((66 * 6 * 4) / 19600) * (10 / 47) * (4 / 46)) + (((220 * 4 * 4 * 4) / 19600) * ((3 * 3) / 47) * (4 / 46))
        else:
            river_threes = (((2 * 3 * 55 * 4 * 4) / 19600) * ((9 * 4) / 47) * (2 / 46))\
            + (((3 * 3 * 11 * 4) / 19600) * ((10 * 4) / 47) * (4 / 46)) \
            + (((3 * 3 * 11 * 4) / 19600) * ((3 / 47) * (6 / 46))) \
            + (((55 * 6 * 4 ) / 19600) * ((9 * 4) / 47) * (2 / 46)) \
            + (((11 * 6 * 2 * 3) / 19600) * ((10 * 4) / 47) * (4 / 46)) \
            + (((165 * 4 * 4 * 4) / 19600) * ((3 * 3) / 47) * (2 / 46)) \
            + (((11 * 6 * 2 * 3) / 19600) * (3 / 47) * (6 / 46)) \
            + (((2 * 3 * 55 * 4 * 4) / 19600) * (3 / 47) * (4 / 46)) \
            + (((55 * 6 * 4) / 19600) * (3 / 47) * (4 / 46)) \
            + (((165 * 4 * 4 * 4) / 19600) * ((2 * 3) / 47) * (2 / 46)) \
            + (((2 * 3 * 55 * 4 * 4) / 19600) * ((2 * 3) / 47) * (4 / 46))

    elif len(table) == 3:
        ranks = build_ranks(hand, table, 3)
        if process_matches(ranks, 2) == 2:
            river_threes = ((3 / 47) * (6 / 46)) + (((10 * 4) / 47) * (4 / 46))
        elif process_matches(ranks, 2) == 1:
            river_threes = (((9 * 4) / 47) * (2 / 46)) + (((3 * 3) / 47) * (4 / 46))
        else:
            river_threes = ((5 * 3) / 47) * (2 / 46)

    else: #We have the turn avialable 
        ranks = build_ranks(hand, table, 4)
        if process_matches(ranks, 2) == 3:
            river_threes = 6 / 46
        elif process_matches(ranks, 2) == 2:
            river_threes = 4 / 46
        elif process_matches(ranks, 2) == 1:
            river_threes = 2 / 46
        else:
            river_threes = 0 if process_matches(ranks, 3) == 0 else 100
    return truncate(river_threes)

def final_check(hand, table = 'n/a'):
    ranks = build_ranks(hand, table, 5)
    return 100 if process_matches(ranks, 3) >= 1 else 0