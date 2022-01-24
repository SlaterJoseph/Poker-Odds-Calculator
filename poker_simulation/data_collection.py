import data_processing

class data_collection:
    #this list collects the data. The first list is preflop, second is flop, third is turn, fourth is river
    data = [[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]]

    def __init__(self):
        self.input_data()
        for x in self.data:
            print(x)


    def input_data(self):
        with open('data.txt') as f:
            curr_line_count = 0 #Every 5 lines is a round, the 1st 4 are players the 5th is the table
            line = f.readline()
            hand1 = []
            hand2 = [] 
            hand3 = []
            hand4 = [] 
            table_cards = []
            while line:
                if curr_line_count == 0:
                    curr_line_count += 1
                    hand1holder = line.split('$')
                    for x in hand1holder:
                        hand1.extend(x.split(':'))

                    hand1.remove('\n')
                    line = f.readline()

                elif curr_line_count == 1:
                    curr_line_count += 1
                    hand2holder = line.split('$')
                    for x in hand2holder:
                        hand2.extend(x.split(':'))

                    hand2.remove('\n')
                    line = f.readline()

                elif curr_line_count == 2:
                    curr_line_count += 1
                    hand3holder = line.split('$')
                    for x in hand3holder:
                        hand3.extend(x.split(':'))

                    hand3.remove('\n')
                    line = f.readline()

                elif curr_line_count == 3:
                    curr_line_count += 1
                    hand4holder = line.split('$')
                    for x in hand4holder:
                        hand4.extend(x.split(':'))

                    hand4.remove('\n')
                    line = f.readline()

                else:
                    tableHolder = line.split('$')
                    for x in tableHolder:
                        table_cards.extend(x.split(':'))
                    line = f.readline()
                    self.process_data(hand1, hand2, hand3, hand4, table_cards)
                    table_cards.clear()
                    hand1.clear()
                    hand2.clear()
                    hand3.clear()
                    hand4.clear()
                    curr_line_count = 0
            
    def process_data(self, hand1, hand2, hand3, hand4, table_cards):
        processing = data_processing()
        print('processing')
        i = 0
        while i < 4:
            if i == 0:
                if(hand1[1] == hand1[3]):
                    self.data[0][1] += 1
                else:
                    self.data[0][0] += 1

                if(hand2[1] == hand2[3]):
                    self.data[0][1] += 1
                else:
                    self.data[0][0] += 1

                if(hand3[1] == hand3[3]):
                    self.data[0][1] += 1
                else:
                    self.data[0][0] += 1

                if(hand4[1] == hand4[3]):
                    self.data[0][1] += 1
                else:
                    self.data[0][0] += 1
             
            elif i == 1:
                flop = table_cards[0:6]
                self.data[1][processing.set_up(hand1, flop)] += 1
                self.data[1][processing.set_up(hand2, flop)] += 1
                self.data[1][processing.set_up(hand3, flop)] += 1
                self.data[1][processing.set_up(hand4, flop)] += 1

            elif i == 2:
                turn = table_cards[0:8]
                self.data[2][processing.set_up(hand1, turn)] += 1
                self.data[2][processing.set_up(hand2, turn)] += 1
                self.data[2][processing.set_up(hand3, turn)] += 1
                self.data[2][processing.set_up(hand4, turn)] += 1
            else:
                river = table_cards[0:10]
                self.data[3][processing.set_up(hand1, river)] += 1
                self.data[3][processing.set_up(hand2, river)] += 1
                self.data[3][processing.set_up(hand3, river)] += 1
                self.data[3][processing.set_up(hand4, river)] += 1
                
            i += 1

