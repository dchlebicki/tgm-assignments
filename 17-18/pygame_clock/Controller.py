import pygame
import time
import math
from Model import *
from View import *

class Controller:
    """
    Controller gets data from model and input from user and puts it into the view.
    """
    def __init__(self):
        """
        Initializes the controller
        """
        self.model = Model()
        self.view = View()

        self.work()


    def work(self):
        """
        Method started during initialization, handles I/O
        """
        pygame.init()
        clock = pygame.time.Clock()

        done = False

        while not done:

            # Keystroke checking
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    done = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        done = True
                    if event.key == pygame.K_a:
                        self.view.mode = "AT"
                    if event.key == pygame.K_d:
                        self.view.mode = "D"
                    if event.key == pygame.K_p:
                        if self.view.mode == "AT":
                            self.view.mode = "AC"
                        else:
                            self.view.mode = "AT"

            clock.tick(60)

            self.view.render(self.model.get_time_tuple())

if __name__ == "__main__":
    controller = Controller()
