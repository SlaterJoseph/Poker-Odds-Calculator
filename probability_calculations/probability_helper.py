import math

def truncate(number) -> float:
    """This function shortens floats to 6 decimal spaces"""
    stepper = 10.0 ** 6
    return math.trunc(stepper * number) / stepper

def process_matches(dictionary, searching_num):
    """This function takes a dictionary and a number to search for, and if the number is found a counter is incremented.
    The counter is then returned after checking all the ranks (1-13)"""
    checked_value = 0
    if(dictionary[1] == searching_num): checked_value += 1
    if(dictionary[2] == searching_num): checked_value += 1
    if(dictionary[3] == searching_num): checked_value += 1
    if(dictionary[4] == searching_num): checked_value += 1
    if(dictionary[5] == searching_num): checked_value += 1
    if(dictionary[6] == searching_num): checked_value += 1
    if(dictionary[7] == searching_num): checked_value += 1
    if(dictionary[8] == searching_num): checked_value += 1
    if(dictionary[9] == searching_num): checked_value += 1
    if(dictionary[10] == searching_num): checked_value += 1
    if(dictionary[11] == searching_num): checked_value += 1
    if(dictionary[12] == searching_num): checked_value += 1
    if(dictionary[13] == searching_num): checked_value += 1
    return checked_value

def process_flushes(dictionary, searching_num):
    """This function takes a dictionary of suits, and searches for a specific value (both parameters). If the value is found,
    a counter is incremented, and once all suits are checked the counter is returned"""
    checked_value = 0
    if(dictionary['heart'] == searching_num): checked_value += 1
    if(dictionary['spade'] == searching_num): checked_value += 1
    if(dictionary['club'] == searching_num): checked_value += 1
    if(dictionary['diamond'] == searching_num): checked_value += 1
    return checked_value

def process_straights(dictionary, searching_num):#unsure how to do this as of now
    pass

def build_ranks(hand, table, cards_in_play):
    """This function builds a dictionary of ranks. It takes in all the cards in play, and then increments the value associated
    with the key. Finally, once all the cards area added the dictionary is returned"""
    ranks = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0, 12:0, 13:0}
    ranks[hand[0].get_value()] += 1
    ranks[hand[1].get_value()] += 1

    if(cards_in_play == 3):
        ranks[table[0].get_value()] += 1
        ranks[table[1].get_value()] += 1
        ranks[table[2].get_value()] += 1
    elif(cards_in_play == 4):
        ranks[table[0].get_value()] += 1
        ranks[table[1].get_value()] += 1
        ranks[table[2].get_value()] += 1
        ranks[table[3].get_value()] += 1
    else:
        ranks[table[0].get_value()] += 1
        ranks[table[1].get_value()] += 1
        ranks[table[2].get_value()] += 1
        ranks[table[3].get_value()] += 1
        ranks[table[4].get_value()] += 1

    return ranks

def build_flushes(hand, table, cards_in_play):
    """This function builds a dictionary of suits. It takes in all the cards in play, and then increments the value associated
    with the key. Finally, once all the cards area added the dictionary is returned"""
    ranks = {'heart':0, 'spade':0, 'diamond':0, 'club':0}
    ranks[hand[0].get_suit()] += 1
    ranks[hand[1].get_suit()] += 1

    if(cards_in_play == 3):
        ranks[table[0].get_suit()] += 1
        ranks[table[1].get_suit()] += 1
        ranks[table[2].get_suit()] += 1
    elif(cards_in_play == 4):
        ranks[table[0].get_suit()] += 1
        ranks[table[1].get_suit()] += 1
        ranks[table[2].get_suit()] += 1
        ranks[table[3].get_suit()] += 1
    else:
        ranks[table[0].get_suit()] += 1
        ranks[table[1].get_suit()] += 1
        ranks[table[2].get_suit()] += 1
        ranks[table[3].get_suit()] += 1
        ranks[table[4].get_suit()] += 1