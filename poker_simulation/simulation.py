from ..poker_components import poker_components

class simulation:

    def __init__(self):
        self.processing()

    def processing(self):
        my_file = open('data.txt', 'w') #opens the file to place the data
        i = 0; 
        my_table = Table() #creates a table
        while i < 10000000:
            my_file.write(str(my_table)) #prints the data of the round to the file
            my_table.reset_round() #resets the table for the next round
            i += 1 #increments i
        my_file.close() #closes the file
        


        