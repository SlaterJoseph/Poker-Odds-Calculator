def running():
    """This method selects which mode to run. If the input is 1 it is simulation mode. If it is 2 it is probabiltiy mode"""
    mode_select = int(input('If 1 in putting the program goes into simulation mode. If 2 is inputed the program goes into probability mode'))

    while mode_select < 1 or mode_select > 4:
        mode_select = int(input('Invalid input. Please input a number 1 - 4 (1 for simulation, 2 for probability'))
