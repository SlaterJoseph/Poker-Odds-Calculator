from probability_helper import truncate
from straight_helper import flop_helper

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
    possible_straights = flop_helper(hand) #checks how many possible straights can be amde
    flop_straight = (possible_straights * 4 * 4 * 4) / 19600
    return truncate(flop_straight)

def turn(hand, table = 'n/a'):
    """This function returns the probability of getting a straight on the turn"""
    if table == 'n/a': #No flop is available yet
        
    else:
        
    return truncate(turn_straight)

def river(hand, table = 'n/a'):
    """This function returns the probability of getting a straight on the river"""
    if table == 'n/a':

    elif len(table) == 3:
        
    else:
        
    return truncate(river_straight)

def final_check(hand, table = 'n/a'):
    """This function checks if you have a straight or not"""
    return 100 if process_dictionary(ranks, 3) >= 1 else 0
