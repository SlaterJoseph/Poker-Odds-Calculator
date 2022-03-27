from running import simulation
from running import probability
print(dir(__package__))

question = 'If you wish to run simulation mode, input 1. If you wish to run probability mode, input 2'
def main():
    choice = 0
    while choice is not 1 and choice is not 2:
        choice = input(question)
        if choice == 1:
            break
        if choice == 2:
            break
        else:
            print('Invalid input. Please input 1 or 2')
    
    if choice == 1:
        pass
    if choice == 2:
        pass

if __name__ == '__main__':
    main()