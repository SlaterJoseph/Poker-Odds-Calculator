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

def possible_straight_finder_four(hand, table, turn = False):
    """This function checks all possible straight draws and adds them to a counter. If a straight is detected the function
    returns true. If no straight is detected a, every missing num which will complete a straight is added to a set. At the
    end of the function the len of the set is returned, which is the number of missing ranks which would complete a straight
    """
    available_ranks = set() #makes a set to store all ranks, then add all ranks in the hand and table
    available_ranks.add(hand[0].get_value())
    available_ranks.add(hand[1].get_value())
    available_ranks.add(table[0].get_value())
    available_ranks.add(table[1].get_value())
    available_ranks.add(table[2].get_value())
    if turn: available_ranks(table[3].get_value()) #adds the turn

    needed_cards = set() #A set to prevent a card which completes multiple straights form being counted twice
    missing_num = 0 
    for x in range(9): #loops to check all possible straights (1(or Ace)-5 to 10-14(or Ace))
        total_counter = 0
        if x not in available_ranks: continue #no reason to check

        if x in available_ranks:
            if x+1 in available_ranks: total_counter += 1 #If x+1 exists increment counter, else it's a missing
            else: missing_num = x+1
            if x+2 in available_ranks : total_counter += 1 #If x+2 exists increment counter, else it's a missing num
            else: missing_num = x+2
            if x+3 in available_ranks: total_counter += 1 #If x+3 exists increment counter, else it's a missing num
            else: missing_num = x+3
            if x+4 in available_ranks: total_counter += 1 #If x+4 exists increment counter, else it's a missing num
            else: missing_num = x+4
            if x+1 in available_ranks and x+2 in available_ranks and x+3 in available_ranks and x != 1: needed_cards.add(x-1)
            #The line above checks if it's a two way straight (3,4,5,6 can have either 2 or 7 make a straight)
            
        if total_counter == 4: return True #if there is a straight we can return true
        if total_counter == 3: needed_cards.add(missing_num) #if the counter = 3 add the missing num to our set
        missing_num = 0 #reset missing_num

    #This block checks specifically royal straights
    total_counter = 0
    if 10 in available_ranks: total_counter += 1
    else: missing_num = 10
    if 11 in available_ranks: total_counter += 1
    else: missing_num = 11
    if 12 in available_ranks: total_counter += 1
    else: missing_num = 12
    if 13 in available_ranks: total_counter += 1
    else: missing_num = 13
    if 1 in available_ranks: total_counter += 1
    else: missing_num = 1

    if total_counter == 5: return True
    if total_counter == 4: needed_cards.add(missing_num)
        
    return (len(needed_cards))

def possible_straight_finder_threes(hand, table):
    """This function checks all possible straight draws and adds them to a counter. If a straight is detected the function
    returns true. If no straight is detected, every pair of missing nums which will complete a straight is added to a set. Then
    another function is called which checks for duplicates of 3s in 4, then removes them from 3s. Finally the length of 3s and 4s
    is returned"""
    set_4s = possible_straight_finder_four(hand, table) #will be used later to removes duplicates

    available_ranks = set() #makes a set to store all ranks, then add all ranks in the hand and table
    available_ranks.add(hand[0].get_value())
    available_ranks.add(hand[1].get_value())
    available_ranks.add(table[0].get_value())
    available_ranks.add(table[1].get_value())
    available_ranks.add(table[2].get_value())

    #These store the missing cards
    missing_num1 = 0
    missing_num2 = 0 
    needed_cards = set() #Where we put all sets of 2 needed cards

    for x in range(9): #loops to check all possible straights (1(or Ace)-5 to 10-14(or Ace))
        total_counter = 0
        if x not in available_ranks: continue #no reason to check

        if x in available_ranks:
            if x+1 in available_ranks: total_counter += 1 #If x+1 exists increment counter, else it's a missing
            elif missing_num1 == 0: missing_num1 = x+1
            else: missing_num2 = x+1
            if x+2 in available_ranks : total_counter += 1 #If x+2 exists increment counter, else it's a missing num
            elif missing_num1 == 0: missing_num1 = x+2
            else: missing_num2 = x+2
            if x+3 in available_ranks: total_counter += 1 #If x+3 exists increment counter, else it's a missing num
            elif missing_num1 == 0: missing_num1 = x+3
            else: missing_num2 = x+3
            if x+4 in available_ranks: total_counter += 1 #If x+4 exists increment counter, else it's a missing num
            elif missing_num1 == 0: missing_num1 = x+4
            else: missing_num2 = x+4
            if x+1 in available_ranks and x+2 in available_ranks  and x != 1: 
                add_to_set = (x-1, x+3)
                needed_cards.add(frozenset(add_to_set)) #adds a frozen set of x-1 and x+3
            #The line above checks if it's a two way straight (3,4,5,6 can have either 2 or 7 make a straight)
            
        if total_counter == 4: return True #if there is a straight we can return true
        add_to_set = (missing_num1, missing_num2)
        if total_counter == 2: needed_cards.add(frozenset(add_to_set)) 
        #if we our counter is 2, add a frozen set to our set of the missing numbers
        #reset missing nums
        missing_num1 = 0
        missing_num2 = 0 

    #This block checks specifically royal straights
    total_counter = 0
    if 10 in available_ranks: total_counter += 1 
    elif missing_num1 == 0: missing_num1 = 10
    if 11 in available_ranks : total_counter += 1 
    elif missing_num1 == 0: missing_num1 = 11
    else: missing_num2 = 11
    if 12 in available_ranks: total_counter += 1 
    elif missing_num1 == 0: missing_num1 = 12
    else: missing_num2 = 12
    if 13 in available_ranks: total_counter += 1 
    elif missing_num1 == 0: missing_num1 = 13
    else: missing_num2 = 13
    if 1 in available_ranks: total_counter += 1
    elif missing_num1 == 0: missing_num1 = 1
    else: missing_num2 = 1

    if total_counter == 5: return True
    add_to_set = (missing_num1, missing_num2)
    if total_counter == 3: needed_cards.add(frozenset(add_to_set))

    return double_check_straights(set_4s, needed_cards)

def double_check_straights(set_4s, set_3s):
    """This function removes any sets from 3s which would be included in 4s. So if 3s has a set of 
    4:8, but 4s has 8 (so that for example 5:6:7:9 is avialable), then 4:8 is not needed as 8 itself makes a straight"""
    set_3_list = list(set_3s)

    for x in set_3_list:
        card_list = list(set_3_list[x])
        if card_list[0] in set_4s or card_list[1] in set_4s: 
            set_3s.remove(x) #If 1 number in set 3s already makes a straight without a number in set 4s it is not needed

