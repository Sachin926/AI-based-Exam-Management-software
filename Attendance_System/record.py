
import os 
import cv2 as cv
import numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_recordWin(object):
    def setupUi(self, recordWin):
        self.count = 0
        recordWin.setObjectName("recordWin")
        recordWin.resize(800, 600)
        recordWin.setStyleSheet("background-color: rgb(226, 255, 252);\n"
"selection-color: rgb(139, 139, 139);")
        self.centralwidget = QtWidgets.QWidget(recordWin)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(180, 20, 481, 401))
        self.frame.setStyleSheet("background-color: rgb(93, 93, 93);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.cam = QtWidgets.QLabel(self.frame)
        self.cam.setGeometry(QtCore.QRect(10, 10, 461, 381))
        self.cam.setText("")
        self.cam.setPixmap(QtGui.QPixmap("capture.jpg"))
        self.cam.setAlignment(QtCore.Qt.AlignCenter)
        self.cam.setObjectName("cam")
        self.roll = QtWidgets.QLineEdit(self.centralwidget)
        self.roll.setGeometry(QtCore.QRect(330, 440, 171, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.roll.setFont(font)
        self.roll.setText("")
        self.roll.setAlignment(QtCore.Qt.AlignCenter)
        self.roll.setObjectName("roll")
        self.enter = QtWidgets.QPushButton(self.centralwidget, clicked = lambda : self.capture())
        self.enter.setGeometry(QtCore.QRect(360, 520, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.enter.setFont(font)
        self.enter.setStyleSheet("background-color: rgb(176, 176, 176);")
        self.enter.setObjectName("enter")
        self.enter.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        recordWin.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(recordWin)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        recordWin.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(recordWin)
        self.statusbar.setObjectName("statusbar")
        recordWin.setStatusBar(self.statusbar)
        self.actionNew = QtWidgets.QAction(recordWin)
        self.actionNew.setObjectName("actionNew")
        self.actionOpen = QtWidgets.QAction(recordWin)
        self.actionOpen.setObjectName("actionOpen")
        self.actionExit = QtWidgets.QAction(recordWin)
        self.actionExit.setObjectName("actionExit")
        self.actionHelp = QtWidgets.QAction(recordWin)
        self.actionHelp.setObjectName("actionHelp")
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuHelp.addAction(self.actionHelp)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(recordWin)
        QtCore.QMetaObject.connectSlotsByName(recordWin)

    def capture(self):
        import success
        import csv
        if (self.count != 0):
            self.cap.release()
            self.count = 0
            return
        self.count = self.count + 1
        rollNo = self.roll.text()
        self.cap = cv.VideoCapture(0)
        classifier = cv.CascadeClassifier(r"haarcascade_frontalface_default.xml")
        model = cv.face.LBPHFaceRecognizer_create()
        model.read(f"C://Attendance_System//face//{rollNo}//" + "testModel.yml")
        l = []
        with open("details.csv", "r") as file:
            read = csv.reader(file)
            for i in read:
                if (len(i) > 0):
                    if (i[1] == rollNo):
                        l = i
        while (1):
            try:
                _, frame = self.cap.read()
                face = classifier.detectMultiScale(frame, scaleFactor = 1.5, minNeighbors = 5)
                for (x, y, w, h) in face:
                    grey = frame[x : x + w, y : y + h, : ]
                    frame = cv.rectangle(frame, pt1 = (x, y), pt2 = (x + w, y + h), color = (0, 255, 0))
                    grey = cv.cvtColor(src = frame, code = cv.COLOR_BGR2GRAY)
                    res = model.predict(grey)
                    if (res[1] < 70):
                        self.cap.release()
                        self.successfull = QtWidgets.QDialog()
                        self.ui = success.Ui_Successfull()
                        self.ui.setupUi(self.successfull, l[0], l[1], l[3], l[2])
                        self.successfull.show()
                        return
                cv.imwrite("recordImg.jpg", frame)
                self.cam.setPixmap(QtGui.QPixmap("recordImg.jpg"))
                key = cv.waitKey(1)
            except:
                continue

    def retranslateUi(self, recordWin):
        _translate = QtCore.QCoreApplication.translate
        recordWin.setWindowTitle(_translate("recordWin", "MainWindow"))
        self.roll.setPlaceholderText(_translate("recordWin", "Roll no"))
        self.enter.setText(_translate("recordWin", "Enter"))
        self.menuFile.setTitle(_translate("recordWin", "File"))
        self.menuHelp.setTitle(_translate("recordWin", "Help"))
        self.actionNew.setText(_translate("recordWin", "New"))
        self.actionOpen.setText(_translate("recordWin", "Open"))
        self.actionExit.setText(_translate("recordWin", "Exit"))
        self.actionHelp.setText(_translate("recordWin", "Help"))


