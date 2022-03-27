def straight_flush_4s(cards):
    """This function checks all possible straight draws and adds them to a counter. If a straight is detected the function
    returns true. If no straight is detected a, every missing num which will complete a straight is added to a set. At the
    end of the function the len of the set is returned, which is the number of missing ranks which would complete a straight
    """
    available_ranks = set() #makes a set to store all ranks, then add all ranks in the hand and table
    for x in cards:
        available_ranks.add(x.get_value())

    needed_cards = set() #A set to prevent a card which completes multiple straights form being counted twice
    missing_num = 0 
    for x in range(9): #loops to check all possible straights (1(or Ace)-5 to 9-13(or King))
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
        
    return needed_cards

def straight_flush_3s(cards):
    """This function checks all possible straight draws and adds them to a counter. If a straight is detected the function
    returns true. If no straight is detected a, every missing num which will complete a straight is added to a set. At the
    end of the function the len of the set is returned, which is the number of missing ranks which would complete a straight
    """
    available_ranks = set() #makes a set to store all ranks, then add all ranks in the hand and table
    for x in cards:
        available_ranks.add(x.get_value())

    needed_cards = set() #A set to prevent a card which completes multiple straights form being counted twice
    two_needed_cards = set()
    missing_num = 0
    missing_num_2 = 0
    for x in range(9): #loops to check all possible straights (1(or Ace)-5 to 9-13(or King))
        total_counter = 0
        if x not in available_ranks: continue #no reason to check

        if x in available_ranks:
            if x+1 in available_ranks: total_counter += 1 #If x+1 exists increment counter, else it's a missing
            else: missing_num = x+1
            if x+2 in available_ranks : total_counter += 1 #If x+2 exists increment counter, else it's a missing num
            elif missing_num == 0: missing_num = x+2
            else: missing_num_2 = x+2
            if x+3 in available_ranks: total_counter += 1 #If x+3 exists increment counter, else it's a missing num
            elif missing_num == 0: missing_num = x+3
            else: missing_num_2 = x+3
            if x+4 in available_ranks: total_counter += 1 #If x+4 exists increment counter, else it's a missing num
            elif missing_num == 0: missing_num = x+4
            else: missing_num_2 = x+4
            if x+1 in available_ranks and x+2 in available_ranks and x != 1: needed_cards.add(x-1)
            #The line above checks if it's a two way straight (3,4,5,6 can have either 2 or 7 make a straight)
            
        if total_counter == 4: return True #if there is a straight we can return true
        if total_counter == 3: needed_cards.add(missing_num) #if the counter = 3 add the missing num to our set
        if total_counter == 2: two_needed_cards.add(frozenset(missing_num, missing_num_2))
        missing_num = 0 #reset missing_num
        missing_num_2 = 0 #rest missing_num_2

    total_counter = 0
    missing_num = 0
    missing_num_2 = 0
    if 10 in available_ranks: total_counter += 1
    else: missing_num = 10
    if 11 in available_ranks: total_counter += 1
    elif missing_num == 0: missing_num = 11
    else: missing_num_2 = 11
    if 12 in available_ranks: total_counter += 1
    elif missing_num == 0: missing_num = 12
    else: missing_num_2 = 12
    if 13 in available_ranks: total_counter += 1
    elif missing_num == 0: missing_num = 13
    else: missing_num_2 = 13
    if 1 in available_ranks: total_counter += 1
    elif missing_num == 0: missing_num = 1
    else: missing_num_2 = 1

    if total_counter == 5: return True
    if total_counter == 4: needed_cards.add(missing_num)
    if total_counter == 3: two_needed_cards.add(frozenset(missing_num, missing_num_2))
        
    return (needed_cards, two_needed_cards)