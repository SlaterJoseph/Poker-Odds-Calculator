from probability_helper import truncate, check_straight
from straight_helper import flop_straights_helper, turn_straight_helper_flopless, river_straight_helper_flopless, \
    possible_straight_finder_four, possible_straight_finder_threes

def calculate_straight(hand, table, round):
    """This processes the probability of getting a straight

    There are parameters for the player's hand, table's cards and current round. Based on the round, a different if statement 
    contains the proper function calls, passing the right amount of card from the table. The hand is always passed"""
    if round == 'preflop':
        probability = [flop(hand), turn(hand), river(hand), flop(hand) + turn(hand) + river(hand)]

    elif round == 'flop':
        if turn(hand, table[0:3]) == 100: #If the probabilty is 100, we found a straight on the flop
            probability = [flop(hand), 100, 100, 100] #no need to check the what the likelyhood is for future rounds

        else: #if there isn't a straight, we pass the table's first 3 cards and the hand to the methods
            probability = [flop(hand), turn(hand, table[0:3]), river(hand, table[0:3]),\
                 turn(hand, table[0:3]) + river(hand, table[0:3])]
    
    elif round == 'turn':
        if turn(hand, table[0:3]) == 100: #checks if the flop contained a straight
            probability = [flop(hand), 100, 100, 100]

        elif river(hand, table[0:4]) == 100:#checks if the turn contained a straight
            probability = [flop(hand), turn(hand, table[0:3]), 100, 100]

        else:
            probability = [flop(hand), turn(hand, table[0:3]), river(hand, table[0:4]), river(hand, table[0:4])]

    else:
        if turn(hand, table[0:3]) == 100: #checks if the flop contained a straight
            probability = [flop(hand), 100, 100, 100] 

        elif river(hand, table[0:4]) == 100: #checks if the turn contained a straight
            probability = [flop(hand), turn(hand, table[0:3]), 100, 100] 

        elif final_check(hand, table) == 100: #to see if by the end of the game there is a straight
            probability = [flop(hand), turn(hand, table[0:3]), river(hand, table[0:4]), 100]

        else:
            probability = [flop(hand), turn(hand, table[0:3]), river(hand, table[0:4]), 0]

    return probability
    
def flop(hand):
    """This function returns the probability of getting a straight on the flop"""
    flop_straight = (flop_straights_helper(hand) * 4 * 4 * 4) / 19600
    return truncate(flop_straight) 

def turn(hand, table = 'n/a'):
    """This function returns the probability of getting a straight on the turn"""
    if table == 'n/a': #No flop is available yet
        straights = turn_straight_helper_flopless(hand)
        turn_straight = (((straights[0] * 4 * 4 * 44) / 19600) * (4 / 47)) + (((straights[1] * 4 * 4 * 4) / 19600) * ( 4 / 47))
    else: #flop is avaliable
        if possible_straight_finder_four(hand, table) == True: return 100
        all_straights = len(possible_straight_finder_four(hand, table))
        turn_straight = (all_straights * 4) / 47 
    return truncate(turn_straight)

def river(hand, table = 'n/a'):
    """This function returns the probability of getting a straight on the river"""
    if table == 'n/a': #no flop avialable
        straights = river_straight_helper_flopless(hand)
        river_straight = (((straights[2] * 4 * 4 * 44) / 19600) * (43 / 47) * (4 / 46))  \
            + (((straights[2] * 4 * 44 * 43) / 19600) * (4 / 47) * (4 / 46)) \
            + (((straights[1] * 4 * 4 * 4) / 19600) * (43 / 47) * (4 / 46)) \
            + (((straights[1] * 4 * 4 * 40) / 19600) * (4 / 47) * (4 / 46)) \
            + (((straights[0] * 4 * 4 * 4) / 19600) * (4 / 47) * (4 / 46))
    elif len(table) == 3: #flop available
        if possible_straight_finder_threes(hand, table) == True: return 100 #checks if we found a straight
        all_straights = possible_straight_finder_threes(hand, table)
        river_straight = 0 
        if len(all_straights[1]) != 0: river_straight += ((len(all_straights[1]) * 4) / 47) * (4 / 46)
        if len(all_straights[0]) != 0: river_straight += ((47 - (len(all_straights[0]) * 4)) / 47) \
            * ((len(all_straights[0]) * 4) / 46)
        

    else: #turn available
        if possible_straight_finder_four(hand, table, True) == True: return 100 #checks if we found a straight
        all_straights = len(possible_straight_finder_four(hand, table, True))
        river_straight = (all_straights * 4) / 46
    return truncate(river_straight)

def final_check(hand, table):
    """This function checks if you have a straight or not"""
    return check_straight(hand, table)
