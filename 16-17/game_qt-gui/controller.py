import sys
import random

from PySide.QtGui import *
from PySide.QtCore import *
from model import Model
from view import Ui_Form


class Controller(QWidget):
    """
    Controller part of the MVC pattern
    """
    def __init__(self, parent=None):
        """
        Initializes the form (view), model and some other variables.

        :param parent: the parent
        """
        super().__init__(parent)

        self.form = Ui_Form()
        self.form.setupUi(self)
        self.model = Model()
        self.buttons = []

        # list of unique random numbers
        self.sample = []

        self.set_up()

    def set_up(self):
        """
        Sets up the user interface buttons, labels, events, etc.

        :return: None
        """

        self.buttons = []

        self.reset()
        self.update_values()
        self.clear_grid()

        # generate the game buttons and connect the signal to a slot
        for c in range(self.model.cols):
            for r in range(self.model.rows):
                # create button and set name
                button = QPushButton(self)
                button.setObjectName("button_" + str(c) + "_" + str(r))
                button.setText("test")
                # connect clicked() signal to game_button_clicked slot
                QObject.connect(button, SIGNAL("clicked()"), self.game_button_clicked)
                # add button to gridLayout
                self.form.gridLayout.addWidget(button, r, c)
                self.buttons.append(button)

        self.sample = random.sample(range(1, self.model.cols * self.model.rows + 1), self.model.cols * self.model.rows)

        for b in self.buttons:
            b.setText(str(self.sample[self.buttons.index(b)]))

    def game_button_clicked(self):
        """
        Checks if the clicked button was clicked in the correct order and
        manipulates the GUI (disabling buttons or changing label text)

        :return: None
        """
        self.model.gesamt += 1
        sender = self.sender()

        # if button text equals number, assume click order was correct
        if self.model.current_number == int(sender.text()):
            sender.setDisabled(True)
            self.model.current_number += 1
            self.model.korrekt += 1
            self.model.offen -= 1
        # else, assume click order was incorrect
        else:
            self.model.falsch += 1

        self.update_values()

        if self.model.offen == 0:
            # removes all widgets from the gridlayout when game is over
            self.clear_grid()
            # and adds a "you won" label
            win_msg = QLabel(self)
            win_msg.setText("Sie haben gewonnen!")
            self.form.gridLayout.addWidget(win_msg)


    def reset(self):
        """
        (Re)sets all values in the model

        :return: None
        """
        # (re)sets all values in the model
        self.model.offen = self.model.cols * self.model.rows
        self.model.korrekt = 0
        self.model.falsch = 0
        self.model.gesamt = 0
        self.model.spiele += 1
        self.model.current_number = 1

    def update_values(self):
        """
        Sets the text of the _value_labels with the values of the model

        :return: None
        """
        self.form.offen_value_label.setText(str(self.model.offen))
        self.form.korrekt_value_label.setText(str(self.model.korrekt))
        self.form.falsch_value_label.setText(str(self.model.falsch))
        self.form.gesamt_value_label.setText(str(self.model.gesamt))
        self.form.spiele_value_label.setText(str(self.model.spiele))

    def clear_grid(self):
        """
        Removes all widgets of the gridlayout

        :return: None
        """
        for i in range(self.form.gridLayout.count()):
            self.form.gridLayout.itemAt(i).widget().close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    c = Controller()
    c.show()
    sys.exit(app.exec_())

