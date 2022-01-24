class data_processing:
    #these 4 sets are for checking if straights are also a flush
    spades = set()
    hearts = set()
    diamonds = set()
    clubs = set()

    def __init__(self):
        pass

    def processing(self, ranks, suits, straight, flush):
        #this checks if there is a straight, if it's royal, and if the numbers are the same suit
        if straight == 'royal' and flush == True:
            return 9
        #this checks if there is a striaght and if the numbers have the same suit
        elif straight == True and flush == True:
            return 8
        #this checks if values has a value of 4, meaning there is a four of a kind
        elif 4 in ranks.values():
            return 7
        #this checks if values contains a value of 2 and 3, meaning there is a full house
        elif 2 in ranks.values() and 3 in ranks.values():
            return 6
        #this checks for a flush. if any of the suits have 5 it means a flush is on the board
        elif suits.get('heart') == 5 or suits.get('spade') == 5 or suits.get('diamond') == 5 or suits.get('club') == 5:
            return 5
            #this checks for a straight
        elif straight == True or straight == 'royal':
            return 4
        #this checks if ranks has a 3, meaning there is a 3 of a kind
        elif 3 in ranks.values():
            return 3
        #this checks if the ranks has a value of 2, which means one or more pairs
        elif 2 in ranks.values():
            del ranks[(list(ranks.keys())[list(ranks.values()).index(2)])] #this removes the first instance of a 2 in ranks values
            if 2 in ranks.values(): #if rank contains another 2 it means there are 2 pairs
                return 2
            else:
                return 1

        else: #this is for when all other cases fail and a high card is what you have
            return 0

    def set_up(self, hand, table_cards):
        suits = dict({'heart':0 , 'spade':0, 'diamond':0, 'club':0}) #a dictionary of all suits
        ranks = dict({1:0 , 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0, 12:0, 13:0}) #a dictionary of all values     

        #this block adds the hand and the flop to the suit and value dictionaries
        suits[hand[0]] = suits.get(hand[0]) + 1
        suits[hand[2]] = suits.get(hand[2]) + 1
        suits[table_cards[0]] = suits.get(table_cards[0]) + 1
        suits[table_cards[2]] = suits.get(table_cards[2]) + 1
        suits[table_cards[4]] = suits.get(table_cards[4]) + 1
        
        ranks[int(hand[1])] = ranks.get(int(hand[1])) + 1
        ranks[int(hand[3])] = ranks.get(int(hand[3])) + 1
        ranks[int(table_cards[1])] = ranks.get(int(table_cards[1])) + 1
        ranks[int(table_cards[3])] = ranks.get(int(table_cards[3])) + 1
        ranks[int(table_cards[5])] = ranks.get(int(table_cards[5])) + 1

        self.add_to_set(hand[0], hand[1])
        self.add_to_set(hand[2], hand[3])
        self.add_to_set(table_cards[0], table_cards[1])
        self.add_to_set(table_cards[2], table_cards[3])
        self.add_to_set(table_cards[4], table_cards[5])

        if(len(table_cards) >= 8): #if the length is this long we are up to the turn, so add 1 more card
            suits[table_cards[6]] = suits.get(table_cards[6]) + 1
            ranks[int(table_cards[7])] = ranks.get(int(table_cards[7])) + 1     
            self.add_to_set(table_cards[6], table_cards[7])


        if(len(table_cards) == 10): #if the length is this long we are up to the river, so add 1 more card
            suits[table_cards[8]] = suits.get(table_cards[8]) + 1
            ranks[int(table_cards[9])] = ranks.get(int(table_cards[9])) + 1 
            self.add_to_set(table_cards[8], table_cards[9])
   
        flush = False #this only check for straight flushes. It does not check for standard flushes
        straight = False
        for x in ranks: #
            try:
                if ranks[x] >= 1:
                    if x > 10:
                        break
                    elif x == 10:
                        if ranks[11] >= 1 and ranks[12] >= 1 and ranks[13] >= 1 and ranks[1] >= 1:
                            straight = 'royal'
                            flush = self.check_royal_flush()
                            break
                    else:
                        if ranks[x+1] >= 1 and ranks[x+2] >= 1 and ranks[x+3] >= 1 and ranks[x+4] >= 1:
                            straight = True
                            flush = self.check_flush(x)
                elif x >= 10:
                    break
            except KeyError:
                break
        self.spades.clear()
        self.hearts.clear()
        self.clubs.clear()
        self.diamonds.clear()
        return self.processing(ranks, suits, straight, flush)

    def add_to_set(self, suit, rank):
        if suit == 'spade':
            self.spades.add(int(rank))
        elif suit == 'heart':
            self.hearts.add(int(rank))
        elif suit == 'club':
            self.clubs.add(int(rank))
        else:
            self.diamonds.add(int(rank))

    def check_flush(self, rank): #This method check if the straight from above is also a flush
        if rank in self.spades and (rank + 1) in self.spades and (rank + 2) in self.spades and (rank + 3) in self.spades and (rank + 4) in self.spades:
            return True
        elif rank in self.hearts and (rank + 1) in self.hearts and (rank + 2) in self.hearts and (rank + 3) in self.hearts and (rank + 4) in self.hearts:
            return True
        elif rank in self.clubs and (rank + 1) in self.clubs and (rank + 2) in self.clubs and (rank + 3) in self.clubs and (rank + 4) in self.clubs:
            return True
        elif rank in self.diamonds and (rank + 1) in self.diamonds and (rank + 2) in self.diamonds and (rank + 3) in self.diamonds and (rank + 4) in self.diamonds:
            return True
        else:
            return False

    def check_royal_flush(self): #this checks just royal straights to see if their a flush
        if 10 in self.spades and 11 in self.spades and 12 in self.spades and 13 in self.spades and 1 in self.spades:
            return True
        elif 10 in self.hearts and 11 in self.hearts and 12 in self.hearts and 13 in self.hearts and 1 in self.hearts:
            return True
        elif 10 in self.clubs and 11 in self.clubs and 12 in self.clubs and 13 in self.clubs and 1 in self.clubs:
            return True
        elif 10 in self.diamonds and 11 in self.diamonds and 12 in self.diamonds and 13 in self.diamonds and 1 in self.diamonds:
            return True
        else:
            return False