import pygame
from pygame import rect
from pygame.constants import *
import pygame.sprite


board_squares=[]

class Display_board:
    def __init__(self)->None:
        self.window=Window()
        
        self.screen=self.window.screen
        self.height=6400
        self.width=6400
        
        self.black=[0,0,0]
        self.white=[255,255,255]

    def make_bored (self):
        for i in range(64):
            column=i%8
            row=int(i//8)
            x=column*100
            y=row*100
            row_odd=row%2
            column_odd=column%2
            black=row_odd==column_odd
            if black:
                color=self.black
            else: 
                color=self.white
            self.square=pygame.Rect(x,y,(self.width/64),(self.height/64))
            pygame.draw.rect(self.screen,color,self.square)
            board_squares.append(self.square)
            
            
class Window:
    def __init__(self)->None:
        self.running = True
        (self.width, self.height) = (1850, 1000)
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.screen.fill([0,0,255])
        
    
    def run_loop(self):
        keys=pygame.key.get_pressed()
        while self.running:
            pygame.display.flip()

            for event in pygame.event.get():
                
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running=False
                if event.type == pygame.QUIT:
                    self.running = False
#chess_game.Board()
#display_board=Display_board()
#display_board.make_bored()
#display_board.window.run_loop()

