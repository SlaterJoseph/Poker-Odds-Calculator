#These are sets of all possible straights with each possible card that will be returned in the set_return function
ace_straights = {1, 10}
two_straights = {1, 2}
three_straights = {1, 2, 3}
four_straights = {1, 2, 3, 4}
five_straights = {1, 2, 3, 4, 5}
six_straights = {2, 3, 4, 5, 6,}
seven_straights = {3, 4, 5, 6, 7,}
eight_straights = {4, 5, 6, 7, 8}
nine_straights = {5, 6, 7, 8, 9}
ten_straights = {6, 7, 8, 9, 10,}
jack_straights = {7, 8, 9, 10}
queen_straights = {8, 9, 10}
king_straights = {9, 10}

def set_return(value):
    """This takes a parameter of a value, then returns the set of all possible straights of that numbers,
    so ace will return a set with length 2, four will return a set with length 4, 6 will return a set of length 5
    (Look above/in the code to view the correlation of rank to possible straights"""
    if value == 1:
        return ace_straights
    elif value == 2:
        return two_straights
    elif value == 3:
        return three_straights
    elif value == 4:
        return four_straights
    elif value == 5:
        return five_straights
    elif value == 6:
        return six_straights
    elif value == 7:
        return seven_straights
    elif value == 8:
        return eight_straights
    elif value == 9:
        return nine_straights
    elif value == 10:
        return ten_straights
    elif value == 11:
        return jack_straights
    elif value == 12:
        return queen_straights
    elif value == 13:
        return king_straights