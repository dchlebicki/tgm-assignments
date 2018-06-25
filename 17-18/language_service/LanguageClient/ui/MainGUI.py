# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\main.ui'
#
# Created: Thu Apr  5 22:26:43 2018
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(575, 466)
        Form.setMinimumSize(QtCore.QSize(392, 318))
        self.verticalLayout_2 = QtGui.QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtGui.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.inputField = QtGui.QTextEdit(Form)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.inputField.setFont(font)
        self.inputField.setObjectName("inputField")
        self.verticalLayout.addWidget(self.inputField)
        self.label_2 = QtGui.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.outputField = QtGui.QTextBrowser(Form)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.outputField.setFont(font)
        self.outputField.setObjectName("outputField")
        self.verticalLayout.addWidget(self.outputField)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.checkButton = QtGui.QPushButton(Form)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkButton.setFont(font)
        self.checkButton.setObjectName("checkButton")
        self.horizontalLayout.addWidget(self.checkButton)
        self.resetButton = QtGui.QPushButton(Form)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.resetButton.setFont(font)
        self.resetButton.setObjectName("resetButton")
        self.horizontalLayout.addWidget(self.resetButton)
        self.closeButton = QtGui.QPushButton(Form)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.closeButton.setFont(font)
        self.closeButton.setObjectName("closeButton")
        self.horizontalLayout.addWidget(self.closeButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Form", "Please provide your text here:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Form", "Here is your result:", None, QtGui.QApplication.UnicodeUTF8))
        self.outputField.setHtml(QtGui.QApplication.translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.checkButton.setText(QtGui.QApplication.translate("Form", "Check", None, QtGui.QApplication.UnicodeUTF8))
        self.resetButton.setText(QtGui.QApplication.translate("Form", "Reset", None, QtGui.QApplication.UnicodeUTF8))
        self.closeButton.setText(QtGui.QApplication.translate("Form", "Close", None, QtGui.QApplication.UnicodeUTF8))

