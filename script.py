#!/usr/bin/env python

from my_modules import functions as f
from time import sleep

def init():
    '''Print out the title display''' 
    print(" ----------------------")
    print("|                      |")
    print("|     Galton Board     |")
    print("|                      |")
    print(" ----------------------\n")


def main():
    '''The main function to run our galton board'''

    # Ask for parameters from user.
    is_int = True
    while is_int:
        try:
            rows = int(input('\nROWS: '))
            balls = int(input('BALLCOUNT: '))
            height = int(input('HEIGHT BELOW: ')) 
        # Check if inputs are integers 
        except:
            print(f.choice(['\tNope, please give me an integer','\tTry again!']))
        else:
            # Check if input height is large enough 
            if height < balls/2:
                print('\tWe need more space:( try a larger number for HEIGHT BELOW')
            else:
                is_int = False
    
    # Create an instance. Set values of instance attributes to user input.
    bd = f.Board(rows, balls, height)

    # Print out, wait 0.2s, and update the board display.
    bd.add_ball()
    while bd.on_display():
        bd.draw_board()
        sleep(0.2)
        bd.next_move()
        bd.draw_board()
        sleep(0.2)
        bd.next_move()
        bd.add_ball()   # Add one ball to board after two moves

    # User can run program again by replying yes. 
    again = input('\n\nPlay agian? Press Y to restart:\t')
    if again == 'y' or again == 'Y':
        main()
    else:
        print('\n\tThanks for playing. See you next time!\n')


if __name__ == "__main__":
    init()
    main()