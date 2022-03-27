def simulation():
    """This function is called to run simulation mode"""
    simulation_count = int(input('How many games do you wish to process?'))
    if simulation_count > 1000:
        confirm = str(input('A simulation of', simulation_count, 'may take considerable time. Are you sure? (Yes or No)'))
        if str.lower(confirm) == 'no':
            simulation()
        if str.lower(confirm) != 'yes':
            print('Invalid input. Resetting')
            simulation()
    
    #Code to run simulation here

def probability():
    """This function is called to run probability mode"""
    print('As of now, you cannot choose the cards. They are distributed at random')
    #code to run probability here