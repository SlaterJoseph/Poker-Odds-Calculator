from all_straight_for_card import set_return

def flop_straights_helper(hand):
    card_1_sets = set_return(hand[0].get_value())
    card_2_sets = set_return(hand[1].get_value())
    #The interesection of the possible straights are all the straights in common between the two hand cards
    #and only straights involving both hand cards are possible in the flop
    all_possible_straights = set.intersection(card_1_sets, card_2_sets)
    return len(all_possible_straights)

def turn_straight_helper_flopless(hand):
    card_1_sets = set_return(hand[0].get_value())
    card_2_sets = set_return(hand[1].get_value())
    #All possible straights involve one of the hand cards, so all straights cd vs   
    all_straights = set.union(card_1_sets, card_2_sets)
    simple_straights = set.intersection(card_1_sets, card_2_sets)
    return [len(all_straights) - len(simple_straights), len(simple_straights)]