

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_login(object):
    def setupUi(self, login):
        login.setObjectName("login")
        login.resize(372, 326)
        self.lab = QtWidgets.QLabel(login)
        self.lab.setGeometry(QtCore.QRect(0, 20, 371, 41))
        self.lab.setStyleSheet("color: rgb(255, 0, 0);")
        self.lab.setAlignment(QtCore.Qt.AlignCenter)
        self.lab.setText("Admin Login")
        self.label = QtWidgets.QLabel(login)
        self.label.setGeometry(QtCore.QRect(50, 70, 71, 51))
        self.label.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(login)
        self.label_2.setGeometry(QtCore.QRect(50, 160, 71, 51))
        self.label_2.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.label_2.setObjectName("label_2")
        self.user_name = QtWidgets.QLineEdit(login, placeholderText = "Username")
        self.user_name.setGeometry(QtCore.QRect(130, 80, 181, 31))
        self.user_name.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.user_name.setObjectName("user_name")
        self.pwd = QtWidgets.QLineEdit(login, placeholderText = "Password")
        self.pwd.setGeometry(QtCore.QRect(130, 170, 181, 31))
        self.pwd.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.pwd.setObjectName("pwd")
        self.pwd.setEchoMode(QtWidgets.QLineEdit.Password)
        self.login_button = QtWidgets.QPushButton(login, clicked = lambda : self.check(login))
        self.login_button.setGeometry(QtCore.QRect(130, 240, 91, 31))
        self.login_button.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";")
        self.login_button.setObjectName("login_button")
        self.login_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.warn = QtWidgets.QLabel(login, text = "")

        self.count = 0;

        self.retranslateUi(login)
        QtCore.QMetaObject.connectSlotsByName(login)

    def check(self, login):
        u = self.user_name.text()
        p = self.pwd.text()
        self.count = self.count + 1

        if (u == "KNIT"):
            if (p == "1234"):
                login.close()
                self.register_window()
            else:
                self.lab.setText(f"Invalid Credentials!!!\n{5 - self.count} tries left")
        else:
            self.lab.setText(f"Invalid Credentials!!!\n{5 - self.count} tries left")

        if (self.count == 5):
            login.destroy()

    def register_window(self):
        import registerWindow
        self.rec = QtWidgets.QMainWindow()
        self.rec_wind = registerWindow.Ui_record()
        self.rec_wind.setupUi(self.rec)
        self.rec.show()



    def retranslateUi(self, login):
        _translate = QtCore.QCoreApplication.translate
        login.setWindowTitle(_translate("login", "Admin"))
        self.label.setText(_translate("login", "User ID"))
        self.label_2.setText(_translate("login", "Password"))
        self.login_button.setText(_translate("login", "Login"))
