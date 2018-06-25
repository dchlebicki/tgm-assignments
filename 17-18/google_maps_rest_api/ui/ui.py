# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui.ui'
#
# Created: Thu Oct 19 23:57:58 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(700, 500)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(80)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(700, 500))
        Form.setMaximumSize(QtCore.QSize(700, 500))
        self.verticalLayout_2 = QtGui.QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.startLabel = QtGui.QLabel(Form)
        self.startLabel.setObjectName("startLabel")
        self.gridLayout.addWidget(self.startLabel, 0, 0, 1, 1)
        self.destinationAdressInput = QtGui.QLineEdit(Form)
        self.destinationAdressInput.setObjectName("destinationAdressInput")
        self.gridLayout.addWidget(self.destinationAdressInput, 1, 1, 1, 1)
        self.startAdressInput = QtGui.QLineEdit(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.startAdressInput.sizePolicy().hasHeightForWidth())
        self.startAdressInput.setSizePolicy(sizePolicy)
        self.startAdressInput.setObjectName("startAdressInput")
        self.gridLayout.addWidget(self.startAdressInput, 0, 1, 1, 1)
        self.destinationLabel = QtGui.QLabel(Form)
        self.destinationLabel.setObjectName("destinationLabel")
        self.gridLayout.addWidget(self.destinationLabel, 1, 0, 1, 1)
        self.submitButton = QtGui.QPushButton(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.submitButton.sizePolicy().hasHeightForWidth())
        self.submitButton.setSizePolicy(sizePolicy)
        self.submitButton.setObjectName("submitButton")
        self.gridLayout.addWidget(self.submitButton, 0, 2, 2, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.navigationTextbox = QtGui.QTextBrowser(Form)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.navigationTextbox.setFont(font)
        self.navigationTextbox.setObjectName("navigationTextbox")
        self.verticalLayout.addWidget(self.navigationTextbox)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.resetButton = QtGui.QPushButton(Form)
        self.resetButton.setObjectName("resetButton")
        self.horizontalLayout.addWidget(self.resetButton)
        self.closeButton = QtGui.QPushButton(Form)
        self.closeButton.setObjectName("closeButton")
        self.horizontalLayout.addWidget(self.closeButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.statusLabel = QtGui.QLabel(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.statusLabel.sizePolicy().hasHeightForWidth())
        self.statusLabel.setSizePolicy(sizePolicy)
        self.statusLabel.setMinimumSize(QtCore.QSize(120, 0))
        self.statusLabel.setObjectName("statusLabel")
        self.horizontalLayout_3.addWidget(self.statusLabel)
        self.JSONRadioButton = QtGui.QRadioButton(Form)
        self.JSONRadioButton.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.JSONRadioButton.sizePolicy().hasHeightForWidth())
        self.JSONRadioButton.setSizePolicy(sizePolicy)
        self.JSONRadioButton.setChecked(True)
        self.JSONRadioButton.setObjectName("JSONRadioButton")
        self.horizontalLayout_3.addWidget(self.JSONRadioButton)
        self.XMLRadioButton = QtGui.QRadioButton(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.XMLRadioButton.sizePolicy().hasHeightForWidth())
        self.XMLRadioButton.setSizePolicy(sizePolicy)
        self.XMLRadioButton.setObjectName("XMLRadioButton")
        self.horizontalLayout_3.addWidget(self.XMLRadioButton)
        self.horizontalLayout_2.addLayout(self.horizontalLayout_3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.startAdressInput, self.destinationAdressInput)
        Form.setTabOrder(self.destinationAdressInput, self.submitButton)
        Form.setTabOrder(self.submitButton, self.navigationTextbox)
        Form.setTabOrder(self.navigationTextbox, self.resetButton)
        Form.setTabOrder(self.resetButton, self.closeButton)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Google Maps Directions API Navigation", None, QtGui.QApplication.UnicodeUTF8))
        self.startLabel.setText(QtGui.QApplication.translate("Form", "Start:", None, QtGui.QApplication.UnicodeUTF8))
        self.destinationLabel.setText(QtGui.QApplication.translate("Form", "Destination: ", None, QtGui.QApplication.UnicodeUTF8))
        self.submitButton.setText(QtGui.QApplication.translate("Form", "Submit", None, QtGui.QApplication.UnicodeUTF8))
        self.resetButton.setText(QtGui.QApplication.translate("Form", "Reset", None, QtGui.QApplication.UnicodeUTF8))
        self.closeButton.setText(QtGui.QApplication.translate("Form", "Close", None, QtGui.QApplication.UnicodeUTF8))
        self.statusLabel.setText(QtGui.QApplication.translate("Form", "Status", None, QtGui.QApplication.UnicodeUTF8))
        self.JSONRadioButton.setText(QtGui.QApplication.translate("Form", "JSON", None, QtGui.QApplication.UnicodeUTF8))
        self.XMLRadioButton.setText(QtGui.QApplication.translate("Form", "XML", None, QtGui.QApplication.UnicodeUTF8))
