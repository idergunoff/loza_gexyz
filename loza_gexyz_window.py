# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\USER\PycharmProjects\loza_gexyz\loza_gexyz_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_loza_gexyz(object):
    def setupUi(self, loza_gexyz):
        loza_gexyz.setObjectName("loza_gexyz")
        loza_gexyz.resize(505, 137)
        self.centralwidget = QtWidgets.QWidget(loza_gexyz)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.lineEdit_direct = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_direct.setObjectName("lineEdit_direct")
        self.gridLayout_2.addWidget(self.lineEdit_direct, 1, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_file = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_file.setObjectName("pushButton_file")
        self.gridLayout.addWidget(self.pushButton_file, 0, 0, 1, 1)
        self.pushButton_gexyz = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_gexyz.setObjectName("pushButton_gexyz")
        self.gridLayout.addWidget(self.pushButton_gexyz, 0, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout_2.addWidget(self.progressBar, 2, 0, 1, 1)
        loza_gexyz.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(loza_gexyz)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 505, 21))
        self.menubar.setObjectName("menubar")
        loza_gexyz.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(loza_gexyz)
        self.statusbar.setObjectName("statusbar")
        loza_gexyz.setStatusBar(self.statusbar)

        self.retranslateUi(loza_gexyz)
        QtCore.QMetaObject.connectSlotsByName(loza_gexyz)

    def retranslateUi(self, loza_gexyz):
        _translate = QtCore.QCoreApplication.translate
        loza_gexyz.setWindowTitle(_translate("loza_gexyz", "Loza gexyz"))
        self.pushButton_file.setText(_translate("loza_gexyz", "?????????????? ???????? ????????????????"))
        self.pushButton_gexyz.setText(_translate("loza_gexyz", "?????????????? ?????????? gexyz"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    loza_gexyz = QtWidgets.QMainWindow()
    ui = Ui_loza_gexyz()
    ui.setupUi(loza_gexyz)
    loza_gexyz.show()
    sys.exit(app.exec_())
