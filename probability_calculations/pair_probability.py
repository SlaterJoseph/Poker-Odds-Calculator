from probability_helper import truncate, process_matches

def calculate_pair(hand, table, round):
    ranks = {hand[0].get_value(), hand[1].get_value()}
    if len(ranks) == 1:
        probability = [100, 100, 100, 100]
    elif round == 'preflop':
        probability = [flop(hand), turn(hand), river(hand), flop(hand) + turn(hand) + river(hand)]

    elif round == 'flop':
        if turn(hand, table[0:3]) == 100: #If the probabilty is 100, we found a pair on the flop
            probability = [flop(hand), 100, 100, 100] #no need to check the what the likelyhood is for future rounds

        else: #if there isn't a three of a kind, we pass the table's first 3 cards and the hand to the methods
            probability = [flop(hand), turn(hand, table[0:3]), river(hand, table[0:3]),\
                 turn(hand, table[0:3]) + river(hand, table[0:3])]
    
    elif round == 'turn':
        if turn(hand, table[0:3]) == 100: #checks if the flop contained a pair
            probability = [flop(hand), 100, 100, 100]

        elif river(hand, table[0:4]) == 100:#checks if the turn contained a pair
            probability = [flop(hand), turn(hand, table[0:3]), 100, 100]

        else:
            probability = [flop(hand), turn(hand, table[0:3]), river(hand, table[0:4]), river(hand, table[0:4])]

    else:
        if turn(hand, table[0:3]) == 100: #checks if the flop contained a pair
            probability = [flop(hand), 100, 100, 100] 

        elif river(hand, table[0:4]) == 100: #checks if the turn contained a pair
            probability = [flop(hand), turn(hand, table[0:3]), 100, 100] 

        elif final_check(hand, table) == 100: #to see if by the end of the game there is a pair
            probability = [flop(hand), turn(hand, table[0:3]), river(hand, table[0:4]), 100]

        else:
            probability = [flop(hand), turn(hand, table[0:3]), river(hand, table[0:4]), 0]

    return probability
    
def flop(hand):
    ranks = {hand[0].get_value(), hand[1].get_value()}
    if len(ranks) == 1:
        flop_pair = 100
    else:
        flop_pair = ((6 * 55 * 4) / 19600) + ((11 * 6 * 2 * 3) / 19600) + ((2 * 6 * 11 * 4) / 19600) + \
                    ((2 * 6 * 3) / 19600) + (2 / 19600) + ((2 * 3 * 55 * 4 * 4) / 19600) + \
                    ((3 * 3 * 55 * 4) / 19600) + (11 * 4 / 19600) #Pair - 1
    return truncate(flop_pair)

def turn(hand, table = 'n/a'):
    if table == 'n/a': #No flop is available yet
        ranks = {hand[0].get_value(), hand[1].get_value()}
        if len(ranks) == 1:
            turn_pair = 100
        else:
            turn_pair = (5 * 3) / 47 #Pair - 2

    else:
        ranks = {hand[0].get_value(), hand[1].get_value(), table[0].get_value(), table[1].get_value(), table[2].get_value()}
        if len(ranks) < 5:
            turn_pair = 100
        else:
            turn_pair = (5 * 3) / 47 #Pair - 3
    return truncate(turn_pair)

def river(hand, table = 'n/a'):
    if table == 'n/a':
        ranks = {hand[0].get_value(), hand[1].get_value()}
        if len(ranks) == 1:
            river_pair = 100
        else:
            river_pair = (6 * 3) / 46  #pair 4

    elif len(table) == 3:
        ranks = {hand[0].get_value(), hand[1].get_value(), table[0].get_value(), table[1].get_value(), table[2].get_value()}
        if len(ranks) < 5:
            river_pair = 100
        else:
           river_pair = (6 * 3) / 46  #pair 5
    else:
        ranks = {hand[0].get_value(), hand[1].get_value(), table[0].get_value(), table[1].get_value(), table[2].get_value(),\
                table[3].get_value()}

        if len(ranks) < 6:
            river_pair = 100
        else:
           river_pair = (6 * 3) / 46  #pair 6
        
    return truncate(river_pair)

def final_check(hand, table):
    ranks = dict({1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0, 12:0, 13:0})
    ranks[hand[0].get_value()] += 1
    ranks[hand[1].get_value()] += 1
    ranks[table[0].get_value()] += 1
    ranks[table[1].get_value()] += 1
    ranks[table[2].get_value()] += 1
    ranks[table[3].get_value()] += 1
    ranks[table[4].get_value()] += 1
    return 100 if process_matches(ranks, 2) >= 1 else 0