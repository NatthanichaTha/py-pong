import pygame
from paddle import Paddle
from random import random, randint
from constant import *

class Ball:
    def __init__(self, start_point_x, start_point_y):
        self.x = start_point_x
        self.y = start_point_y
        self.radius = 15
        
        self.ballspeed_x = 5
        self.ballspeed_y = 5
    
    def draw(self, screen):
        pygame.draw.circle(
            surface=screen, color=(255, 255, 255), center=(self.x, self.y), radius=self.radius)
    
    def is_out(self):
        #out (=touch or beyond the horizontal border)
        if self.x - self.radius <= 0:
            return 1
        elif self.x + self.radius >= SCREEN_WIDTH:
            return 2

        return 0 
        
    def touch_corner(self):
        if self.y - self.radius == 0 or self.y + self.radius == SCREEN_HEIGHT:
            return 1 #touch the vertical border (1)
        return 0
    
    def check_touch(self, paddle: Paddle):
        if self.x - self.radius > paddle.position_x + paddle.width:
            #ball is on the right of paddle and not touching
            return False
        if self.x + self.radius < paddle.position_x:
            #ball is on the left of paddle and not touching
            return False
        if self.y + self.radius < paddle.position_y:
            #ball is above the paddle and not touching
            return False
        if self.y - self.radius > paddle.position_y + paddle.height:
            #ball is below the paddle and not touching
            return False
        
        return True


    def move(self, paddle1, paddle2):

        if self.is_out() != 0:
            self.x = SCREEN_WIDTH/2
            self.y = SCREEN_HEIGHT/2

        if self.check_touch(paddle1) or self.check_touch(paddle2):
            self.ballspeed_x = -self.ballspeed_x
            self.ballspeed_x *= 1.5

        if self.touch_corner() == 1:
            self.ballspeed_y = -self.ballspeed_y

        self.x += self.ballspeed_x
        self.y += self.ballspeed_y
        



