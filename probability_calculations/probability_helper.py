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

def truncate(number) -> float: #cuts the number off at 6 decmial spaces
    stepper = 10.0 ** 6
    return math.trunc(stepper * number) / stepper

def process_dictionary(dictionary, searching_num): #this method checks a dictionary of ranks, and increments a variable 
    #based on how many of those keys values match the searching_num

    checked_value = 0
    if(dictionary[1] == searching_num): checked_value += 1
    if(dictionary[2] == searching_num): checked_value += 1
    if(dictionary[3] == searching_num): checked_value += 1
    if(dictionary[4] == searching_num): checked_value += 1
    if(dictionary[5] == searching_num): checked_value += 1
    if(dictionary[6] == searching_num): checked_value += 1
    if(dictionary[7] == searching_num): checked_value += 1
    if(dictionary[8] == searching_num): checked_value += 1
    if(dictionary[9] == searching_num): checked_value += 1
    if(dictionary[10] == searching_num): checked_value += 1
    if(dictionary[11] == searching_num): checked_value += 1
    if(dictionary[12] == searching_num): checked_value += 1
    if(dictionary[13] == searching_num): checked_value += 1
    return checked_value