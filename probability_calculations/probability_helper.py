import math

def caluclate_probability(n, k): #n!/k!(n-k)! n is the whole pool, k is the number of a item being searched for
    return math.factorial(n)/(math.factorial(k) * math.factorial (n - k))

def truncate(number) -> float: #cuts the number off at 6 decmial spaces
    stepper = 10.0 ** 6
    return math.trunc(stepper * number) / stepper

def process_matches(dictionary, searching_num): #this method checks a dictionary of ranks, and increments a variable 
    #based on how many of those keys values match the searching_num
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

def process_flushes(dictionary, searching_num): #this method checks how many cards of a suit exist, and returns the counter
    checked_value = 0
    if(dictionary['heart'] == searching_num): checked_value += 1
    if(dictionary['spade'] == searching_num): checked_value += 1
    if(dictionary['club'] == searching_num): checked_value += 1
    if(dictionary['diamond'] == searching_num): checked_value += 1
    return checked_value

def process_straights(dictionary, searching_num):#unsure how to do this as of now
    pass

def build_ranks(hand, table, cards_in_play): #This function is to put all the card's ranks into a dictionary
    #It exists to clean up the probability sections involving rank dicitonaries
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