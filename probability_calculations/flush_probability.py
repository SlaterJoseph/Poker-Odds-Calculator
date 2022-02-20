from probability_helper import truncate, process_flushes, build_flushes


def calculate_flush(hand, table, round):
    """This processes the probability of getting a flush

    There are parameters for the player's hand, table's cards and current round. Based on the round, a different if statement 
    contains the proper function calls, passing the right amount of card from the table. The hand is always passed"""
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
    """This function returns the probability of getting a flush on the flop"""
    suits = {hand[0].get_suit(), hand[1].get_suit()}
    if len(suits) == 1: #The hand cards are suited
        flop_flush = 165 / 19600
    else: #If the hand is not suited a flush on the flop is impossible
        flop_flush = 0
    return truncate(flop_flush)

def turn(hand, table = 'n/a'):
    """This function returns the probability of getting a flush on the turn"""
    if table == 'n/a': #No flop is available yet
        suits = {hand[0].get_suit(), hand[1].get_suit()}
        if len(suits) == 1: #The hand cards are suited
            turn_flush = ((55 * 3 * 13) / 19600) * (9 / 47)
        else: #The hand cards are not suited
            turn_flush = ((2 * 66) / 19600) * (9 / 47)
    else:
        suits = build_flushes(hand, table, 3)
        if process_flushes(suits, 4) == 1: #We have 4 cards of 1 suit making a flush possible
            turn_flush = 9 / 47
        else: #If we know the flop and don't have 4 cards of one suit a flush is impossible
            turn_flush = 0
        
    return truncate(turn_flush)

def river(hand, table = 'n/a'):
    """This function returns the probability of getting a flush on the river"""
    if table == 'n/a': #We do not know the flop yet
        suits = {hand[0].get_suit(), hand[1].get_suit()}
        if len(suits) == 1:
            river_flush = (((55 * 39) / 19600) * (38 / 47) * (9 / 46)) \
                + (((11 * 741) / 19600) * (10 / 47) * (9 / 46)) + (((3 * 286) / 19600) * (10 / 47) * (9 / 46))
        else:
            river_flush = (((2 * 220) / 19600) * (39 / 47) * (9 / 46)) \
                + (((2 * 66 * 39) / 19600) * (10 / 47) * (9 / 46)) + (((2 * 286) / 19600) * (10 / 47) * (9 / 46))
            
    elif len(table) == 3: #We have the flop available
        suits = build_flushes(hand, table, 3)
        if process_flushes(suits, 4) >= 1: #We have 4 cards of 1 suit
            river_flush = (38 / 49) * (9 / 46)
        elif process_flushes(suits, 3) >= 1: #We have 3 cards of 1 suit
            river_flush = (10 / 47) * (9 / 46)
        else: #A flush is not possible or already exists
            river_flush = 0 if process_flushes(suits, 5) == 0 else 100
    else: #We have the turn available 
        suits = build_flushes(hand, table, 4)
        if process_flushes(suits, 4) >= 1: #We have 4 cards of 1 suit
            river_flush = 9 / 46
        else: #A flush is not possible or already exists
            river_flush = 0 if process_flushes(suits, 5) == 0 else 100
    return truncate(river_flush)

def final_check(hand, table = 'n/a'):
    """This function checks if by the end of the game there is a flush"""
    suits = build_flushes(hand, table, 5)
    return 100 if process_flushes(suits, 5) >= 1 else 0 
