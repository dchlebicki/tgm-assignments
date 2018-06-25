import math
import random
import time

from multiprocessing import Process, Value

SPEED = 7

class Point(Process):
    def __init__(self, x, y, xmove, ymove, color):
        """
        Initializes the point with different properties.

        :param x: the x coordinate of the start position
        :param y: the y coordinate of the start position
        :param xmove: the x range of space in which the point can move
        :param ymove: the y range of space in which the point can move
        :param color: the color as a tuple in (R, G, B) format
        """
        super().__init__()

        # "i" for integer
        self.x = Value("f", x)
        self.y = Value("f", y)

        self.xmove = xmove
        self.ymove = ymove

        # creating a unit vector makes sure that
        # all points travel at the same speed:
        # get random directions
        self.xdir = random.uniform(-1.0, 1.0)
        self.ydir = random.uniform(-1.0, 1.0)

        # calculate magnitude
        mag = math.sqrt(self.xdir**2 + self.ydir**2)

        # divide directions by magnitude
        # to get unit vector
        self.xdir /= mag
        self.ydir /= mag

        # multiply by speed to set speed
        self.xdir *= SPEED
        self.ydir *= SPEED

        self.color = color


    def run(self):
        """
        Manages the point's position

        :return: None
        """
        self.running = True

        # update frame every 1/24 seconds (24 fps)
        while self.running:
            time.sleep(1/24)

            self.x.value += self.xdir
            self.y.value += self.ydir

            # switch x/y direction when getting out of bounds
            if self.x.value <= 10 or self.x.value >= self.xmove:
                self.xdir *= -1

            if self.y.value <= 10 or self.y.value >= self.ymove:
                self.ydir *= -1

    def join(self, timeout=None):
        """
        Ends the point process

        :param timeout: the timeout
        :return: None
        """
        self.running = False


