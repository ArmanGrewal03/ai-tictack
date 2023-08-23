from constants import *
import pygame
from board import Board
class Game:

    def __init__(self):
        self.player=1
        self.running=True
        self.gamemode='ai'
        self.board=Board()

    def bg(self, surface):
        pygame.draw.line(surface,LINE_COLOR,(SQSIZE,0),(SQSIZE,HEIGHT),LINE_WIDTH)
        pygame.draw.line(surface,LINE_COLOR,(WIDTH-SQSIZE,0),(WIDTH-SQSIZE,HEIGHT),LINE_WIDTH)

        pygame.draw.line(surface,LINE_COLOR,(0,SQSIZE),(WIDTH,SQSIZE),LINE_WIDTH)
        pygame.draw.line(surface,LINE_COLOR,(0,HEIGHT-SQSIZE),(WIDTH,HEIGHT-SQSIZE),LINE_WIDTH)
    
    def next_turn(self):
        self.player=self.player%2+1

    def change_gamemode(self):
        if self.gamemode=='2p':
            self.gamemode='ai'
        else:
            self.gamemode='2p'

    def reset(self):
        self.__init__()
        print('reset game')
    
    def isover(self,board):
        return board.final_state()!= 0 or board.is_full()


    def draw_fig(self,row,col,screen):
        if self.player==1:
            start_desc=(col*SQSIZE+OFFSET,row*SQSIZE+OFFSET)
            end_desc=(col*SQSIZE+SQSIZE-OFFSET,row*SQSIZE+SQSIZE-OFFSET)
            pygame.draw.line(screen,CROSS_COLOR,start_desc,end_desc,CROSS_WIDTH)
            start_asc=(col*SQSIZE+OFFSET,row*SQSIZE+SQSIZE-OFFSET)
            end_asc=(col*SQSIZE+SQSIZE-OFFSET,row*SQSIZE+OFFSET)
            pygame.draw.line(screen,CROSS_COLOR,start_asc,end_asc,CROSS_WIDTH)
        elif self.player==2:
            centre=(col*SQSIZE+SQSIZE//2,row*SQSIZE+SQSIZE//2)
            pygame.draw.circle(screen,CIRC_COLOR,centre,RADIUS,CIRC_WIDTH)
            