from view import View
from model import Model
from PySide.QtGui import *
from PySide.QtCore import *
import sys

class Controller(QWidget):
    """
    Controller part of the MVC pattern, handles the communication between model and view layers.
    """
    def __init__(self):
        """
        Initializes the controller and sets everything up.
        """
        self.view = View()
        self.model = Model()

        QObject.connect(self.view.submitButton, SIGNAL("clicked()"), self.submit)
        QObject.connect(self.view.resetButton, SIGNAL("clicked()"), self.reset)
        QObject.connect(self.view.closeButton, SIGNAL("clicked()"), self.close)

    def submit(self):
        """
        Calls the Google Maps REST API via a function in the model to find a route to the specified destination and
        shows the returned values in the GUI.

        :return: None
        """
        origin = self.view.startAdressInput.text()
        destination = self.view.destinationAdressInput.text()

        if self.view.XMLRadioButton.isChecked():
            file_format = "xml"
        else:
            file_format = "json"

        (route_description, status) = self.model.requestNavigation(origin, destination, file_format)

        self.view.navigationTextbox.insertHtml(route_description)
        self.view.statusLabel.setText(status)


    def reset(self):
        """
        Resets all fields in the GUI

        :return: None
        """
        self.view.startAdressInput.setText("")
        self.view.destinationAdressInput.setText("")
        self.view.navigationTextbox.setText("")
        self.view.statusLabel.setText("")

    def close(self):
        """
        Closes the app.

        :return: None
        """
        app.exit()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    c = Controller()
    sys.exit(app.exec_())
