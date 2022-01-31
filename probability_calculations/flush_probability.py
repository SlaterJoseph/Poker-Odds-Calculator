from probability_helper import truncate

def calculate_flush(hand, table, round): #a list of all the probabilities is returned 
    if round == 'preflop': #the player has just his hand
        probability = [flop(hand), turn(hand), river(hand), flop(hand) + turn(hand) + river(hand)] 
    elif round == 'flop':
        if turn(hand, table) == 100: #checks if the flop contained a flush
            #the only probability now that should not have 100 is the flop, as before the flop happened we were unsure if
            #there would be a flush
            probability = [flop(hand), 100, 100, 100] 

        else:
            probability = [flop(hand), turn(hand, table[0:3]), river(hand, table[0:4]), \
            turn(hand, table[0:3]) + river(hand, table[0:4])] 

    elif round == 'turn':
        if turn(hand, table[0:3]) == 100: #checks if the flop contained a flush
            probability = [flop(hand), 100, 100, 100] 

        elif river(hand, table) == 100: #checks if the turn contained a flush
            #similiar logic applies as above, except also including the turn this time
            probability = [flop(hand), turn(hand, table[0:3]), 100, 100] 

        else:
            probability = [flop(hand), turn(hand, table[0:3]), river(hand, table[0:4]), river(hand, table[0:4])] 

    else:
        if turn(hand, table[0:3]) == 100: #checks if the flop contained a flush
            probability = [flop(hand), 100, 100, 100] 

        elif river(hand, table[0:4]) == 100: #checks if the turn contained a flush
            probability = [flop(hand), turn(hand, table[0:3]), 100, 100] 

        elif final_check(hand, table) == 100: #to see if by the end of the game there is a flush
            probability = [flop(hand), turn(hand, table[0:3]), river(hand, table[0:4]), 100]

        else:
            probability = [flop(hand), turn(hand, table[0:3]), river(hand, table[0:4]), 0]

    return probability


def flop(hand): #Checks the probability for the flop
    suits = {hand[0].get_suit(), hand[1].get_suit()} #a set of the suits
    if(len(suits) == 1): #the hand has to be suited(matching suits)
        return truncate(165 / 19600) #Flush - 1

    else: #if the hand is not of matching suit there cannot be a flush on the flop
        return 0

def turn(hand, table = 'n/a'): #Checks the probability for the turn
    flush_turn = 0
    suits = {'heart' : 0, 'spade' : 0, 'diamond' : 0, 'club' : 0} #a dictionary of the suits in the hand
    suits[hand[0].get_suit()] += 1 #adding the suits of the cards from the hand
    suits[hand[1].get_suit()] += 1
    if table == 'n/a': #no community cards are avialable yet

        if suits['heart'] == 2 or suits['club'] == 2 or suits['spade'] == 2 or suits['diamond'] == 2: #suited hand 
            flush_turn = ((55 * 3 * 13) / 19600) * (9 / 47) #Flush - 2

        else: #unsuited hand
            flush_turn = ((2 * 220) / 19600) * (9 / 47) #Flush - 3

    else: #community cards avialable
        suits[table[0].get_suit()] += 1 #adding the suits of the community cards
        suits[table[1].get_suit()] += 1
        suits[table[2].get_suit()] += 1
        #one of the suits has 5, so there is a flush
        if suits['heart'] == 5 or suits['club'] == 5 or suits['spade'] == 5 or suits['diamond'] == 5: 
            return 100
        #on of the suits has 4, so there is a flush draw
        elif suits['heart'] == 4 or suits['club'] == 4 or suits['spade'] == 4 or suits['diamond'] == 4:
            flush_turn = 9 / 47 #Flush - 4

        else: #no flush is possible on the turn
            return 0

    return truncate(flush_turn) #if we get over 100, it means there is a flush somewhere

def river(hand, table = 'n/a'): #Checks the probability for the river
    flush_river = 0
    suits = {'heart' : 0, 'spade' : 0, 'diamond' : 0, 'club' : 0} #a dictionary of the suits in the hand
    suits[hand[0].get_suit()] += 1 #adding the suits of the cards from the hand
    suits[hand[1].get_suit()] += 1
    if table == 'n/a':
        if suits['heart'] == 2 or suits['club'] == 2 or suits['spade'] == 2 or suits['diamond'] == 2: #suited hand 
            flush_river = ((55 + 39) / 19600) * (38 / 47) * (9 / 46) #Flush - 5
            flush_river += ((11 * 741) / 19600) * (10 / 47) * (9 / 46)

        else: #unsuited hand
            flush_river = ((2 * 220) / 19600) * (38 / 47) * (9 / 46) #Flush - 6
            flush_river += ((2 * 66 * 38) / 19600) * (10 / 48) * (9 / 46)

    elif len(table) == 3: #flop cards avialable
        suits[table[0].get_suit()] += 1 #adding the suits of the community cards
        suits[table[1].get_suit()] += 1
        suits[table[2].get_suit()] += 1
        #one of the suits has 5, so there is a flush
        if suits['heart'] == 5 or suits['club'] == 5 or suits['spade'] == 5 or suits['diamond'] == 5: 
            return 100

        #one of the suits has 4, so there is a flush draw, and we do not want the turn to be the flush
        elif suits['heart'] == 4 or suits['club'] == 4 or suits['spade'] == 4 or suits['diamond'] == 4: 
            flush_river = (38 / 47) * (9 / 46) #Flush - 7

        #one of the suits has 3, so we need both the turn and river to be of the same suit
        elif suits['heart'] == 3 or suits['club'] == 3 or suits['spade'] == 3 or suits['diamond'] == 3: 
            flush_river = (10 / 47) * (9 / 46) #Flush - 8

        else: #a flush is no longer possible
            return 0

        return truncate(flush_river)

    else: #flop and turn avialable
        suits[table[0].get_suit()] += 1 #adding the suits of the community cards
        suits[table[1].get_suit()] += 1
        suits[table[2].get_suit()] += 1
        suits[table[3].get_suit()] += 1
        #one of the suits has 5, so there is a flush
        if suits['heart'] == 5 or suits['club'] == 5 or suits['spade'] == 5 or suits['diamond'] == 5: 
            return 100

        #one of the suits has 4, so there is a flush draw
        elif suits['heart'] == 4 or suits['club'] == 4 or suits['spade'] == 4 or suits['diamond'] == 4: 
            flush_river = (9 / 46) #Flush - 9
            
    return truncate(flush_river)

def final_check(hand, table): #Checks the probability at the end of the round
    suits = {'heart' : 0, 'spade' : 0, 'diamond' : 0, 'club' : 0} #a dictionary of the suits in the hand
    suits[hand[0].get_suit()] += 1 #adding the suits of the cards from the hand
    suits[hand[1].get_suit()] += 1
    suits[table[0].get_suit()] += 1 #adding the suits of the community cards
    suits[table[1].get_suit()] += 1
    suits[table[2].get_suit()] += 1
    suits[table[3].get_suit()] += 1
    suits[table[4].get_suit()] += 1
    #if any of the suits have 5 return 100, otherwise return 0
    return 100 if suits['heart'] == 5 or suits['club'] == 5 or suits['spade'] == 5 or suits['diamond'] == 5 else 0 
