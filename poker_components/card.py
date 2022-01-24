class Card:
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
