import math

class probability:

    def __init__(self):
        pass

        #this  method returns the number of cards that should be available in a given round
    def calculate_rounds_to_num(self, rounds):
        if(rounds == 'start'):
            return 2
        elif(rounds == 'flop'):
            return 5
        elif(rounds == 'turn'):
            return 6
        elif(rounds == 'river'):
            return 7

    def caluclate_probability(self, n, k): #n!/k!(n-k)! n is the whole pool, k is the number of a item being searched for
        return math.factorial(n)/(math.factorial(k) * math.factorial (n - k))