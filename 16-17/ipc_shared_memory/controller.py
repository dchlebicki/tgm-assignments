from view import View
from PySide.QtGui import *
from PySide.QtCore import *
from point import Point
import sys
import random

class Controller():
    def __init__(self):
        """
        Initializes the controller
        """
        self.view = View()

        QObject.connect(self.view.new_point_button, SIGNAL("clicked()"), self.create_point)
        QObject.connect(self.view.delete_last_point_button, SIGNAL("clicked()"), self.remove_last_point)

    def create_point(self):
        """
        Creates a new random point in the field

        :return: None
        """
        p = Point(random.randint(10, self.view.draw.size().width()),
                  random.randint(10, self.view.draw.size().height()),
                  self.view.draw.size().width(),
                  self.view.draw.size().height(),
                  (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
                  )

        p.start()
        self.view.points.append(p)

    def remove_last_point(self):
        """
        Removes the last added point

        :return: None
        """
        self.view.points[-1].join()
        self.view.points.pop(-1)

    def update(self):
        """
        Updates the point positions

        :return: None
        """
        self.view.repaint()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    c = Controller()

    while c.view.isVisible():
        c.update()
        app.processEvents()

    sys.exit()
