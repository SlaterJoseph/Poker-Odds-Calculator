import data_processing

class data_collection:
    #this list collects the data. The first list is preflop, second is flop, third is turn, fourth is river
    data = [[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]]

    def __init__(self):
        self.input_data()

    def input_data(self):
        with open('data.txt') as f:
            curr_line_count = 0 #Every 5 lines is a round, the 1st 4 are players the 5th is the table
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

                hand2holder = line.split('$')
                hand2.extend(hand2holder[0].split(':'))
                hand2.extend(hand2holder[1].split(':'))
                hand2.remove('\n')
                line = f.readline()

                hand3holder = line.split('$')
                hand3.extend(hand3holder[0].split(':'))
                hand3.extend(hand3holder[1].split(':'))
                hand3.remove('\n')
                line = f.readline()

                hand4holder = line.split('$')
                hand4.extend(hand4holder[0].split(':'))
                hand4.extend(hand4holder[1].split(':'))
                hand4.remove('\n')
                line = f.readline()

                tableHolder = line.split('$')
                table_cards.extend(tableHolder[0].split(':'))
                table_cards.extend(tableHolder[1].split(':'))
                table_cards.extend(tableHolder[2].split(':'))
                table_cards.extend(tableHolder[3].split(':'))
                table_cards.extend(tableHolder[4].split(':'))
                line = f.readline()

                self.process_data(hand1, hand2, hand3, hand4, table_cards)
                table_cards.clear()
                hand1.clear()
                hand2.clear()
                hand3.clear()
                hand4.clear()
            
    def process_data(self, hand1, hand2, hand3, hand4, table_cards):
        processing = data_processing()
        if hand1[1] == hand1[3]:
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