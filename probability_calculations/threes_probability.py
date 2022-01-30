from probability_helper import truncate

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

        if turn(hand, table[0:3]) == 100:
            probability = [flop(hand), 100, 100, 100]

        elif river(hand, table[0:4]) == 100:
            probability = [flop(hand), turn(hand, table[0:3]), 100, 100]

        else:
            probabiltiy = [flop(hand), turn(hand, table[0:3]), river(hand, table[0:4]), river]






    return probability

    

def flop(hand):
    return 1

def turn(hand, table = 'n/a'):
    return 1

def river(hand, table = 'n/a'):
    return 1

def final_check(hand, table = 'n/a'):
    return 1
