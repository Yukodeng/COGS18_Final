from random import choice
from time import sleep
from math import floor
from IPython.display import clear_output

    
def print_out(text):
    '''Clear previous display and print out the current board.
        Used for updating each ball's position.

        Parameters
        ---------
        text: list
            A 2D array of galton board list.
        '''
    clear_output()
    print(text)
    

class Ball():
    def __init__(self, x):
        '''Initilize a ball.

            Parameters
            ----------
            sign: string
                representation of the ball: 'O'
            x: int
                initial x position of the ball
            y: int
                initial y position of the ball; set to 0
            '''
        self.sign = 'O'         
        self.x = x
        self.y = 0
    
    def move(self):
        '''Update ball position when it falls left or right.'''    
        self.x += choice([-1,1])  #randomly goes left or right
        self.y += 2     # not 1 becuase need to skip the grid row 
        
    def fall(self):
        '''Update ball position when it falls vertically'''
        self.y += 1

        
class Board(Ball):
    def __init__(self, rows, ballcount, height):
        '''Inherit from Ball class. Initilize the board.

            Parameters
            --------
            sign: string
                Representaltion of the ball: 'O'
            x: int
                Initial x position of the ball
            y: int
                Initial y position of the ball; set to 0
            rows: int
                Number of peg rows
            ballcount: int
                Total number of balls
            height: int
                Max height of ball stack below the pegs
            boardx: int
                x dimension of the board
            grid_list: list
                2d array of list for all possible positions on board
            balls: list
                List of current number of balls
            stack: list
                List of ballcount in each stack respectively
            '''
        self.sign = 'O'
        self.x = rows
        self.y = 0
        self.rows = rows
        self.ballcount = ballcount
        self.height = height
        self.boardx = rows*2 + 1
        self.grid_list = [[''for c in range(rows*2 + 1)]
                              for r in range(rows*2 + height)] 
        self.balls = []
        self.stack = [0]*(rows + 1)
        
       
    def draw_pegs(self):  
        '''Assign pegs to correct positions'''
        pegcount = 1    
        pegdrawn = 0
        firstx = (self.boardx-1) / 2
        pegx = firstx
        pegy = 1

        # Loop through positions of a squared grid row by row using 
        # a for loop wihtin another for loop.  The first if statement
        # checks whether should assign '.' to the position to represent
        # a peg. After each assignment, update next peg x position by +2 
        # and add 1 to the number of pegs assigned.  The second if 
        # stateemnt updates conditions for the next peg row. Eventually
        # we get a triangle of pegs.

        for r in range(self.boardx):                                    
            for c in range(self.boardx):                                
                if c == pegx and r == pegy and pegdrawn < pegcount:
                    self.grid_list[r][c] = '.'
                    pegdrawn += 1
                    pegx += 2          

            if r >= 1 and r % 2 == 0:
                pegcount += 1 
                pegdrawn = 0
                firstx -= 1
                pegx = firstx
                pegy += 2      

            
    def draw_ball(self,ball):
        '''Assign ball to its current position.
            
            Parameter
            ---------
            ball: __main__.Ball
                Instance of the Ball class
        '''
        self.grid_list[ball.y][ball.x] = self.sign 


    def next_move(self):
        '''Decide the next ball move.'''

        # Loop through each ball on the board.  If ball y position is
        # above the last row of pegs, randomly move it left or right.
        # If ball is suspended in the empty space below, move it down 1
        # grid. If ball touches the stack of balls, do not move it and
        # add 1 to the ballcount in this stack.

        for ball in self.balls:
            if ball.y < self.boardx - 1:
                ball.move()
            elif ball.y < self.boardx - 1 + self.height - self.stack[floor(ball.x/2)]:
                ball.fall()
            elif ball.y == self.boardx - 1 + self.height - self.stack[floor(ball.x/2)]:
                self.stack[floor(ball.x/2)] += 1
            

    def add_ball(self):
        '''Keep adding balls to the board.'''
        if len(self.balls) < self.ballcount:
            self.balls.append(Ball(self.x))

    def on_display(self):
        '''Returns a boolean of whether all the balls have fallen.'''
        boolean = sum(self.stack) < len(self.balls)
        return boolean
        
    
    def draw_board(self):
        '''Given assignment of pegs and balls to their positions,
            print out the entire board.'''
        self.grid_list = [[' 'for c in range(self.boardx)] 
                               for r in range(self.boardx + self.height)] 
        self.draw_pegs()
        for ball in self.balls:
            self.draw_ball(ball)
        print_out('\n'.join([' '.join(i) for i in self.grid_list]))  

       
        

