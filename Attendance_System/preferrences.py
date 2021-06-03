

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_settings(object):
    def setupUi(self, settings):
        settings.setObjectName("settings")
        settings.resize(330, 290)
        self.label = QtWidgets.QLabel(settings)
        self.label.setGeometry(QtCore.QRect(60, 80, 81, 21))
        self.label.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.seats = QtWidgets.QComboBox(settings)
        self.seats.setGeometry(QtCore.QRect(170, 80, 81, 21))
        self.seats.setCurrentText("")
        self.seats.setObjectName("seats")
        seat_list = list(range(0, 110, 10))
        for i in range(len(seat_list)):
            seat_list[i] = str(seat_list[i])
        lang = ["English", "Hindi", "Gujarati", "Tamil"]
        self.seats.addItems(seat_list)
        self.label_2 = QtWidgets.QLabel(settings)
        self.label_2.setGeometry(QtCore.QRect(60, 150, 81, 21))
        self.label_2.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.language = QtWidgets.QComboBox(settings)
        self.language.setGeometry(QtCore.QRect(170, 150, 81, 21))
        self.language.setCurrentText("")
        self.language.setObjectName("language")
        self.language.addItems(lang)
        self.save_settings = QtWidgets.QPushButton(settings, clicked = lambda : (self.save_preferrences(), settings.close()))
        self.save_settings.setGeometry(QtCore.QRect(120, 220, 75, 23))
        self.save_settings.setObjectName("save_settings")

        self.retranslateUi(settings)
        QtCore.QMetaObject.connectSlotsByName(settings)

    def save_preferrences(self):
        with open("settings.txt", "wt") as file:
            file.write(self.seats.currentText())
            file.write(",")
            file.write(self.language.currentText())



    def retranslateUi(self, settings):
        _translate = QtCore.QCoreApplication.translate
        settings.setWindowTitle(_translate("settings", "Settings"))
        self.label.setText(_translate("settings", "No. of Seats"))
        self.label_2.setText(_translate("settings", "Language"))
        self.save_settings.setText(_translate("settings", "Save"))

