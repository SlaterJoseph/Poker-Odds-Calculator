class Player:
    hand = [] #this is the player's current hand (The two cards only they use)
    focused = False #this is to indicate which player the user can see the cards of
    name = "n/a" #this is the name of the player

    def __init__(self, name, cards): #takes a name and hand and applies them to this instance of player
        self.hand = cards
        self.name = name

    def set_focus(self, boolean): #indicates if this is the player the user sees the cards of
        self.focused = boolean

    def get_focus(self): #a getter to know if thisn player is the focus
        return self.focused

    def get_hand(self): #a getter to get the player's hand
        return self.hand

    def get_name(self): #a getter to get the player's name
        return self.name

    def __str__(self): #a string method to help with testing
        to_return = str(self.hand[0]) + str(self.hand[1]) + '\n'
        return to_return