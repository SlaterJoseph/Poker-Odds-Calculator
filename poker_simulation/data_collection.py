import data_processing

class data_collection:
    """This class is where the the data from the simulation is broken up, sent to processing and organized.
    There is a tuple of tuples (called data), with the 1st being pre-flop, 2nd being flop, 3rd being turn and 
    last being river.
    
    When the class is constructed the input_data function is called, which reads and processes the text from data.txt.
    It breaks up each line by '$' (to seperate cards) and by ':' (to seperate rank from suit). Once 5 lines are processed,
    4 for players and 1 for the table, the data is sent to process_data. Once the data is completely processed, the results
    are put in the data tuple."""

    #this list collects the data. The first list is preflop, second is flop, third is turn, fourth is river
    data = ((0,0,0,0,0,0,0,0,0,0),(0,0,0,0,0,0,0,0,0,0),(0,0,0,0,0,0,0,0,0,0),(0,0,0,0,0,0,0,0,0,0))

    def __init__(self):
        self.input_data()

    def input_data(self):
        with open('data.txt') as f:
            line = f.readline()
            hand1 = []
            hand2 = [] 
            hand3 = []
            hand4 = [] 
            table_cards = []
            while line: #This loop splits the line into the hands then send the hands to be processed
                hand1holder = line.split('$') #splits the line of text into cards
                hand1.extend(hand1holder[0].split(':')) #splits the 1st card into suit and rank
                hand1.extend(hand1holder[1].split(':')) #splits the 2nd card into suit and rank
                hand1.remove('\n')
                line = f.readline()

                hand2holder = line.split('$') #splits the line of text into cards
                hand2.extend(hand2holder[0].split(':')) #splits the 1st card into suit and rank
                hand2.extend(hand2holder[1].split(':')) #splits the 2nd card into suit and rank
                hand2.remove('\n')
                line = f.readline()

                hand3holder = line.split('$') #splits the line of text into cards
                hand3.extend(hand3holder[0].split(':')) #splits the 1st card into suit and rank
                hand3.extend(hand3holder[1].split(':')) #splits the 2nd card into suit and rank
                hand3.remove('\n')
                line = f.readline()

                hand4holder = line.split('$') #splits the line of text into cards
                hand4.extend(hand4holder[0].split(':')) #splits the 1st card into suit and rank
                hand4.extend(hand4holder[1].split(':')) #splits the 2nd card into suit and rank
                hand4.remove('\n')
                line = f.readline()

                tableHolder = line.split('$') #splits the line of text into cards
                table_cards.extend(tableHolder[0].split(':')) #splits the 1st card into suit and rank
                table_cards.extend(tableHolder[1].split(':')) #splits the 2nd card into suit and rank
                table_cards.extend(tableHolder[2].split(':')) #splits the 3rd card into suit and rank
                table_cards.extend(tableHolder[3].split(':')) #splits the 4th card into suit and rank
                table_cards.extend(tableHolder[4].split(':')) #splits the 5th card into suit and rank
                line = f.readline()

                self.process_data(hand1, hand2, hand3, hand4, table_cards) #sends our newly organized data to processing
                table_cards.clear() #resets the lists to avoid errors
                hand1.clear()
                hand2.clear()
                hand3.clear()
                hand4.clear()
            
    def process_data(self, hand1, hand2, hand3, hand4, table_cards):
        processing = data_processing()
        if hand1[1] == hand1[3]: #Only a pair is possible in the preflop, so these if else statements process possible pocket pairs
            self.data[0][1] += 1
        else:
            self.data[0][0] += 1

        if hand2[1] == hand2[3]:
            self.data[0][1] += 1
        else:
            self.data[0][0] += 1

        if hand3[1] == hand3[3]:
            self.data[0][1] += 1
        else:
            self.data[0][0] += 1

        if hand4[1] == hand4[3]:
            self.data[0][1] += 1
        else:
            self.data[0][0] += 1

        flop = table_cards[0:6]#processing the hands after the flop is revealed
        self.data[1][processing.set_up(hand1, flop)] += 1
        self.data[1][processing.set_up(hand2, flop)] += 1
        self.data[1][processing.set_up(hand3, flop)] += 1
        self.data[1][processing.set_up(hand4, flop)] += 1

        turn = table_cards[0:8]#processing the hands after the turn is revealed
        self.data[2][processing.set_up(hand1, turn)] += 1
        self.data[2][processing.set_up(hand2, turn)] += 1
        self.data[2][processing.set_up(hand3, turn)] += 1
        self.data[2][processing.set_up(hand4, turn)] += 1

        river = table_cards[0:10]#processing the hands after the river is revealed
        self.data[3][processing.set_up(hand1, river)] += 1
        self.data[3][processing.set_up(hand2, river)] += 1
        self.data[3][processing.set_up(hand3, river)] += 1
        self.data[3][processing.set_up(hand4, river)] += 1