import pygame
from constant import *

PADDLE_WIDTH = 30
PADDLE_HEIGHT = 100

class Paddle():
    def __init__(self, start_point_x,color, up_key, down_key):
        self.width = PADDLE_WIDTH
        self.height = PADDLE_HEIGHT
        self.color = color
        self.position_y = (SCREEN_HEIGHT/2) - (self.height/2)
        self.up_key = up_key
        self.down_key = down_key

        if start_point_x == "left":
            self.position_x = 0
        elif start_point_x == "right":
            self.position_x = SCREEN_WIDTH - self.width
    
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, pygame.Rect(self.position_x, self.position_y, self.width, self.height))
    
    def move(self):
        key_pressed = pygame.key.get_pressed()
        if key_pressed[self.up_key] and self.position_y > 0:
            #move up when press up (until the screen edge)
            self.position_y -= 5
        elif key_pressed[self.down_key] and self.position_y + self.height < SCREEN_HEIGHT: 
            #move down when press down (intil the screen edge)
            self.position_y += 5
    
    def reset(self):
        self.position_y = (SCREEN_HEIGHT/2) - (self.height/2)
            



        



    
