def find_easy_straights(hand):
    """This function checks for how many overlapping straights the 2 cards have regardless of position(So A,2 has the
    amount as 6,7)"""
    hand_values = [hand[0].get_value(), hand[1].get_value()]
    easier_straights = abs(hand_values[0] - hand_values[1])
    if easier_straights == 0: #The hand contains a pair and a straight is not possible
        easier_straights = 0
    elif easier_straights == 1: #The distance of the cards is 1 (ex. 5,6) and 4 straights are possible max
        easier_straights = 4
    elif easier_straights == 2: #The distance of the cards is 2 (ex. 5,7) and 3 straights are possible max
        easier_straights = 3
    elif easier_straights == 3: #The distance of the cards is 3 (ex. 5,8) and 2 straights are possible max
        easier_straights = 2
    elif easier_straights == 4: #The distance of the cards is 4 (ex. 5,9) and 1 straight is possible max
        easier_straights = 1
    elif 1 in hand: #Sepcifically to check if there is a ace for hands like (K/Q/J/10 and Ace) where it won't be accounted for earlier
        easier_straights = 1 if 13 in hand_values or 12 in hand_values or 11 in hand_values or 10 in hand_values else 0
    else:
        easier_straights = 0
    return easier_straights

def find_viable_straights(hand):
    """This function find the viable straights using the 2 ranks of the hand. So 2 only has 2 while 6 has 5"""
    hand_values = [hand[0].get_value(), hand[1].get_value()]
    max_straights = max(abs(7.5 - hand_values[0]), abs(7.5 - hand_values[1]))
    #7.5 is the exact middle (excluding ace), so by subtracting a card's value (with abs) we can find which card is farthest from
    #the middle, and preform the necesssary changes to the straight_count
    straight_count = 0
    if max_straights == 6.5: #This can only be found with a ace (7.5 - 1) = 6.5
        straight_count = 1 if 2 in hand_values or 3 in hand_values or 4 in hand_values or 5 in hand_values \
            or 10 in hand_values or 11 in hand_values or 12 in hand_values or 13 in hand_values else 0
        #If there is a ace there needs to be a 2,3,4,5 or K,Q,J,10
    elif max_straights == 5.5: #This can only be found with a king or 2 (|7.5 - (2 or 13)| = 5.5)
        straight_count = 2
    elif max_straights == 4.5: #This can only be found with a queen or 3 (|7.5 - (3 or 12)| = 4.5)
        straight_count = 3
    elif max_straights == 3.5: #This can only be found with a jack or 4 (|7.5 - (4 or 11)| = 3.5)
        straight_count = 4
    elif max_straights <= 2.5: #This is all other numbers (|7.5 - (5,6,7,8,9,10)| = 2.5 or less (1.5, 0.5))
        straight_count = 5
    return straight_count

def total_straight_counter(rank):
    """This function returns the total possible straights a rank can have"""
    if rank == 1: return 2
    if rank == 2: return 2
    if rank == 3: return 3
    if rank == 4: return 4
    if rank == 5: return 5
    if rank == 6: return 5
    if rank == 7: return 5
    if rank == 8: return 5
    if rank == 9: return 5
    if rank == 10: return 5
    if rank == 11: return 4
    if rank == 12: return 3
    if rank == 13: return 2

def flop_helper(hand):
    """This method takes in the hand as a parameter, and outputs the number of possible straights that can be
    formed with the given hand in the flop."""
    easier_straights = find_easy_straights(hand)
    viable_straights = find_viable_straights(hand)
    return min(easier_straights, viable_straights)

def turn_helper_flopless(hand):
    """This method takes in the hand as a parameter, and outputs the number of possible straights that can be
    formed with the given hand in the turn."""
    hand_values = [hand[0].get_value(), hand[1].get_value()]
    total_straights = total_straight_counter(hand_values[0]) + total_straight_counter(hand_values[1])
    easy_straights = find_easy_straights(hand) #find the straights we have 2 ranks for
    medium_straights = total_straights - easy_straights  #find the straights we have 1 rank for
    return [medium_straights, easy_straights]

def river_helper_flopless(hand):
    """This method takes in the hand as a parameter, and outputs the number of possible straights that can be
    formed with the given hand in the river."""
    hand_values = [hand[0].get_value(), hand[1].get_value()]
    straights_with_hand = total_straight_counter(hand_values[0]) + total_straight_counter(hand_values[1])
    easy_straight = find_easy_straights(hand) #find the straights we have 2 ranks for
    medium_straight = straights_with_hand - easy_straight #find the straights we have 1 rank for
    hard_straight = 10 - easy_straight - medium_straight #finds the straights we have 0 ranks for
    return [hard_straight, medium_straight, easy_straight]