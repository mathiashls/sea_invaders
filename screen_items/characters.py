import abc
import pygame
import random


class ScreenItem(object):

    SKIN = None

    def __init__(self, screen, screen_bounds, position_x, position_y, pace_x, pace_y):
        self.screen = screen
        self.screen_bounds = screen_bounds
        self.position_x = position_x
        self.position_y = position_y
        self.pace_x = pace_x
        self.pace_y = pace_y
        self.image = pygame.image.load(self.SKIN)

    def render(self):
        """ Render object on screen based o current set positions """
        self.screen.blit(self.image, (self.position_x, self.position_y))

    @abc.abstractmethod
    def move(self):
        """ Defines how each ScreenItem subclass will move """


class Player(ScreenItem):
    SKIN = "images/tortoise.png"

    def __init__(self, screen, screen_bounds, position_x, position_y, pace_x, pace_y):
        self.score = 0
        super().__init__(
            screen, screen_bounds, position_x, position_y, pace_x, pace_y
        )

    def move(self, change_x, change_y):
        self.position_x += change_x
        self.position_y += change_y


class Enemy(ScreenItem):

    def __init__(self, position_x, position_y, pace_x, pace_y):
        self.SKIN = random.choice(
            "images/plastic_bag.png"
            "images/plastic_bottle.png"
            "images/straw_01.png"
            "images/straw_02.png"
        )
        super().__init__(position_x, position_y, pace_x, pace_y)


class Bullet(ScreenItem):
    SKIN = "images/crab.png"
    STATE_READY = "bullet_ready"
    STATE_RELOADING = "bullet_reloading"

    def __init__(self, screen, screen_bounds, position_x, position_y, pace_x, pace_y):
        self.state = self.STATE_READY
        super().__init__(
            screen, screen_bounds, position_x, position_y, pace_x, pace_y
        )

    def move(self):
        pass

    def shot(self, position_x, position_y):
        self.state = self.STATE_RELOADING
        self.position_x = position_x
        self.position_y = position_y
        self.render()

    def reload(self):
        self.state = self.STATE_READY
        self.position_y = self.screen.get_height() - (self.screen.get_height() * (15/100))
