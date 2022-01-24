# from card import card
from card import Card

class Deck:
    the_deck = []

    def __init__(self): #the constructor calls the deck building method so the deck is build right away
        self.build_deck()

    def build_deck(self):
        x = 0 #Used to count overall card as well as value and suit on card (0 - Heart Ace, 12 - Heart King, 13 - Spade Ace

        while x < 52: #A deck has 51 cards, so this loop runs 52 time (0-51)
            if x < 13: #0 - 12 will be the heart cards
                suit = "heart"
                value = x + 1
            elif x > 12 and x < 26: #13 - 25 will be the spade cards
                suit = "spade"
                value = x - 12
            elif x > 25 and x < 39: #26 - 38 will be diamond cards
                suit = "diamond"
                value = x - 25
            else: #39 - 51 are the club cards
                suit = "club"
                value = x - 38

            new_card = Card(suit, value) #initializing the new card to add to the deck
            self.the_deck.append(new_card) #adding the card to the deck
            x += 1 #incrementing x

    def __str__(self): #Testing purposes
        to_return = ""
        for x in range(len(self.deck)):
            card = self.deck[x]
            line = str(x) + "." + str(card)
            to_return += str(line) + "\n"
        return to_return

    def get_deck(self): #a simple getter to get the deck
        return self.the_deck

    def shuffle_deck(self): #this method resets the deck by clearing it and rebuilding it
        self.the_deck.clear()
        self.build_deck()

