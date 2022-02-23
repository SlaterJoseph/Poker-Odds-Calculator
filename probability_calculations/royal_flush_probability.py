from probability_helper import truncate, royal_helper


def calculate_royal_flush(hand, table, round):
    """This processes the probability of getting a royal flush

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
    """This function returns the probability of getting a royal flush on the flop"""
    royal = royal_helper(hand, 'n/a', 0)
    if 2 in royal.values(): #Our hand contains 1 suit and 2 royal ranks
        flop_royal_flush = 1 / 19600
    else: #A royal flush is not possible
        flop_royal_flush = 0
    return truncate(flop_royal_flush)

def turn(hand, table = 'n/a'):
    """This function returns the probability of getting a royal flush on the turn"""
    if table == 'n/a': #No flop is available yet
        royal = royal_helper(hand, 'n/a', 0) #makes a dictionary of suits and royal ranks (key then value)
        if 2 in royal.values(): #Our hand contains 1 suit and 2 royal ranks
            turn_royal_flush = ((3 * 47) / 19600) * (1 / 47)
        #the if statement below checks if 2 different suits have a royal card
        if (royal['heart'] == 1 and royal['diamond'] == 1) or (royal['heart'] == 1 and royal['club'] == 1) \
           or (royal['heart'] == 1 and royal['spade'] == 1) or (royal['spade'] == 1 and royal['diamond'] == 1) \
           or (royal['spade'] == 1 and royal['club'] == 1) or (royal['club'] == 1 and royal['diamond'] == 1):
            turn_royal_flush = ((2 * 4) / 19600) * (1 / 47)
        elif 1 in royal.values(): #checks if the player has 1 royal card
            turn_royal_flush = (4 / 19600) * (1 / 47)
        else: #a royal flush is not possible
            turn_royal_flush = 100 if 5 in royal.values() else 0

    else: #flop is avialable 
        royal = royal_helper(hand, table, 3) #makes a dictionary of suits and royal ranks (key then value)
        if 4 in royal.values(): #We have 4 royal cards of 1 suit
            turn_royal_flush = 1 / 47
        else: #A royal flush is not possible
            turn_royal_flush = 100 if 5 in royal.values() else 0
        
    return truncate(turn_royal_flush)

def river(hand, table = 'n/a'):
    """This function returns the probability of getting a royal flush on the river"""
    if table == 'n/a':
        royal = royal_helper(hand, 'n/a', 0) #makes a dictionary of suits and royal ranks (key then value)
        if 2 in royal.values(): #Our hand contains 1 suit and 2 royal ranks
            river_royal_flush = (((3 * 47) / 19600) * (46 / 47)  * (1 / 46))\
                + (((3 * 1081) / 19600) * (2 / 47) * (1 / 46)) \
                + (((3 * 10) / 19600) * (2 / 47) * (1 / 46))
        #the if statement below checks if 2 different suits have a royal card
        if (royal['heart'] == 1 and royal['diamond'] == 1) or (royal['heart'] == 1 and royal['club'] == 1) \
           or (royal['heart'] == 1 and royal['spade'] == 1) or (royal['spade'] == 1 and royal['diamond'] == 1) \
           or (royal['spade'] == 1 and royal['club'] == 1) or (royal['club'] == 1 and royal['diamond'] == 1):
            river_royal_flush = (((2 * 4) / 19600) * (46 / 47)  * (1 / 46))\
                + (((2 * 6 * 47) / 19600) * (2 / 47) * (1 / 46)) + (((2 * 10) / 19600) * (2 / 47) * (1 / 46))
        elif 1 in royal.values(): #checks if the player has 1 royal card
            river_royal_flush = ((4 / 19600) * (47 / 47)  * (1 / 46))\
                + (((6 * 47) / 19600) * (2 / 47) * (1 / 46)) + (((2 * 10) / 19600) * (2 / 47) * (1 / 46))
        else: #a royal flush is not possible
            river_royal_flush = ((4 * 10) / 19600) * (2 / 47) * (1 / 46)

    elif len(table) == 3: #The flop is avialable 
        royal = royal_helper(hand, table, 3) #makes a dictionary of suits and royal ranks (key then value)
        if 4 in royal.values(): #There are 4 royal ranks of 1 suit
            river_royal_flush = (46 / 47) * (1 / 46)
        elif 3 in royal.values(): #There are 3 royal ranks of 1 suit
            river_royal_flush = (2 / 47) * (1 / 46)
        else: #There either is a royal flush or there cannot be one
            river_royal_flush = 100 if 5 in royal.values() else 0
    else: #The turn is avialable
        royal = royal_helper(hand, table, 4) #makes a dictionary of suits and royal ranks (key then value)
        if 4 in royal.values(): #There are 4 royal ranks of 1 suit
            river_royal_flush = 1 / 46
        else: #There is either a royal flush or there cannot be one
            river_royal_flush = 100 if 5 in royal.values() else 0
        
    return truncate(river_royal_flush)

def final_check(hand, table):
    """This function checks if by the end of the round if there is a royal flush"""
    return 100 if 5 in royal_helper(hand, table, 5).values() else 0