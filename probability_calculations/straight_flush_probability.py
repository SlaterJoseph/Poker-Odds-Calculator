from probability_helper import truncate, build_flushes, process_flushes, process_flushes_suit
from straight_helper import possible_straight_finder_four
from straight_helper import flop_straights_helper, turn_straight_helper_flopless, river_straight_helper_flopless, \
possible_straight_finder_four, possible_straight_finder_threes, rank_to_set
from sf_helper import straight_flush_4s
from card import Card

def calculate_straight_flush(hand, table, round):
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
    suits = {hand[0].get_suit(), hand[1].get_suit()}
    if len(suits) == 1: #both cards share the same suit
        flop_straight_flush_probability = (flop_straights_helper(hand) * 1 * 1 * 1) / 19600
    else: flop_straight_flush_probability = 0 #cards don't share a suit, making a flush impossible


    return truncate(flop_straight_flush_probability)

def turn(hand, table = 'n/a'):
    if table == 'n/a': #No flop is available yet
        suits = {hand[0].get_suit(), hand[1].get_suit()}
        if len(suits) == 1: #The two cards are of the same suit, so they possibly can make the same straight
            straights = turn_straight_helper_flopless(hand)
            turn_straight_flush_probability = \
                (((straights[0] * 1 * 1 * 47) / 19600) * (1 / 47)) + (((straights[1] * 1 * 1 * 1) / 19600) * (1 / 47))
                #straights[0] holds the number of overlapping straights while straight[1] is the straights which don't overlap
        else:
            total_sfs = len(rank_to_set(hand[0].get_value())) + len(rank_to_set(hand[1].get_value()))

            turn_straight_flush_probability = \
                ((total_sfs * 1 * 1 * 1) / 19600) * (1 / 47)
    else: 
        suits = build_flushes(hand, table, 3)
        if process_flushes(suits, 4) >= 1: #Checks if there is 4 cards of a suit avialable 
            searching_suit = process_flushes_suit(suits, 4)
            hand.extend(table) #Makes hand a list of all cards
            working_cards = set() #A set for all cards with our suit

            for card in hand: #Loops through all cards to add them to the working_cards
                if card.get_suit() == searching_suit: working_cards.add(card) #Adds the cards
                
            workable_cards = straight_flush_4s(working_cards)
            turn_straight_flush_probability = len(workable_cards) / 47
            
        else: #a straight flush is not possible
            turn_straight_flush_probability = 0

    return truncate(turn_straight_flush_probability)

def river(hand, table = 'n/a'):
    if table == 'n/a':
        suits = {hand[0].get_suit(), hand[1].get_suit()}
        if len(suits) == 1:
            straights = river_straight_helper_flopless(hand) #This find all possible straight of the suit using our ranks
            river_straight_flush_probability = (((straights[2] * 47) / 19600) * (46 / 47) * (1 / 46)) \
                + (((straights[2] * 48 * 47) / 19600) * (1 / 47) * (1 / 46)) \
                + ((straights[1] / 19600) * (46 / 47) * (1 / 46)) \
                + ((straights[1] * 46) * (1 / 47) * (1 / 46)) \
                + (((straights[0]) / 19600) * (1 / 47) * (1 / 46)) \
                + ((30 / 19600) * (2 / 47) * (1 / 46))
        else:

    elif len(table) == 3:
      pass  
    else: 
        pass
    return truncate(river_straight_flush_probability)

def final_check(hand, table):
    hand.extend(table)
    for x in hand:
        curr_rank = x.get_value()
        curr_suit = x.get_suit()
        if curr_rank != 10: #checks for everything not a inlcuded in a royal flush
            card1 = Card(curr_rank + 1, curr_suit)
            card2 = Card(curr_rank + 2, curr_suit)
            card3 = Card(curr_rank + 3, curr_suit)
            card4 = Card(curr_rank + 4, curr_suit)
        else: #checks for royal flushes
            card1 = Card(11, curr_suit)
            card2 = Card(12, curr_suit)
            card3 = Card(13, curr_suit)
            card4 = Card(1, curr_suit)
        if card1 in hand and card2 in hand and card3 in hand and card4 in hand: #our straight flush exists
            return 100
        
    return 0