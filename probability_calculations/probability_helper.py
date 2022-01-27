import math

def calculate_rounds_to_num(rounds):
    if(rounds == 'start'):
        return 2
    elif(rounds == 'flop'):
        return 5
    elif(rounds == 'turn'):
        return 6
    elif(rounds == 'river'):
        return 7

def caluclate_probability(n, k): #n!/k!(n-k)! n is the whole pool, k is the number of a item being searched for
    return math.factorial(n)/(math.factorial(k) * math.factorial (n - k))