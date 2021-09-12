
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Successfull(object):
    def setupUi(self, Successfull, name, roll, semNo, bran):
        Successfull.setObjectName("Successfull")
        Successfull.resize(400, 300)
        self.groupBox = QtWidgets.QGroupBox(Successfull)
        self.groupBox.setGeometry(QtCore.QRect(30, 20, 341, 241))
        self.groupBox.setObjectName("groupBox")
        self.system = QtWidgets.QLineEdit(self.groupBox)
        self.system.setGeometry(QtCore.QRect(130, 30, 171, 21))
        self.system.setReadOnly(True)
        self.system.setObjectName("system")
        self.name = QtWidgets.QLineEdit(self.groupBox)
        self.name.setGeometry(QtCore.QRect(130, 70, 171, 21))
        self.name.setReadOnly(True)
        self.name.setObjectName("name")
        self.rollNo = QtWidgets.QLineEdit(self.groupBox)
        self.rollNo.setGeometry(QtCore.QRect(130, 110, 171, 21))
        self.rollNo.setReadOnly(True)
        self.rollNo.setObjectName("rollNo")
        self.branch = QtWidgets.QLineEdit(self.groupBox)
        self.branch.setGeometry(QtCore.QRect(130, 150, 171, 21))
        self.branch.setReadOnly(True)
        self.branch.setObjectName("branch")
        self.sem = QtWidgets.QLineEdit(self.groupBox)
        self.sem.setGeometry(QtCore.QRect(130, 190, 171, 21))
        self.sem.setReadOnly(True)
        self.sem.setObjectName("sem")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(20, 30, 101, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(20, 70, 101, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(20, 110, 101, 21))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(20, 150, 101, 21))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(20, 190, 101, 21))
        self.label_5.setObjectName("label_5")

        self.name.setText(name)
        self.rollNo.setText(roll)
        self.branch.setText(bran)
        self.sem.setText(semNo)
        sys = self.getSystemNo()
        self.system.setText(sys)


        self.retranslateUi(Successfull)
        QtCore.QMetaObject.connectSlotsByName(Successfull)

    def getSystemNo(self):
        import random
        with open("alloted.txt", "rt") as file:
            l = file.readlines()
        l = l.split(",")

        index = random.randint(0, len(l) - 1)
        sys = l[index]
        with open("alloted.txt", "wt") as file:
            str = ""
            for i in range (0, len(l) - 1):
                if (i == index):
                    continue
                else:
                    str = str + l[i] + ","
            file.writelines(str)

        return sys


    def retranslateUi(self, Successfull):
        _translate = QtCore.QCoreApplication.translate
        Successfull.setWindowTitle(_translate("Successfull", "Dialog"))
        self.groupBox.setTitle(_translate("Successfull", "Details"))
        self.label.setText(_translate("Successfull", "System No."))
        self.label_2.setText(_translate("Successfull", "Name"))
        self.label_3.setText(_translate("Successfull", "Roll no."))
        self.label_4.setText(_translate("Successfull", "Branch"))
        self.label_5.setText(_translate("Successfull", "Semester"))
