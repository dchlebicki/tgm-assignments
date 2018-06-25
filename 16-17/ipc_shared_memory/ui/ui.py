# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui.ui'
#
# Created: Sat Dec 17 23:51:28 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(506, 391)
        Form.setMinimumSize(QtCore.QSize(506, 391))
        Form.setMaximumSize(QtCore.QSize(506, 391))
        self.verticalLayout_2 = QtGui.QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.draw = QtGui.QWidget(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.draw.sizePolicy().hasHeightForWidth())
        self.draw.setSizePolicy(sizePolicy)
        self.draw.setObjectName("draw")
        self.verticalLayout.addWidget(self.draw)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.new_point_button = QtGui.QPushButton(Form)
        self.new_point_button.setObjectName("new_point_button")
        self.horizontalLayout.addWidget(self.new_point_button)
        self.delete_last_point_button = QtGui.QPushButton(Form)
        self.delete_last_point_button.setObjectName("delete_last_point_button")
        self.horizontalLayout.addWidget(self.delete_last_point_button)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "IPC Points", None, QtGui.QApplication.UnicodeUTF8))
        self.new_point_button.setText(QtGui.QApplication.translate("Form", "New Point", None, QtGui.QApplication.UnicodeUTF8))
        self.delete_last_point_button.setText(QtGui.QApplication.translate("Form", "Remove Last Point", None, QtGui.QApplication.UnicodeUTF8))

