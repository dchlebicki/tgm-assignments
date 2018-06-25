# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\ip_chooser.ui'
#
# Created: Thu Apr  5 22:27:12 2018
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(242, 100)
        Form.setMinimumSize(QtCore.QSize(242, 100))
        Form.setMaximumSize(QtCore.QSize(242, 100))
        self.verticalLayout_2 = QtGui.QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtGui.QLabel(Form)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.IPAdressInput = QtGui.QLineEdit(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.IPAdressInput.sizePolicy().hasHeightForWidth())
        self.IPAdressInput.setSizePolicy(sizePolicy)
        self.IPAdressInput.setObjectName("IPAdressInput")
        self.horizontalLayout.addWidget(self.IPAdressInput)
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.portInput = QtGui.QLineEdit(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.portInput.sizePolicy().hasHeightForWidth())
        self.portInput.setSizePolicy(sizePolicy)
        self.portInput.setObjectName("portInput")
        self.horizontalLayout.addWidget(self.portInput)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.connectButton = QtGui.QPushButton(Form)
        self.connectButton.setObjectName("connectButton")
        self.horizontalLayout_2.addWidget(self.connectButton)
        self.closeButton = QtGui.QPushButton(Form)
        self.closeButton.setObjectName("closeButton")
        self.horizontalLayout_2.addWidget(self.closeButton)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.statusLabel = QtGui.QLabel(Form)
        self.statusLabel.setObjectName("statusLabel")
        self.verticalLayout.addWidget(self.statusLabel)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Form", "IP:Port", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Form", ":", None, QtGui.QApplication.UnicodeUTF8))
        self.connectButton.setText(QtGui.QApplication.translate("Form", "Connect", None, QtGui.QApplication.UnicodeUTF8))
        self.closeButton.setText(QtGui.QApplication.translate("Form", "Close", None, QtGui.QApplication.UnicodeUTF8))
        self.statusLabel.setText(QtGui.QApplication.translate("Form", "Insert your preferred IP address and port.", None, QtGui.QApplication.UnicodeUTF8))

