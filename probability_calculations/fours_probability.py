from probability_helper import truncate, process_matches, build_ranks


def calculate_fours(hand, table, round):
    """This processes the probability of getting four of a kind 

    There are parameters for the player's hand, table's cards and current round. Based on the round, a different if statement 
    contains the proper function calls, passing the right amount of card from the table. The hand is always passed"""
    if round == 'preflop': #Only the hand is available
        probability = [flop(hand), turn(hand), river(hand), flop(hand) + turn(hand) + river(hand)]

    elif round == 'flop': #The hand and 3 table cards are avialable
        if turn(hand, table[0:3]) == 100: #If the probabilty is 100, we found a four of a kind on the flop
            probability = [flop(hand), 100, 100, 100] #no need to check the what the likelyhood is for future rounds

        else: #if there isn't a three of a kind, we pass the table's first 3 cards and the hand to the methods
            probability = [flop(hand), turn(hand, table[0:3]), river(hand, table[0:3]),\
                 turn(hand, table[0:3]) + river(hand, table[0:3])]
    
    elif round == 'turn': #The hand and 4 table cards are available
        if turn(hand, table[0:3]) == 100: #checks if the flop contained fours
            probability = [flop(hand), 100, 100, 100]

        elif river(hand, table[0:4]) == 100:#checks if the turn contained fours
            probability = [flop(hand), turn(hand, table[0:3]), 100, 100]

        else:
            probability = [flop(hand), turn(hand, table[0:3]), river(hand, table[0:4]), river(hand, table[0:4])]

    else: #The hand and all 5 table cards are avialable 
        if turn(hand, table[0:3]) == 100: #checks if the flop contained fours
            probability = [flop(hand), 100, 100, 100] 

        elif river(hand, table[0:4]) == 100: #checks if the turn contained fours
            probability = [flop(hand), turn(hand, table[0:3]), 100, 100] 

        elif final_check(hand, table) == 100: #to see if by the end of the game there is fours
            probability = [flop(hand), turn(hand, table[0:3]), river(hand, table[0:4]), 100]

        else:
            probability = [flop(hand), turn(hand, table[0:3]), river(hand, table[0:4]), 0]

    return probability
    
def flop(hand):
    """This function checks the probability of getting four of a kind specifically on the flop"""
    ranks = {hand[0].get_value(), hand[1].get_value()}
    if len(ranks) == 1: #We have a pokcet pair
        flop_fours = (12 * 4) / 19600
    else: #Our hand did not contain a pocket pair
        flop_fours = (2 * 4) / 19600
    return truncate(flop_fours)

def turn(hand, table = 'n/a'):
    """This function checks the probability of getting four of a kind specifically on the turn"""
    if table == 'n/a': #No flop is available yet
        ranks = {hand[0].get_value(), hand[1].get_value()}
        if len(ranks) == 1: #We have a pokcet pair
            turn_fours  = (((2 * 66 * 4 * 4) / 19600) * (1 / 47)) + (((2 * 12 * 6) / 19600) * (1 / 47)) \
                + (((12 * 4) / 19600) * (1 / 47))
        else: #Our hand did not contain a pocket pair
            turn_fours = (((2 * 3 * 3) / 19600) * ( 1 / 47)) \
                + (((2 * 3 * 11 * 4) / 19600) * (1 / 47)) \
                    + (((11 * 4) / 19600) * (1 / 47))
    else: #We have the flop available 
        ranks = build_ranks(hand, table, 3)
        if process_matches(ranks, 3) >= 1: #This checks if our table contains 3s
            turn_fours = 1 / 47
        else:  #We didn't find threes, making 4s impossible
            turn_fours = 0 if process_matches(ranks, 4) == 0 else 100
    return truncate(turn_fours)

def river(hand, table = 'n/a'):
    """This function checks the probability of getting four of a kind specifically on the river"""
    if table == 'n/a': #No flop is available yet
        ranks = {hand[0].get_value(), hand[1].get_value()}
        if len(ranks) == 1: #We have a pokcet pair
            river_fours = (((2 * 12 * 6) / 19600 * (2 / 27) * (2 / 46)))\
                + (((12 * 4) / 19600) * (2 / 47) * (2 / 46)) \
                + (((2 * 66 * 4 * 4) / 19600) * ((10 * 4) / 47) * (1 / 46)) \
                + (((2 * 12 * 6) / 19600) * ((11 * 4) / 47) * (1 / 46)) \
                + (((2 * 66 * 4 * 4) / 19600) * ((2 * 3) / 47) * (1 / 46)) \
                + (((220 * 4 * 4 * 4) / 19600) * (2 / 47) * (1 / 46)) \
                + (((66 * 2 * 6 * 4) / 19600) * ( 2 / 47) * (1 / 46)) \
                + (((12 * 4) / 19600) * ((11 * 4) / 47) * (1 / 46)) \
                + (((66 * 2 * 6 * 4) / 19600) * (2 / 47) * (1 / 46))
        else: #Our hand did not contain a pocket pair
            river_fours = (((2 * 3 * 3) / 19600) * (2 / 47) * (2 / 46)) \
                + (((2 * 3 * 3) / 19600) * ((11 * 4) / 47) * (1 / 46)) \
                + (((2 * 3 * 11 * 4) / 19600) * ((11 * 4) / 47) * (1 / 46)) \
                + (((3 * 3 * 11 * 4) / 19600) * ((2 * 2) / 47) * (1 / 46)) \
                + (((2 * 3 * 11 * 6) / 19600) * (2 / 47) * (1 / 46)) \
                + (((2 * 3 * 11 * 4) / 19600) * ((10 * 4) / 47) * (1 / 46)) \
                + (((2 * 3 * 11 * 4) / 19600) * (3 / 47) * (1 / 46)) \
                + (((2 * 3 * 55 * 4 * 4) / 19600) * (2 / 47) * (1 / 46)) \
                + (((11 * 4) / 19600) * ((2 * 3) / 47) * (1 / 46)) \
                + (((11 * 4) / 19600) * ((10 * 4) / 47) * (1 / 46)) \
                + (((55 * 2 * 6 * 4) / 19600) * (2 / 47) * (1 / 46)) \
                + (((11 * 6 * 2 * 3) / 19600) * (2 / 47) * (1 / 46)) 

    elif len(table) == 3:
        ranks = build_ranks(hand, table, 3)
        if process_matches(ranks, 3) >= 1 and process_matches(ranks, 2) >= 1: #There is a full house inplay
            river_fours = ((2 / 47) * (2 / 46)) + (((11 * 4) / 47) * (1 / 46))
        elif process_matches(ranks, 3) >= 1: #There is just 3 of a kind (no additonal pair)
            river_fours = (((2 * 3) / 47) * (1 / 46)) + (((10 * 4) / 47) * (1 / 46))
        elif process_matches(ranks, 2) == 2: #There are 2 pairs
            river_fours = ((2 * 2) / 47) * (1 / 46)
        elif process_matches(ranks, 2) == 1: #There is 1 pair
            river_fours = (2 / 47) * (1 / 46)
        else: #There are no pairs b
            river_fours = 0
        
    else: #This is for when the flop and turn are revealed
        ranks = build_ranks(hand, table, 4)
        if process_matches(ranks, 3) == 2: #We have two 3s
            river_fours = 2 / 46
        elif process_matches(ranks, 3) == 1: #We have one 3s
            river_fours = 1 / 46
        else: #Either we have no 3s or we have 4s, making the return 0 or 100
            river_fours = 100 if process_matches(ranks, 4) >= 1 else 0
    return truncate(river_fours)

def final_check(hand, table = 'n/a'):
    """This function checks the probability of getting four of a kind by the end of the game"""
    ranks = build_ranks(hand, table, 5)
    return 100 if process_matches(ranks, 4) >= 1 else 0