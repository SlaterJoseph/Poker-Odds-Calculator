

def flop_helper(hand):
    """This method takes in the hand as a parameter, and outputs the number of possible straights that can be
    formed with the given hand."""
    hand_values = [hand[0].get_value(), hand[1].get_value()]
    straight_count = abs(hand_values[0] - hand_values[1])
    if straight_count == 0: #The hand contains a pair and a straight is not possible
        straight_count = 0
    elif straight_count == 1: #The distance of the cards is 1 (ex. 5,6) and 4 straights are possible max
        straight_count = 4
    elif straight_count == 2: #The distance of the cards is 2 (ex. 5,7) and 3 straights are possible max
        straight_count = 3
    elif straight_count == 3: #The distance of the cards is 3 (ex. 5,8) and 2 straights are possible max
        straight_count = 2
    elif straight_count == 4: #The distance of the cards is 4 (ex. 5,9) and 1 straight is possible max
        straight_count = 1
    elif 1 in hand: #Sepcifically to check if there is a ace for hands like (K/Q/J/10 and Ace) where it won't be accounted for earlier
        straight_count = 10
    else:
        straight_count = 0

    #Now we need check how are cards are spaced. If it is a K or 2, only 2 straights are possible, even if you cards are 2,3
    # so we need a bunch of checks for all numbers like this (K,Q,J,2,3,4). Aces are special and will be checked later    

    max_straights = max(abs(7.5 - hand_values[0]), abs(7.5 - hand_values[1]))
    #7.5 is the exact middle (excluding ace), so by subtracting a card's value (with abs) we can find which card is farthest from
    #the middle, and preform the necesssary changes to the straight_count
    if max_straights == 6.5: #This can only be found with a ace (7.5 - 1) = 6.5
        straight_count = 1 if 2 in hand_values or 3 in hand_values or 4 in hand_values or 5 in hand_values \
            or 10 in hand_values or 11 in hand_values or 12 in hand_values or 13 in hand_values else 0
        #If there is a ace there needs to be a 2,3,4,5 or K,Q,J,10
    elif max_straights == 5.5: #This can only be found with a king or 2 (|7.5 - (2 or 13)| = 5.5)
        straight_count = min(straight_count, 2)
    elif max_straights == 4.5: #This can only be found with a queen or 3 (|7.5 - (3 or 12)| = 4.5)
        straight_count = min(straight_count, 3)
    elif max_straights == 3.5: #This can only be found with a jack or 4 (|7.5 - (4 or 11)| = 3.5)
        straight_count = min(straight_count, 4)
    elif max_straights <= 2.5: #This is all other numbers (|7.5 - (5,6,7,8,9,10)| = 2.5 or less (1.5, 0.5))
        straight_count = min(straight_count, 5)

    return straight_count