from probability_helper import truncate, process_matches

def calculate_two_pair(hand, table, round):
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
    if len(ranks) == 1:
        flop_two_pair = ((66 * 4 * 6) / 19600) + ((12 * 4) / 19600) + ((2 * 12 * 6) / 19600)

    else:
        flop_two_pair = ((3 * 3 * 11 * 4) / 19600) + ((2 * 3 * 11 * 6) / 19600) + ((2 * 3 * 3) / 19600)
    return truncate(flop_two_pair)

def turn(hand, table = 'n/a'):
    if table == 'n/a': #No flop is available yet
        ranks = {hand[0].get_value(), hand[1].get_value()}
        if len(ranks) == 1:
           turn_two_pair = ((220 * 4 * 4 * 4)/19600) * (9 / 47) + ((2 * 66 * 4 * 4)/19600) * (6 / 47) \
           + ((12 * 4)/19600) * (3 / 47)

        else:
            turn_two_pair =  (((2 * 3 * 55 * 4 * 4) / 19600) * (9 / 47)) + (((55 * 6 * 4) / 19600) * (9 / 47)) \
            + (((11 * 4) / 19600) * ((6 / 47))) + ((2 / 19600) * (3 / 47)) + (((2 * 3 * 11 * 4) / 19600) * (6 / 47))
    else:
        ranks = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0, 12:0, 13:0}
        ranks[hand[0].get_value()] += 1
        ranks[hand[1].get_value()] += 1
        ranks[table[0].get_value()] += 1
        ranks[table[1].get_value()] += 1
        ranks[table[2].get_value()] += 1

        if process_matches(ranks, 4) == 1: # if we have fours, only 1 card can make a pair on the flop
            turn_two_pair = 3 / 47 

        elif process_matches(ranks, 3) == 1: #if we have 3s, 2 cards can make a pair on the flop
            turn_two_pair = 6 / 47 

        elif process_matches(ranks, 2) == 1: #if we have 1 pair, 3 cards can make a pair on the flop
            turn_two_pair = 9 / 47 

        else: #either we have no pairs or 2 pairs
            turn_two_pair = 0 if process_matches(ranks, 2) == 0 else 100
    return truncate(turn_two_pair)

def river(hand, table = 'n/a'):
    if table == 'n/a':
        ranks = {hand[0].get_value(), hand[1].get_value()}
        if len(ranks) == 1:
            river_two_pair = (((2 * 66 * 4 * 4) / 19600) * ((10 * 4) / 47) * (9 / 46)) \
            + (((220 * 4 * 4 * 4) / 19600) * ((9 * 4) / 47) * (12 / 46)) + (((12 * 4) / 19600) * ((11 * 4) / 47) * (6 / 46)) \
            + (((220 * 4 * 4 * 4) / 19600) * ((2 * 4) / 47) * (9 / 46)) + (((2 * 66 * 4 * 4) / 19600) * (1 / 47) * (9 / 46))
        else:
            river_two_pair =  (((2 * 3 * 55 * 4 * 4) / 19600) * ((9 * 4) / 47) * (12 / 46)) \
            + (((2 * 3 * 11 * 4) / 19600) * ((10 * 4) / 47) * (9 / 46)) + ((2  / 19600) * ((11 * 4) / 47) * (6 / 46)) \
            + (((55 * 6 * 4) / 19600) * ((9 * 4) / 47) * (12 / 46)) + (((11 * 4) / 19600) * ((10 * 4) / 47) * (9 / 46)) \
            + (((165 * 4 * 4 * 4) / 19600) * ((2 * 3) / 47) * (12 / 46)) \
            + (((2 * 3 * 55 * 4 * 4) / 19600) * (2 / 47) * (9 / 46)) + (((2 * 3 * 11 * 4 * 4) / 19600) * (1 / 47) * (6 / 46)) \
            + (((165 * 4 * 4 * 4) / 19600) * ((3 * 3) / 47) * (12 / 46)) \
            + (((55 * 6 * 4) / 19600) * (2 / 47) * (9 / 46)) + (((11 * 4) / 19600) * (1 / 47) * (6 / 46))

    elif len(table) == 3:
        ranks = dict({1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0, 12:0, 13:0})
        ranks[hand[0].get_value()] += 1
        ranks[hand[1].get_value()] += 1
        ranks[table[0].get_value()] += 1
        ranks[table[1].get_value()] += 1
        ranks[table[2].get_value()] += 1

        if process_matches(ranks, 4) == 1: # if we have fours, only 1 card can make a pair on the flop
            river_two_pair = ((11 * 4) / 47) * (6 / 46) 

        elif process_matches(ranks, 3) == 1: #if we have 3s, 2 cards can make a pair on the flop
            river_two_pair = (2 / 47) * (6 / 46) + ((10 * 4) / 47) * (9 / 46) 

        elif process_matches(ranks, 2) == 1: #if we have 1 pair, 3 cards can make a pair on the flop
            river_two_pair = ((9 * 4) / 47) * (12 / 46) + (2 / 47) * (9 / 46)  

        else: #either we have no pairs or 2 pairs
            river_two_pair = ((5 * 3) / 47) * ((4 * 3) / 46) if process_matches(ranks, 2) == 2 else 0
    else:
        ranks = dict({1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0, 12:0, 13:0})
        ranks[hand[0].get_value()] += 1
        ranks[hand[1].get_value()] += 1
        ranks[table[0].get_value()] += 1
        ranks[table[1].get_value()] += 1
        ranks[table[2].get_value()] += 1
        ranks[table[3].get_value()] += 1
        if process_matches(ranks, 4) == 1: # if we have fours, only 1 card can make a pair on the flop
            river_two_pair = (6 / 46) 

        elif process_matches(ranks, 3) == 1: #if we have 3s, 2 cards can make a pair on the flop
            river_two_pair = (9 / 46) 

        elif process_matches(ranks, 2) == 1: #if we have 1 pair, 3 cards can make a pair on the flop
            river_two_pair = (12 / 46)  

        else: #either we have no pairs or 2 pairs
            river_two_pair = 0 if process_matches(ranks, 2) == 0 else 100

    return truncate(river_two_pair)

def final_check(hand, table = 'n/a'):
    ranks = dict({1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0, 12:0, 13:0})
    ranks[hand[0].get_value()] += 1
    ranks[hand[1].get_value()] += 1
    ranks[table[0].get_value()] += 1
    ranks[table[1].get_value()] += 1
    ranks[table[2].get_value()] += 1
    ranks[table[3].get_value()] += 1
    ranks[table[4].get_value()] += 1
    return 100 if process_matches(ranks, 2) >= 2 else 0