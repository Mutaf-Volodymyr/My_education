import pygame
from random import randint
from constanse import SCREEN_WIDTH, ALIENS_STEP


class Alien:
    def __init__(self):
        self.image = pygame.image.load('images/alien.png')
        self.width, self.height = self.image.get_size()
        self.x = randint(0, SCREEN_WIDTH - self.width)
        self.y = 0
        self.step = ALIENS_STEP

    def update_position(self):
        self.y += self.step

    def increase_step(self):
        self.step *= 1.1

    def reset(self):
        self.increase_step()
        self.x = randint(0, SCREEN_WIDTH - self.width)
        self.y = 0

    def has_reached_fighters(self, fighter):
        return self.y + self.height >= fighter.y