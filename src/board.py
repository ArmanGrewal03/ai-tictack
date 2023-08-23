import numpy as np
import pygame
from constants import *



class Board:

    def __init__(self):
        self.squares=np.zeros((ROWS,COLS))
        self.marked_squares=0
        self.empty_sqrs=self.squares
        self.color=CIRC_COLOR
        self.iPos=(0,0)
        self.fPos=(0,0)

    def mark_sqr(self,row,col,player):
        self.squares[row][col]=player
        self.marked_squares+=1

    def reset(self):
        self.__init__()
        print('reset board')

    def isempty(self):
        return self.marked_sqrs == 0
    
    def final_state(self,show=False):
        for col in range(COLS):
            if self.squares[0][col]==self.squares[1][col]==self.squares[2][col]!=0:
                self.color=CIRC_COLOR if self.squares[0][col]==2 else CROSS_COLOR
                self.iPos=(col*SQSIZE+SQSIZE//2,20)
                self.fPos=(col*SQSIZE+SQSIZE//2,HEIGHT-20)
                return self.squares[0][col]
        
        for row in range(ROWS):
            if self.squares[row][0]==self.squares[row][1]==self.squares[row][2]!=0:
                self.color = CIRC_COLOR if self.squares[row][0] == 2 else CROSS_COLOR
                self.iPos = (20, row * SQSIZE + SQSIZE // 2)
                self.fPos = (WIDTH - 20, row * SQSIZE + SQSIZE // 2)
                return self.squares[row][0]
        
        if self.squares[2][0]==self.squares[1][1]==self.squares[0][2]!=0:
            self.color = CIRC_COLOR if self.squares[1][1] == 2 else CROSS_COLOR
            self.iPos = (20, HEIGHT - 20)
            self.fPos = (WIDTH - 20, 20)
            return self.squares[2][0]
        
        elif self.squares[0][0]==self.squares[1][1]==self.squares[2][2]!=0:
            self.color = CIRC_COLOR if self.squares[1][1] == 2 else CROSS_COLOR
            self.iPos = (20, 20)
            self.fPos = (WIDTH - 20, HEIGHT - 20)
            return self.squares[0][0]
        
        return 0
        
    def is_full(self):
        return self.marked_squares==9
        
    def empty_sqr(self, row, col):
        return self.squares[row][col] == 0
    
    def get_empty_squares(self):
        empty_squares=[]
        for row in range(ROWS):
            for col in range(COLS):
                if self.squares[row][col]==0:
                    empty_squares.append((row,col))

        return empty_squares
