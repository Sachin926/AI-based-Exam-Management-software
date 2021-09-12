from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_welcome(object):
    def setupUi(self, welcome):
        welcome.setObjectName("welcome")
        welcome.resize(400, 300)
        self.label = QtWidgets.QLabel(welcome)
        self.label.setGeometry(QtCore.QRect(0, 0, 391, 241))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("knit.png"))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.rec = QtWidgets.QPushButton(welcome, clicked = lambda : self.user_record(welcome))
        self.rec.setGeometry(QtCore.QRect(240, 250, 151, 41))
        self.rec.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.rec.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.rec.setObjectName("rec")
        self.reg = QtWidgets.QPushButton(welcome, clicked = lambda : self.admin_login(welcome))
        self.reg.setGeometry(QtCore.QRect(10, 250, 151, 41))
        self.reg.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.reg.setObjectName("reg")
        self.reg.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        self.retranslateUi(welcome)
        QtCore.QMetaObject.connectSlotsByName(welcome)

    def user_record(self, window):
        window.destroy()
        import record
        self.recWin = QtWidgets.QMainWindow()
        self.ui = record.Ui_recordWin()
        self.ui.setupUi(self.recWin)
        self.recWin.show()


    def admin_login(self, welcome):
        welcome.destroy()
        import log
        self.dialog_obj = QtWidgets.QDialog()
        self.login = log.Ui_login()
        self.login.setupUi(self.dialog_obj)
        self.dialog_obj.show()

    def retranslateUi(self, welcome):
        _translate = QtCore.QCoreApplication.translate
        welcome.setWindowTitle(_translate("welcome", "WELCOME"))
        self.rec.setText(_translate("welcome", "Record Attendance"))
        self.reg.setText(_translate("welcome", "Register"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    welcome = QtWidgets.QDialog()
    ui = Ui_welcome()
    ui.setupUi(welcome)
    welcome.show()
    sys.exit(app.exec_())

