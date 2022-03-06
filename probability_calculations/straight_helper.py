from all_straight_for_card import set_return

def flop_straights_helper(hand):
    """This takes a hand and returns the intersection of all possible straights of those cards. Only straights missing 3
    cards can be obtained on the flop"""
    card_1_sets = set_return(hand[0].get_value())
    card_2_sets = set_return(hand[1].get_value())
    #The interesection of the possible straights are all the straights in common between the two hand cards
    #and only straights involving both hand cards are possible in the flop
    all_possible_straights = set.intersection(card_1_sets, card_2_sets)
    return len(all_possible_straights)

def turn_straight_helper_flopless(hand):
    """This takes a hand and checks intersections and union of all possible straights. Intersection requires 3 cards while union
    requires 4. A tuple is returned which has a 0 index of union - intersection (which is all straights which require 4 cards)
    and the 1st index is the intersections (or straights which require 3 cards)"""
    card_1_sets = set_return(hand[0].get_value())
    card_2_sets = set_return(hand[1].get_value())
    #All possible straights involve one of the hand cards, so all straights of the union are possible  
    all_straights = set.union(card_1_sets, card_2_sets)
    #All easier starights are composed of both hand cards, so all straights of the intersection are easier
    simple_straights = set.intersection(card_1_sets, card_2_sets) 
    #subtract easier straights from all straights to find the medium straights
    return (len(all_straights) - len(simple_straights), len(simple_straights))

def river_straight_helper_flopless(hand):
    """This function takes a hand and checks the intersection and union of all overlapping straights. There are 10 possible
    straights. We find easy (or 3 card straights) with the intersection of the two hand ranks. We find medium (or 4 card straights)
    with the union - intersection of all possible straights. We find the hard straights (straights where we need all 5 cards to
    come onto the table) by doing 10 - union"""
    card_1_sets = set_return(hand[0].get_value())
    card_2_sets = set_return(hand[1].get_value())
    #All straight are possible right now, so we must firgure out the easy, medium, and hard straights to obtain
    all_straights = set.union(card_1_sets, card_2_sets)
    simple_straights = set.intersection(card_1_sets, card_2_sets)
    return [10 - len(all_straights), len(all_straights) - len(simple_straights), len(simple_straights)]

def possible_straight_finder(hand, table, turn = False):
    """This function checks all possible straight draws and adds them to a counter. If a straight is detected the function
    returns true. If no straight is detected a tuple with straight draws as index 0 and 3 cards to straight is returns
    with index of 1"""
    available_ranks = set #makes a set to store all ranks, then add all ranks in the hand and table
    available_ranks.add(hand[0].get_value())
    available_ranks.add(hand[1].get_value())
    available_ranks.add(table[0].get_value())
    available_ranks.add(table[1].get_value())
    available_ranks.add(table[2].get_value())
    if turn: available_ranks(table[3].get_value()) #adds the turn

    counter_4 = 0
    counter_3 = 0
    for x in range(10): #loops to check all possible straights (1(or Ace)-5 to 10-14(or Ace))
        total_counter_up = 0
        if x not in available_ranks: continue #no reason to check

        if x in available_ranks:
            if x+1 in available_ranks: total_counter_up += 1
            if x+2 in available_ranks : total_counter_up += 1
            if x+3 in available_ranks: total_counter_up += 1
            if x+4 in available_ranks: total_counter_up += 1
            if x+1 in available_ranks and x+2 in available_ranks and x+3 in available_ranks and x != 1: counter_4 += 1
            #The line above checks if it's a two way straight (3,4,5,6 can have either 2 or 7 make a straight)
            if x == 10 and 1 in available_ranks: total_counter += 1 #checks specifically 10 - Ace
        
        if total_counter_up == 5: return True #if there is a straight we can return true
        if total_counter_up == 3: counter_4 += 1
        if total_counter_up == 2: counter_3 += 1

    return (counter_4, counter_3)