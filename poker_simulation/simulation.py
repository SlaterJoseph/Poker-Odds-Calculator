import sys
sys.path.append()
print(sys.path)

from poker_table import Table

class simulation:
    """This class simulates the games of poker, writing the results down in a txt file to be parsed later. It contains 2 functions
    __init__ (No parameters, calls the processing function)
    processing (Opens the text file, then creates a table, putting the cards from table in the text file in a specific
    format to be parsed later. For now the looptime is predetermined and must be changed in the code"""
    def __init__(self):
        self.processing()

    def processing(self):
        my_file = open('data.txt', 'w') #opens the file to place the data
        i = 0; 
        my_table = Table() #creates a table
        while i < 100:
            my_file.write(str(my_table)) #prints the data of the round to the file
            my_table.reset_round() #resets the table for the next round
            i += 1 #increments i
        my_file.close() #closes the file