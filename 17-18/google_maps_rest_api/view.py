from ui import Ui_Form
from PySide import QtGui

class View(Ui_Form, QtGui.QWidget):
    """
    View part of the MVC pattern, creates and initializes the window and form
    """
    def __init__(self):
        """
        Initializes the window and form
        """
        super().__init__()
        self.setupUi(self)
        self.show()

        self.statusLabel.setText("")
