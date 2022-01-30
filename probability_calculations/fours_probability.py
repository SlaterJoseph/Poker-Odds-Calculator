from probability_helper import truncate

def calculate_fours(hand, table, round):
    if round == 'preflop': #the player has just his hand
        probability = [flop(hand), turn(hand), river(hand), flop(hand) + turn(hand) + river(hand)] 
    elif round == 'flop':
        if turn(hand, table[0:3]) == 100: #checks if the flop contained a four of a kind
            #the only probability now that should not have 100 is the flop, as before the flop happened we were unsure if
            #there would be a four of a kind
            probability = [flop(hand), 100, 100, 100] 

        else:
            probability = [flop(hand), turn(hand, table), river(hand, table), turn(hand, table) + river(hand, table)] 

    elif round == 'turn':
        if turn(hand, table[0:3]) == 100: #checks if the flop contained a four of a kind
            probability = [flop(hand), 100, 100, 100] 

        elif river(hand, table) == 100: #checks if the turn contained a four of a kind
            #similiar logic applies as above, except also including the turn this time
            probability = [flop(hand), turn(hand, table[0:3]), 100, 100] 

        else:
            probability = [flop(hand), turn(hand, table[0:3]), river(hand, table), river(hand, table)] 

    else:
        if turn(hand, table[0:3]) == 100: #checks if the flop contained a four of a kind
            probability = [flop(hand), 100, 100, 100] 

        elif river(hand, table[0:4]) == 100: #checks if the turn contained a four of a kind
            probability = [flop(hand), turn(hand, table[0:3]), 100, 100] 

        elif final_check(hand, table) == 100: #to see if by the end of the game there is a four of a kind
            probability = [flop(hand), turn(hand, table[0:3]), river(hand, table[0:4]), 100]

        else:
            probability = [flop(hand), turn(hand, table[0:3]), river(hand, table[0:4]), 0]

    return probability
    

def flop(hand):
    cards = {hand[0].get_value(), hand[1].get_value()}
    fours_flop = 0
    if len(cards) == 1: #pocket pair
        fours_flop = 48 / 19600 #four of a kind - 1

    else: #unpaired hand
        pass #four of a kind - 2

    return truncate(fours_flop)

def turn(hand, table = 'n/a'):
    fours_flop = 0

    if table == 'n/a': #no community cards known yet
        cards = {hand[0].get_value(), hand[1].get_value()}
        if len(cards) == 1: #pocket pair
            fours_flop = ((2 * 1128) / 19600) * (1 / 47) #four of a kind - 3
    else:
        ranks = dict({1:0 , 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0, 12:0, 13:0}) #a dictionary of all values

    return fours_flop

def river(hand, table = 'n/a'):
    ranks = dict({1:0 , 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0, 12:0, 13:0}) #a dictionary of all values     

    if table == 'n/a':
        pass
    pass

def final_check(hand, table):
    ranks = dict({1:0 , 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0, 12:0, 13:0}) #a dictionary of all values     
    ranks[hand[0].get_value()] += 1 #adding the suits of the cards from the hand
    ranks[hand[1].get_value()] += 1
    ranks[table[0].get_value()] += 1 #adding the suits of the community cards
    ranks[table[1].get_value()] += 1
    ranks[table[2].get_value()] += 1
    ranks[table[3].get_value()] += 1
    ranks[table[4].get_value()] += 1 
    #if any rank is has a counter of 4 there is a four of a kind
    return 100 if (ranks[1] == 4 or ranks[2] == 4 or ranks[3] == 4 or ranks[4] == 4 /
    ranks[5] == 4 or ranks[6] == 4 or ranks[7] == 4 or ranks[8] == 4 or ranks[9] == 4 /
    ranks[10] == 4 or ranks[11] == 4 or ranks[12] == 4 or ranks[13] == 4) else 0 