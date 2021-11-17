import pygame
from pygame.constants import K_DOWN, K_a
import pygame.sprite


class Board:
    def __init__(self) -> None:
    self.running = True
    (self.width, self.height) = (300, 200)
    self.screen = pygame.display.set_mode((width, height))
    

    def run_loop(self):
        keys=pygame.key.get_pressed()
        while running:
            pygame.display.flip()

            for event in pygame.event.get():
                
                
            
                if event.type == pygame.QUIT:
                    running = False