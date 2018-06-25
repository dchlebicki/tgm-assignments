import pygame
import math

# define some colors
# general colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# colors for the digital clock
D_DARK_TEXT = (32, 32, 32)
D_LIGHT_TEXT = (105, 105, 25)
D_BACKGROUND = (120, 120, 20)

# colors for the analog clock
A_DARK_GREY = (64, 64, 64)
A_SECONDS = (150, 0, 0)


# and some sizes
DIGITAL_SCREEN_SIZE = (572, 141)  # derived from size of rendered time text + 40px padding on each side
ANALOG_SCREEN_SIZE = (572, 572)
ANALOG_HANDS_LENGTH = (170, 260, 260)


class View:
    """
    View shows everything user can see on screen
    """
    def __init__(self):
        """
        Initializes the view
        """
        pygame.init()
        self.mode = "D" # "D" digital, "AT" analog with ticking second hand, "AC" analog with continuous second handpygame.font.init()
        self.screen = pygame.display.set_mode(DIGITAL_SCREEN_SIZE)

        pygame.font.init()
        # font from http://www.keshikan.net/fonts-e.html or https://github.com/keshikan/DSEG
        self.digitalFont = pygame.font.SysFont('DSEG7 Modern-Regular', 100)

        pygame.display.set_caption("Clock")

    def render(self, time_tuple):
        """
        Renders one of the clock types onto the screen, depending on set mode
        :param time_tuple: Tuple in (hours, minutes, second, microsecond) pattern, must be formatted, e.g. hour: "09" instead of "9"
        """
        self.screen.fill(WHITE)

        if self.mode == "D":
            self.screen = pygame.display.set_mode(DIGITAL_SCREEN_SIZE)
            time_formatted = time_tuple[0] + ":" + time_tuple[1] + ":" + time_tuple[2]

            time_now_background_surface = self.digitalFont.render("88:88:88", False, D_LIGHT_TEXT)
            time_now_main_surface = self.digitalFont.render(time_formatted, False, D_DARK_TEXT)

            pygame.draw.rect(self.screen, D_LIGHT_TEXT, (0, 0, DIGITAL_SCREEN_SIZE[0], DIGITAL_SCREEN_SIZE[1]), 0)
            pygame.draw.rect(self.screen, D_BACKGROUND,
                             (10, 10, DIGITAL_SCREEN_SIZE[0] - 2 * 10, DIGITAL_SCREEN_SIZE[1] - 2 * 10), 0)

            self.screen.blit(time_now_background_surface, (20, 20))
            self.screen.blit(time_now_main_surface, (20, 20))

        if self.mode in ["AT", "AC"]:
            self.screen = pygame.display.set_mode(ANALOG_SCREEN_SIZE)

            pygame.draw.rect(self.screen, A_DARK_GREY, (0, 0, ANALOG_SCREEN_SIZE[0], ANALOG_SCREEN_SIZE[1]), 0)
            pygame.draw.circle(self.screen, BLACK, (int(ANALOG_SCREEN_SIZE[0]/2), int(ANALOG_SCREEN_SIZE[0]/2)), int(ANALOG_SCREEN_SIZE[0]/2) - 7, 0)
            pygame.draw.circle(self.screen, WHITE, (int(ANALOG_SCREEN_SIZE[0]/2), int(ANALOG_SCREEN_SIZE[0]/2)), int(ANALOG_SCREEN_SIZE[0]/2) - 10, 0)
            pygame.draw.circle(self.screen, BLACK, (int(ANALOG_SCREEN_SIZE[0]/2), int(ANALOG_SCREEN_SIZE[0]/2)), 5, 0)

            hour = (int(time_tuple[0]) - 15) * 30
            minute = (int(time_tuple[1]) - 15) * 6
            if self.mode == "AT":
                second = (int(time_tuple[2]) - 15) * 6
            else:
                print(int(time_tuple[3]), time_tuple[3])
                second = (int(time_tuple[2]) + int(time_tuple[3])/1000000 - 15) * 6

            hourXPos = math.cos(math.radians(hour)) * ANALOG_HANDS_LENGTH[0]
            hourYPos = math.sin(math.radians(hour)) * ANALOG_HANDS_LENGTH[0]
            hourXPos += int(ANALOG_SCREEN_SIZE[0] / 2)
            hourYPos += int(ANALOG_SCREEN_SIZE[1] / 2)
            pygame.draw.line(self.screen, A_DARK_GREY, (int(ANALOG_SCREEN_SIZE[0] / 2), int(ANALOG_SCREEN_SIZE[0] / 2)),
                             (hourXPos, hourYPos), 5)

            minXPos = math.cos(math.radians(minute)) * ANALOG_HANDS_LENGTH[1]
            minYPos = math.sin(math.radians(minute)) * ANALOG_HANDS_LENGTH[1]
            minXPos += int(ANALOG_SCREEN_SIZE[0] / 2)
            minYPos += int(ANALOG_SCREEN_SIZE[1] / 2)
            pygame.draw.line(self.screen, A_DARK_GREY, (int(ANALOG_SCREEN_SIZE[0] / 2), int(ANALOG_SCREEN_SIZE[0] / 2)),
                             (minXPos, minYPos), 5)

            secXPos = math.cos(math.radians(second)) * ANALOG_HANDS_LENGTH[2]
            secYPos = math.sin(math.radians(second)) * ANALOG_HANDS_LENGTH[2]
            secXPos += int(ANALOG_SCREEN_SIZE[0] / 2)
            secYPos += int(ANALOG_SCREEN_SIZE[1] / 2)
            pygame.draw.line(self.screen, A_SECONDS, (int(ANALOG_SCREEN_SIZE[0] / 2), int(ANALOG_SCREEN_SIZE[0] / 2)),
                             (secXPos, secYPos), 3)

        pygame.display.flip()
