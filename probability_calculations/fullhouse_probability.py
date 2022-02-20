from probability_helper import truncate, process_matches, build_ranks

def calculate_full_house(hand, table, round):
    """This processes the probability of getting a full house

    There are parameters for the player's hand, table's cards and current round. Based on the round, a different if statement 
    contains the proper function calls, passing the right amount of card from the table. The hand is always passed"""
    if round == 'preflop':
        probability = [flop(hand), turn(hand), river(hand), flop(hand) + turn(hand) + river(hand)]

    elif round == 'flop':
        if turn(hand, table[0:3]) == 100: #If the probabilty is 100, we found a full house
            probability = [flop(hand), 100, 100, 100] #no need to check the what the likelyhood is for future rounds
        else: #if there a full house, we pass the table's first 3 cards and the hand to the methods
            probability = [flop(hand), turn(hand, table[0:3]), river(hand, table[0:3]),\
                 turn(hand, table[0:3]) + river(hand, table[0:3])]
    
    elif round == 'turn':
        if turn(hand, table[0:3]) == 100: #checks if the flop contained a full house
            probability = [flop(hand), 100, 100, 100]
        elif river(hand, table[0:4]) == 100:#checks if the turn contained a full house
            probability = [flop(hand), turn(hand, table[0:3]), 100, 100]
        else:
            probability = [flop(hand), turn(hand, table[0:3]), river(hand, table[0:4]), river(hand, table[0:4])]

    else:
        if turn(hand, table[0:3]) == 100: #checks if the flop contained a full house
            probability = [flop(hand), 100, 100, 100] 
        elif river(hand, table[0:4]) == 100: #checks if the turn contained a full house
            probability = [flop(hand), turn(hand, table[0:3]), 100, 100] 
        elif final_check(hand, table) == 100: #to see if by the end of the game there is a full house
            probability = [flop(hand), turn(hand, table[0:3]), river(hand, table[0:4]), 100]
        else:
            probability = [flop(hand), turn(hand, table[0:3]), river(hand, table[0:4]), 0]

    return probability
    
def flop(hand):
    """This function returns the probability of getting a full house on the flop"""
    ranks = {hand[0].get_value(), hand[1].get_value()} #A set to see if the cards are the same rank
    if len(ranks) == 1: #You have a pocket pair
        flop_full_house = ((2 * 12 * 6) / 19600) + ((12 * 4) / 19600) 
    else: #You don't have a pocket pair
        flop_full_house = (2 * 6 * 4) / 19600
    return truncate(flop_full_house)

def turn(hand, table = 'n/a'):
    """This function returns the probability of getting a full house on the turn"""
    if table == 'n/a': #No flop is available yet
        ranks = {hand[0].get_value(), hand[1].get_value()} #A set to see if the hand is a pokcet pair
        if len(ranks) == 1: #The hand is a pocket pair
            turn_full_house = (((2 * 66 * 4 * 4) / 19600) * (3 / 47)) \
                + (((66 * 2 * 6 * 4) / 19600) * ((2 * 3) / 47))
        else: #The hand is not a pocket pair
            turn_full_house = (((2 * 3 * 11 * 4) / 19600) * ((2 * 3) / 47)) \
                + (((3 * 3 * 11 * 4) / 19600) * ((2 * 2) / 47)) \
                + (((11 * 4) / 19600)* ((2 * 3) / 47))

    else: #The flop has been revealed
        ranks = build_ranks(hand, table, 3) #Builds the ranks dictionary with the 3 flop cards
        if process_matches(ranks, 3) == 1 and process_matches(ranks, 2) == 1: #If we have 3s and a pair we have a full house
            turn_full_house = 100
        elif process_matches(ranks, 3) == 1: #We have just 3s
            turn_full_house = ((2 * 3) / 47)
        elif process_matches(ranks, 2) == 2: #We have just 2 pairs
            turn_full_house = (2 * 2) / 47
        else: #We have 1 pairs or no pairs, either way a full house is impossible
            turn_full_house = 0
        
    return truncate(turn_full_house)

def river(hand, table = 'n/a'):
    """This function returns the probability of getting a full house on the river"""
    if table == 'n/a': #No flop is available yet
        ranks = {hand[0].get_value(), hand[1].get_value()} #A set to see if the hand is a pokcet pair
        if len(ranks) == 1: #The hand is a pocket pair
            river_full_house = (((2 * 66 * 4 * 4) / 19600) * ((10 * 4) / 47) * ((3 * 3) / 46)) \
                + (((66 * 2 * 6 * 4) / 19600) * (3 / 47) * ((3 * 2) / 46)) \
                + (((220 * 4 * 4 * 4) / 19600) * (2 / 47) * ((3 * 3) / 46)) \
                + (((66 * 2 * 6 * 4) / 19600) * ((10 * 4) / 47) * ((2 * 2) / 46)) \
                + (((220 * 4 * 4 * 4) / 19600) * ((3 * 3) / 47) * ((2 * 2) / 46)) \
                + (((12 * 4) / 19600) * ((11 * 4) / 47) * ((2 * 3) / 46)) + (((2 * 66 * 4 * 4) / 19600) * (1 / 47) * ((2 * 3) / 46)) 
        else: #The hand is not a pocket pair
            river_full_house = (((2 * 3 * 11 * 4) / 19600) * ((10 * 32 / 47) * ((3 * 3) / 46))) \
                + (((2 * 3 * 66 * 4 * 4) / 19600) * (2 / 47) * ((3 * 3) / 46)) + (((11 * 4) / 19600) * ((10 * 4) / 47) * ((3 * 3) / 46)) \
                + (((55 * 2 * 6 * 4) / 19600) * ((2 * 3) / 47) * ((2 * 2) / 46)) + ((2 / 19600) * ((11 * 4) / 47) * ((2 * 3) / 46)) \
                + (((2 * 3 * 11 * 4) / 19600) * (2 / 47) * ((2 * 3) / 46)) + (((3 * 3 * 11 * 4) / 19600) * (3 / 47) * ((3 * 2) / 46)) \
                + (((2 * 3 * 11 * 6) / 19600) * (3 / 47) * ((3 * 2) / 46)) + (((11 * 4) / 19600) * (1 / 47) * ((2 * 3) / 46)) \
                + (((55 * 2 * 6 * 4) / 19600) * (2 / 47) * ((3 * 3) / 46)) + (((2 * 3 * 55 * 4 * 4) / 19600) * ((2 * 3) / 47) * ((2 * 2) / 46)) \
                + (((11 * 6 * 2 * 3) / 19600) * ((10 * 4) / 47) * ((2 * 2) / 46)) 

    elif len(table) == 3: #Flop is available, turn is not
        ranks = build_ranks(hand, table, 3) #Builds the ranks dictionary with the 3 flop cards
        if process_matches(ranks, 3) == 1 and process_matches(ranks, 2) == 1: #If we have 3s and a pair we have a full house
            river_full_house = 100
        elif process_matches(ranks, 4) == 1:
            river_full_house = ((11 * 4) / 47) * ((2 * 3) / 46)
        elif process_matches(ranks, 3) == 1: #We have just 3s
            river_full_house = ((10 * 4) / 47) * ((3 * 3) / 46)
        elif process_matches(ranks, 2) == 2: #We have just 2 pairs
            river_full_house = ((3 / 47) * ((3 * 2) / 46)) + ((2 / 47) * ((3 * 3) / 46))
        elif process_matches(ranks, 2) == 1: #We have 1 pairs 
            river_full_house = ((2 / 47) * ((3 * 3) / 46)) + (((3 * 3) / 47) * ((2 * 2) / 46))
        else:
            river_full_house = 0


    else: #Both flop and turn are avialable 
        ranks = build_ranks(hand, table, 4) #Builds the ranks dictionary with the 3 flop cards
        if process_matches(ranks, 3) >= 1 and process_matches(ranks, 2) >= 1:
            river_full_house = 100
        elif process_matches(ranks, 3) == 1: #We have a three of a kind
            river_full_house = (3 * 3) / 46
        elif process_matches(ranks, 4) == 1: #We have 4 of a kind
            river_full_house = (2 * 3) / 46
        elif process_matches(ranks, 2) == 3: #We have 3 pairs
            river_full_house = (3 * 2) / 46
        elif process_matches(ranks, 2) == 2: #We have 2 pairs
            river_full_house = (2 * 2) / 46
        else: #We cannot get a full house
            river_full_house = 0
    return truncate(river_full_house)

def final_check(hand, table = 'n/a'):
    """This is used once at the end to see if we have a full house"""
    ranks = build_ranks(hand, table, 5)
    return 100 if process_matches(ranks, 2) >= 1 and process_matches(ranks, 3) >= 1 else 0