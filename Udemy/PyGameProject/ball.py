import pygame
from constanse import BALL_STEP


class Ball:
    def __init__(self, fighter):
        self.image = pygame.image.load('images/ball.png')
        self.width, self.height = self.image.get_size()
        self.x, self.y = 0, 0
        self.was_fire = False
        self.step = BALL_STEP
        self.fighter = fighter

    def fire(self):
        self.was_fire = True
        self.x = self.fighter.x + self.fighter.height / 2
        self.y = self.fighter.y - self.height

    def update_position(self):
        if self.was_fire:
            self.y -= self.step

    def is_out_of_screen(self):
        if self.y + self.height <= 0 and self.was_fire:
            self.was_fire = False

    def reset(self):
        self.was_fire = False

    def is_collision(self, alien):
        return self.was_fire and \
                (alien.x < self.x < alien.x + alien.width or
                 alien.x < self.x + self.width < alien.x + alien.width) \
                and self.y <= alien.y + alien.height

