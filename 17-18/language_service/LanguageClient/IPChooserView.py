from ui.IPChooserGUI import Ui_Form
from PySide import QtGui

class View(QtGui.QWidget, Ui_Form):
    """
    View of the language client's IP address chooser, also works with hostnames.
    """
    def __init__(self):
        """
        Initializes the view
        """
        super().__init__()
        self.setupUi(self)