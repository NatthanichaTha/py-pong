import pygame
from pygame.locals import *
from ball import Ball 
from paddle import Paddle
from constant import *

class PongGame:
    def __init__(self):      
        #Initialise screen
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("PyPong")

        self.p1_score = 0
        self.p2_score = 0

        # Fill background
        self.background = pygame.Surface(self.screen.get_size())
        self.background = self.background.convert()
        self.background.fill(BG_COLOR)

        #Make texts to show player score
        self.font = pygame.font.Font('digital-7.ttf', 50)
        self.score1_text = self.font.render(str(self.p1_score), True, BLUE)
        self.score2_text = self.font.render(str(self.p2_score), True, YELLOW)
        self.textRect_1 = self.score1_text.get_rect()
        self.textRect_2 = self.score2_text.get_rect()
        self.textRect_1.center = (SCORE1_X, SCORE1_Y)
        self.textRect_2.center = (SCORE2_X, SCORE2_Y)

        self.clock = pygame.time.Clock()

        self.ball = Ball(SCREEN_CENTER[0], SCREEN_CENTER[1])

        self.paddle1 = Paddle("left", BLUE, pygame.K_w, pygame.K_s)
        self.paddle2 = Paddle("right", YELLOW, pygame.K_UP, pygame.K_DOWN)

    def game_loop(self):
        while True:
            # Events: keyboard input
            for event in pygame.event.get():
                if event.type == QUIT:
                    return
            
            # Logic: moving the ball, see if it went out of screen ecc..
            self.ball.move(self.paddle1, self.paddle2)
            self.paddle1.move()
            self.paddle2.move()
            
            if self.ball.is_out() != 0:  
                if self.ball.is_out() == 1:
                    self.p2_score += 1
                elif self.ball.is_out() == 2:
                    self.p1_score += 1

                self.ball.ballspeed_x = 0
                self.ball.ballspeed_y = 0
                self.paddle1.reset()
                self.paddle2.reset()

            key_pressed = pygame.key.get_pressed()
            if key_pressed[pygame.K_SPACE] and self.ball.ballspeed_x == 0 and self.ball.ballspeed_y == 0:
                self.ball.ballspeed_x = 5
                self.ball.ballspeed_y = 5
                
                self.ball.move(self.paddle1, self.paddle2)

            # Rendering: first clear with background and then draw each object
            # Blit everything to the screen
            self.screen.blit(self.background, (0, 0))

            self.score1_text = self.font.render(str(self.p1_score), True, BLUE)
            self.score2_text = self.font.render(str(self.p2_score), True, YELLOW)
            self.screen.blit(self.score1_text, self.textRect_1)
            self.screen.blit(self.score2_text, self.textRect_2)

            self.ball.draw(self.screen)
            self.paddle1.draw(self.screen)
            self.paddle2.draw(self.screen)
            pygame.display.flip()
            self.clock.tick(30)