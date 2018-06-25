from ui import Ui_Form
from PySide import QtGui

POINT_SIZE = 8

class View(Ui_Form, QtGui.QWidget):
    def __init__(self):
        """
        Initializes the view
        """
        super().__init__()
        self.setupUi(self)
        self.show()

        self.points = []

        self.painter = QtGui.QPainter()

    def paintEvent(self, event):
        """
        Paints the points.
        Called when repainting.

        :param event: the event
        :return: None
        """
        self.painter.begin(self)

        for i in self.points:
            self.painter.setBrush(QtGui.QColor(i.color[0], i.color[1], i.color[2]))
            self.painter.drawEllipse(i.x.value, i.y.value, POINT_SIZE, POINT_SIZE)

        self.painter.end()

    def closeEvent(self, event):
        """
        Ends all point processes

        :param event: the event
        :return: None
        """
        for i in self.points:
            i.join()
