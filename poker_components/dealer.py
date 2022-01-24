from random import randint, randrange
from deck import Deck

class Dealer:
    deck = Deck() #creating a deck for the dealer to utilize
   
    def __init__(self):
        pass

    def random_number(self):
        drawn_card = randrange(len(self.deck.get_deck())) #gives a random int from 0 to the amount of cards remaining
        return drawn_card #returns the index of the card being drawn

    def burn_card(self): #burning a card is drawing it and then putting it out of play wihtout knowing the card's value
        drawn_card = self.random_number() #gives the index of the card to be burned
        self.deck.get_deck().pop(drawn_card) #removes the card at the drawn_card index, burning the card
        # print(str(card) + "---> Burned") TESTING

    def draw_card(self):
        drawn_card = self.random_number() #gives the index of the card to be drawn
        card = self.deck.get_deck().pop(drawn_card)
        # print(str(card) + "---> Drawn") TESTING
        return card

    def deal_player(self): #In texas holdem a player only has 2 cards, and no cards are burnt while dealing
        hand = []
        hand.append(self.draw_card()) #adding the two cards to the hand
        hand.append(self.draw_card())
        return hand #returns the hand

    def deal_flop(self): #the flop is the first set of 3 cards, with one being burned before the 3 are revealed
        flop = []
        self.burn_card() #burning the card
        flop.append(self.draw_card()) #adding the 3 cards to the flop list
        flop.append(self.draw_card())
        flop.append(self.draw_card())
        return flop #return the flop

    def deal_turn_river(self): #the turn and river are the 2 turns after the flop. They both burn one card then add one to the table
        self.burn_card()
        return self.draw_card()

    def shuffle_deck(self):
        self.deck.shuffle_deck() #this "shuffles" the deck object to reset the deck

    def get_deck(self): #a simple getter to get the deck the dealer is utilizing 
        return self.deck


        
