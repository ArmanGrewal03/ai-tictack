import pygame
import sys
from constants import *
from game import Game
from board import Board
from ai import AI

class Main: 

    def __init__(self):
        pygame.init()
        self.ai=AI()
        self.game = Game()
        self.board=Board()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('AI Game By Arman Grewal')

    def mainLoop(self):
        screen = self.screen
        game = self.game
        board=self.board
        ai=self.ai
        screen.fill(BG_COLOR)
        while True:
            game.bg(screen)
            if game.running==False:
                pygame.draw.line(screen,board.color,board.iPos,board.fPos,LINE_WIDTH)
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_g:
                        game.change_gamemode()
                        print("GAMEMODE CHANGED TO: "+ game.gamemode)
                    
                    #random ai
                    if event.key==pygame.K_0:
                        ai.level=0
                        print("AI LEVEL:"+ ai.level)

                    if event.key==pygame.K_1:
                        ai.level=1
                        print("AI LEVEL:"+ ai.level)

                    if event.key==pygame.K_r:
                         game.reset()
                         board.reset()
                         screen.fill(BG_COLOR)
                         game.bg(screen)
                       



                if event.type==pygame.MOUSEBUTTONDOWN:
                    pos=event.pos
                    row=pos[1]//SQSIZE
                    col=pos[0]//SQSIZE
                    if board.empty_sqr(row,col) and game.running:
                        board.mark_sqr(row,col,game.player)
                        game.draw_fig(row,col,screen)
                        game.next_turn()
                    if game.isover(board):
                        game.running=False
                        pygame.draw.line(screen,board.color,board.iPos,board.fPos,LINE_WIDTH)
            
            if game.gamemode=='ai' and game.player==ai.player and game.running:
                pygame.display.update()
                row,col=ai.eval(board)
                board.mark_sqr(row,col,ai.player)
                game.draw_fig(row,col,screen)
                game.next_turn()
                if game.isover(board):
                    game.running=False
                    pygame.draw.line(screen,board.color,board.iPos,board.fPos,LINE_WIDTH)
                        
            pygame.display.update()


main = Main()
main.mainLoop()