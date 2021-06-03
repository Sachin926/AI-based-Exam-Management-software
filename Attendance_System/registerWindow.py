
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_record(object):
    def setupUi(self, record):
        record.setObjectName("record")
        record.resize(787, 612)
        record.setStyleSheet("background-color: rgb(212, 255, 248);\n"
"selection-color: rgb(0, 0, 0);\n"
"selection-background-color: rgb(5, 170, 240);")
        self.centralwidget = QtWidgets.QWidget(record)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(30, 20, 721, 531))
        self.tabWidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.groupBox = QtWidgets.QGroupBox(self.tab)
        self.groupBox.setGeometry(QtCore.QRect(40, 20, 301, 191))
        self.groupBox.setObjectName("groupBox")
        self.formLayoutWidget = QtWidgets.QWidget(self.groupBox)
        self.formLayoutWidget.setGeometry(QtCore.QRect(20, 30, 261, 121))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.nameLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.nameLabel.setObjectName("nameLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.nameLabel)
        self.nameLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.nameLineEdit.setObjectName("nameLineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.nameLineEdit)
        self.rollNoLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.rollNoLabel.setObjectName("rollNoLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.rollNoLabel)
        self.rollNoLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.rollNoLineEdit.setObjectName("rollNoLineEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.rollNoLineEdit)
        self.branchLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.branchLabel.setObjectName("branchLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.branchLabel)
        self.branchLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.branchLineEdit.setObjectName("branchLineEdit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.branchLineEdit)
        self.semesterLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.semesterLabel.setObjectName("semesterLabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.semesterLabel)
        self.semesterLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.semesterLineEdit.setObjectName("semesterLineEdit")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.semesterLineEdit)
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_2.setGeometry(QtCore.QRect(360, 20, 301, 191))
        self.groupBox_2.setObjectName("groupBox_2")
        self.formLayoutWidget_2 = QtWidgets.QWidget(self.groupBox_2)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(20, 30, 251, 131))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.formLayout_2 = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setObjectName("formLayout_2")
        self.subject1Label = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.subject1Label.setObjectName("subject1Label")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.subject1Label)
        self.subject1LineEdit = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.subject1LineEdit.setObjectName("subject1LineEdit")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.subject1LineEdit)
        self.subject2Label = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.subject2Label.setObjectName("subject2Label")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.subject2Label)
        self.subject2LineEdit = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.subject2LineEdit.setObjectName("subject2LineEdit")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.subject2LineEdit)
        self.subject3Label = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.subject3Label.setObjectName("subject3Label")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.subject3Label)
        self.subject3LineEdit = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.subject3LineEdit.setObjectName("subject3LineEdit")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.subject3LineEdit)
        self.subject4Label = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.subject4Label.setObjectName("subject4Label")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.subject4Label)
        self.subject4LineEdit = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.subject4LineEdit.setObjectName("subject4LineEdit")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.subject4LineEdit)
        self.subject5Label = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.subject5Label.setObjectName("subject5Label")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.subject5Label)
        self.subject5LineEdit = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.subject5LineEdit.setObjectName("subject5LineEdit")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.subject5LineEdit)

        self.error_save_messsage = QtWidgets.QLabel(self.tab)
        self.error_save_messsage.setGeometry(50, 459, 481, 31)
        self.error_save_messsage.setStyleSheet("color: rgb(255, 0, 0);")
        self.error_save_messsage.setText("")

        self.groupBox_3 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_3.setGeometry(QtCore.QRect(50, 270, 611, 181))
        self.groupBox_3.setObjectName("groupBox_3")
        self.formLayoutWidget_3 = QtWidgets.QWidget(self.groupBox_3)
        self.formLayoutWidget_3.setGeometry(QtCore.QRect(20, 30, 571, 131))
        self.formLayoutWidget_3.setObjectName("formLayoutWidget_3")
        self.formLayout_3 = QtWidgets.QFormLayout(self.formLayoutWidget_3)
        self.formLayout_3.setContentsMargins(0, 0, 0, 0)
        self.formLayout_3.setObjectName("formLayout_3")
        self.phoneLabel = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.phoneLabel.setObjectName("phoneLabel")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.phoneLabel)
        self.subject1LineEdit_2 = QtWidgets.QLineEdit(self.formLayoutWidget_3)
        self.subject1LineEdit_2.setObjectName("subject1LineEdit_2")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.subject1LineEdit_2)
        self.address1Label = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.address1Label.setObjectName("address1Label")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.address1Label)
        self.subject2LineEdit_2 = QtWidgets.QLineEdit(self.formLayoutWidget_3)
        self.subject2LineEdit_2.setObjectName("subject2LineEdit_2")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.subject2LineEdit_2)
        self.address2Label = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.address2Label.setObjectName("address2Label")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.address2Label)
        self.subject3LineEdit_2 = QtWidgets.QLineEdit(self.formLayoutWidget_3)
        self.subject3LineEdit_2.setObjectName("subject3LineEdit_2")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.subject3LineEdit_2)
        self.stateLabel = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.stateLabel.setObjectName("stateLabel")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.stateLabel)
        self.subject4LineEdit_2 = QtWidgets.QLineEdit(self.formLayoutWidget_3)
        self.subject4LineEdit_2.setObjectName("subject4LineEdit_2")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.subject4LineEdit_2)
        self.districtLabel = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.districtLabel.setObjectName("districtLabel")
        self.formLayout_3.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.districtLabel)
        self.subject5LineEdit_2 = QtWidgets.QLineEdit(self.formLayoutWidget_3)
        self.subject5LineEdit_2.setObjectName("subject5LineEdit_2")
        self.formLayout_3.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.subject5LineEdit_2)
        self.detailsSave = QtWidgets.QPushButton(self.tab, clicked = lambda : self.save_details())
        self.detailsSave.setGeometry(QtCore.QRect(540, 460, 101, 31))
        self.detailsSave.setStyleSheet("background-color: rgb(230, 230, 230);")
        self.detailsSave.setObjectName("detailsSave")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.cam = QtWidgets.QLabel(self.tab_2)
        self.cam.setGeometry(QtCore.QRect(190, 20, 361, 351))
        self.cam.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.cam.setText("")
        self.cam.setPixmap(QtGui.QPixmap("cam.jpg"))
        self.cam.setAlignment(QtCore.Qt.AlignCenter)
        self.cam.setObjectName("cam")
        self.startCam = QtWidgets.QPushButton(self.tab_2, clicked = lambda : self.turn_on_webcam())
        self.startCam.setGeometry(QtCore.QRect(320, 430, 101, 31))
        self.startCam.setStyleSheet("background-color: rgb(230, 230, 230);")
        self.startCam.setObjectName("startCam")
        self.camMessage = QtWidgets.QLabel(self.tab_2)
        self.camMessage.setGeometry(QtCore.QRect(190, 390, 361, 31))
        self.camMessage.setAlignment(QtCore.Qt.AlignCenter)
        self.camMessage.setObjectName("camMessage")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.qrCode = QtWidgets.QLabel(self.tab_3)
        self.qrCode.setGeometry(QtCore.QRect(200, 40, 321, 301))
        self.qrCode.setFrameShape(QtWidgets.QFrame.Box)
        self.qrCode.setText("")
        self.qrCode.setPixmap(QtGui.QPixmap("qr_begin.png"))
        self.qrCode.setAlignment(QtCore.Qt.AlignCenter)
        self.qrCode.setObjectName("qrCode")
        self.codeGenerate = QtWidgets.QPushButton(self.tab_3, clicked = lambda : self.QR_code())
        self.codeGenerate.setGeometry(QtCore.QRect(310, 380, 101, 31))
        self.codeGenerate.setStyleSheet("background-color: rgb(230, 230, 230);")
        self.codeGenerate.setObjectName("codeGenerate")
        self.tabWidget.addTab(self.tab_3, "")
        record.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(record)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 787, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuExit = QtWidgets.QMenu(self.menubar)
        self.menuExit.setObjectName("menuExit")
        self.menuExit_2 = QtWidgets.QMenu(self.menubar)
        self.menuExit_2.setObjectName("menuExit_2")
        record.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(record)
        self.statusbar.setObjectName("statusbar")
        record.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(record)
        self.actionOpen.setObjectName("actionOpen")
        self.actionNew = QtWidgets.QAction(record)
        self.actionNew.setObjectName("actionNew")
        self.actionQuit = QtWidgets.QAction(record)
        self.actionQuit.setObjectName("actionQuit")
        self.actionRecord_DataBase = QtWidgets.QAction(record)
        self.actionRecord_DataBase.setObjectName("actionRecord_DataBase")
        self.actionAbout_Us_2 = QtWidgets.QAction(record)
        self.actionAbout_Us_2.setObjectName("actionAbout_Us_2")
        self.actionClose_Window = QtWidgets.QAction(record)
        self.actionClose_Window.setObjectName("actionClose_Window")
        self.actionClose_Window.triggered.connect(lambda : self.open_preferrences_window())
        self.actionExit = QtWidgets.QAction(record)
        self.actionExit.setObjectName("actionExit")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)
        self.menuHelp.addAction(self.actionRecord_DataBase)
        self.menuHelp.addAction(self.actionAbout_Us_2)
        self.menuExit.addAction(self.actionClose_Window)
        self.menuExit_2.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuExit.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menubar.addAction(self.menuExit_2.menuAction())

        import os
        self.actionOpen.triggered.connect(self.open_database)
        self.actionExit.triggered.connect(lambda : record.close())
        self.actionQuit.triggered.connect(lambda : record.close())
        self.actionRecord_DataBase.triggered.connect(lambda : os.startfile(r"C:\Attendance_System\help\record_database_help.txt"))
        self.actionAbout_Us_2.triggered.connect(lambda : os.startfile(r"C:\Attendance_System\help\aboutUs.txt"))
        self.actionNew.triggered.connect(lambda : (record.close(), self.new_reg_window()))

        self.retranslateUi(record)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(record)

    def open_preferrences_window(self):
        import preferrences
        self.set = QtWidgets.QDialog()
        self.pref_ui = preferrences.Ui_settings()
        self.pref_wind = self.pref_ui.setupUi(self.set)
        self.set.show()

    def new_reg_window(self):
        import registerWindow
        self.rec = QtWidgets.QMainWindow()
        self.rec_wind = registerWindow.Ui_record()
        self.rec_wind.setupUi(self.rec)
        self.rec.show()

    def open_database(self):
    	import os
    	os.startfile(r"C:\Attendance_System\details.csv")

    def QR_code(self):
    	import pyqrcode
    	import png
    	from pyqrcode import QRCode
    	import cv2 as cv
    	s = ""

    	for i in range(4):
    		s = s + self.details_database[i] + ","

    	image = pyqrcode.create(s)
    	image.png("test_QR.png", scale = 8)
    	image = cv.imread("test_QR.png")
    	image = cv.resize(image, (225, 225))
    	self.qrCode.setPixmap(QtGui.QPixmap("test_QR.png"))





    def turn_on_webcam(self):
        import cv2 as cv
        import face_data_acquisition

        self.cam_id = cv.VideoCapture(0)
        self.vid_cap = face_data_acquisition.capture()
        self.vid_cap.show_cam(self.cam_id, self.cam, self.details_database[1])

    

    def save_details(self):
        import csv
        import os
        self.flag = 1
        self.details_database = [self.nameLineEdit.text(), self.rollNoLineEdit.text(), self.branchLineEdit.text(),
        self.semesterLineEdit.text(), self.subject1LineEdit.text(), self.subject2LineEdit.text(), 
        self.subject3LineEdit.text(), self.subject4LineEdit.text(), self.subject5LineEdit.text(),
        self.subject1LineEdit_2.text(), self.subject2LineEdit_2.text(), self.subject3LineEdit_2.text(),
        self.subject4LineEdit_2.text(),self.subject5LineEdit_2.text()]

        if ("" in self.details_database):
            self.error_save_messsage.setText("*Incomplete Entries\n")
            self.flag = 0

        try:
            temp = int(self.details_database[1])
    
        except ValueError:
            self.error_save_messsage.setText(self.error_save_messsage.text() + "*Invalid Roll Number\n")
            self.flag = 0

        try:
            temp = int(self.details_database[9])
            
        except ValueError:
            self.error_save_messsage.setText(self.error_save_messsage.text() + "*Invalid Contact\n")
            self.flag = 0

        if (self.flag):
            with open(r"details.csv", "at") as file:
                write = csv.writer(file)
                write.writerow(self.details_database)

            self.error_save_messsage.setText("Data updated successfully") 

            os.mkdir(f"C://Attendance_System//face//{self.details_database[1]}") 


    def retranslateUi(self, record):
        _translate = QtCore.QCoreApplication.translate
        record.setWindowTitle(_translate("record", "MainWindow"))
        self.groupBox.setTitle(_translate("record", "Student Details"))
        self.nameLabel.setText(_translate("record", "Name"))
        self.rollNoLabel.setText(_translate("record", "Roll No."))
        self.branchLabel.setText(_translate("record", "Branch"))
        self.semesterLabel.setText(_translate("record", "Semester"))
        self.groupBox_2.setTitle(_translate("record", "Exam Details"))
        self.subject1Label.setText(_translate("record", "Subject1"))
        self.subject2Label.setText(_translate("record", "Subject2"))
        self.subject3Label.setText(_translate("record", "Subject3"))
        self.subject4Label.setText(_translate("record", "Subject4"))
        self.subject5Label.setText(_translate("record", "Subject5"))
        self.groupBox_3.setTitle(_translate("record", "Exam Details"))
        self.phoneLabel.setText(_translate("record", "Phone"))
        self.address1Label.setText(_translate("record", "Address1"))
        self.address2Label.setText(_translate("record", "Address2"))
        self.stateLabel.setText(_translate("record", "State"))
        self.districtLabel.setText(_translate("record", "District"))
        self.detailsSave.setText(_translate("record", "Save"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("record", "Details"))
        self.startCam.setText(_translate("record", "Start"))
        self.camMessage.setText(_translate("record", "Start the Webcam"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("record", "Capture Face"))
        self.codeGenerate.setText(_translate("record", "Generate"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("record", "Genrate QR"))
        self.menuFile.setTitle(_translate("record", "File"))
        self.menuHelp.setTitle(_translate("record", "Help"))
        self.menuExit.setTitle(_translate("record", "Settings"))
        self.menuExit_2.setTitle(_translate("record", "Exit"))
        self.actionOpen.setText(_translate("record", "Open"))
        self.actionNew.setText(_translate("record", "New"))
        self.actionQuit.setText(_translate("record", "Quit"))
        self.actionRecord_DataBase.setText(_translate("record", "Record DataBase"))
        self.actionAbout_Us_2.setText(_translate("record", "About Us"))
        self.actionClose_Window.setText(_translate("record", "Preferences"))
        self.actionExit.setText(_translate("record", "Exit"))
