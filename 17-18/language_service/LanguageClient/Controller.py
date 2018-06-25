import MainView, IPChooserView, Model
from PySide.QtGui import *
from PySide.QtCore import *
import sys


class Controller:
    """
    Controller handles I/O and the communication between model and view
    """
    def __init__(self):
        """
        Sets everything up.
        """

        # initialize some objects
        self.IPChooserView = IPChooserView.View()
        self.mainView = MainView.View()
        self.model = None

        # set up the IP chooser
        # in case IP/Port is already defined in sys.argv, set as value of input fields
        self.IPChooserView.show()
        if len(sys.argv) == 3:
            self.IPChooserView.IPAdressInput.setText(sys.argv[1])
            self.IPChooserView.portInput.setText(sys.argv[2])

        # bind ip chooser widget's buttons to methods
        QObject.connect(self.IPChooserView.connectButton, SIGNAL("clicked()"), self.connect)
        QObject.connect(self.IPChooserView.closeButton, SIGNAL("clicked()"), self.close)
        # bind main widget's buttons to methods
        QObject.connect(self.mainView.checkButton, SIGNAL("clicked()"), self.check)
        QObject.connect(self.mainView.resetButton, SIGNAL("clicked()"), self.reset)
        QObject.connect(self.mainView.closeButton, SIGNAL("clicked()"), self.close)

    def connect(self):
        """
        Sets up the connection to the language service
        """
        # initializes the model with IP and port from ip address chooser
        self.model = Model.Model(self.IPChooserView.IPAdressInput.text(), self.IPChooserView.portInput.text())
        # also hides ip chooser and shows main window
        self.IPChooserView.hide()
        self.mainView.show()

    def check(self):
        """
        Puts the result of the language service response into the GUI
        """
        response = self.model.detectLanguage(self.mainView.inputField.toPlainText())

        if response == "error":
            self.mainView.outputField.setHtml("No connection could be established to the language service, "
                                              "are you sure the IP address and/or port is correct?")
        else:
            reliable = "yes" if response["reliable"] else "no"
            self.mainView.outputField.setHtml("Reliable: <b>%s</b><br/>"
                                              "Language: <b>%s</b><br/>"
                                              "Probability: <b>%i%%</b>"
                                              % (reliable, response["language"], response["prob"]))

    def reset(self):
        """
        Resets all fields in the GUI
        """
        self.mainView.inputField.clear()
        self.mainView.outputField.clear()

    def close(self):
        """
        Closes the application
        """
        app.exit()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    c = Controller()
    sys.exit(app.exec_())
