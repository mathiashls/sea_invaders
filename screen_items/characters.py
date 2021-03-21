import abc
import pygame
import random


class ScreenItem(object):

    SKIN = None

    def __init__(self, position_x, position_y, pace_x, pace_y):
        self.position_x = position_x
        self.position_y = position_y
        self.pace_x = pace_x
        self.pace_y = pace_y
        self.image = pygame.image.load(self.SKIN)

    @abc.abstractmethod
    def set_bounds(self):
        """
        Each new implemented element must know and set it's own bounds based
        on the screen resolution. That's why every element have a screen
        reference inside it. Attributes to be set are:

        self.left_bounds
        self.right_bounds
        self.top_bounds
        self.bottom_bounds
        """
        pass

    def is_inbounds(self):
        """
        A game element can't pass it's own bounds. This method check if
        current position respect current bounds.
        """
        return all(
            self.left_bounds  <= self.position_x <= self.right_bounds and
            self.top_bounds  <= self.position_y <= self.bottom_bounds
        )

    def render(self, screen):
        screen.blit(self.image, (self.POSITION_X, self.POSITION_Y))

    def move(self):
        self.position_x += self.pace_x
        self.position_y += self.pace_y


class Player(ScreenItem):
    SKIN = "images/tortoise.png"

    def __init__(self, position_x, position_y, pace_x, pace_y):
        self.score = 0
        super().__init__(position_x, position_y, pace_x, pace_y)


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

    def __init__(self, position_x, position_y, pace_x, pace_y):
        self.state = self.STATE_READY
        super().__init__(position_x, position_y, pace_x, pace_y)

    def shot(self, position_x, position_y):
        self.state = self.STATE_RELOADING
        self.position_x = position_x
        self.position_y = position_y
        self.render()

    def reload(self):
        self.state = self.STATE_READY
        self.position_y = self.screen.get_height() - (self.screen.get_height() * (15/100))
