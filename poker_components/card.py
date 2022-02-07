class Card:
    """This class is just a basic card. I holds both a suit and a rank, and contains 4 functions:
        __init__ (initializes the card. Takes a suit and rank as parameters)
        get_suit (returns the suit of the card)
        get_value (returns the rank of the card)
        __str__ (a to string function of card)"""
    suit = "none" #holds the suit of the card
    value = 0 #holds the value: 1 - Ace, 13 - King, 10 - Ten

    #the constructor takes a suit(string) and number(int) and assigns the suit and value variables to them
    def __init__(self, suit, number):
        self.suit = suit
        self.value = number

    #simple getter methods for the suit and value
    def get_suit(self):
        return self.suit

    def get_value(self):
        return self.value

    #testing purposes
    def __str__(self):
        return self.suit + ":" + str(self.value) + "$"
