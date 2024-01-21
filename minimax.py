import copy
import numpy as np

class Board:
    def __init__(self) -> None:
        self.squares = np.zeros( ( 3, 3) )
        self.marked_srs = 0
    
    def is_emp_sqr(self,row,col):
        return self.squares[row][col] == 0
        
    def mark_sqr(self,row,col,val):
        if self.is_emp_sqr(row,col):
            self.squares[row][col]== val
class Game:
    def __init__(self) -> None:
        self.board = Board()
        self.player = 2
        self.stack_moves = []
    
    def make_move(self,row,col):
        self.board.mark_sqr(row,col,self.player)

    def next_turn(self):
        self.player = (self.player + 1) // 2 