# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\python\test_project\new_table_example.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(820, 516)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.exportbtn = QtWidgets.QPushButton(Form)
        self.exportbtn.setObjectName("exportbtn")
        self.horizontalLayout.addWidget(self.exportbtn)
        self.addbtn = QtWidgets.QPushButton(Form)
        self.addbtn.setObjectName("addbtn")
        self.horizontalLayout.addWidget(self.addbtn)
        self.deletebtn = QtWidgets.QPushButton(Form)
        self.deletebtn.setObjectName("deletebtn")
        self.horizontalLayout.addWidget(self.deletebtn)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.tableView = QtWidgets.QTableView(Form)
        self.tableView.setObjectName("tableView")
        self.verticalLayout.addWidget(self.tableView)
        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.exportbtn.setText(_translate("Form", "export"))
        self.addbtn.setText(_translate("Form", "add"))
        self.deletebtn.setText(_translate("Form", "delete"))
