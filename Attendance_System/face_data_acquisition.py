import cv2 as cv
from PyQt5 import QtCore, QtGui, QtWidgets

class capture:

	def show_cam(self, cap, cam, roll):
		face_recognition = cv.CascadeClassifier("haarcascade_frontalface_default.xml")
		count = 0
		while (1):
			_, self.frame = cap.read()
			self.frame = cv.resize(self.frame, (340, 340))
			try:
				face = face_recognition.detectMultiScale(self.frame, scaleFactor = 1.8, minNeighbors = 5)
			except:
				cv.imwrite("disable.jpg", self.frame)
				cam.setPixmap(QtGui.QPixmap("disable.jpg"))	
				cv.waitKey(1)
			try:
				cv.rectangle(img = self.frame, pt1 = (face[0][0], face[0][1]), 
					pt2 = (face[0][0] + face[0][2], face[0][1] + face[0][3]), color = (255, 0, 0))
				count = count + 1
				if (count == 100):
					count = 0
					cap.release()
					break
				image = self.frame[face[0][1] : (face[0][1] + face[0][3]),face[0][0] : (face[0][0] + face[0][2]), :]
				image = image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
				cv.resize(image, (140, 140))
				cv.imwrite(f"C://Attendance_System//face//{roll}//{count}.jpg", image)
				cv.imwrite("disable.jpg", self.frame)
				cam.setPixmap(QtGui.QPixmap("disable.jpg"))	
				cv.waitKey(1)
			except:
				continue
		self.train(roll)

	def train(self, roll):
		import numpy as np
		import os
		dataPath = f"C://Attendance_System//face//{roll}"
		l = os.listdir(dataPath)
		listDir = []
		for i in l:
			if (i.endswith("jpg")):   #to prevent thumbs.db file from getting considered
				listDir.append(os.path.join(dataPath, i))
		train, label = [], []
		for i in range (len(listDir)):
			image = cv.imread(listDir[i], 0)
			image = np.asarray(image, dtype = np.uint8)
			train.append(image)
			label.append(i)
		label = np.asarray(label, dtype = np.int32)
		global model
		model = cv.face.LBPHFaceRecognizer_create()
		model.train(np.asarray(train, dtype = np.uint8), label)
		model.save(f"C://Attendance_System//face//{roll}//" + "testModel.yml")
		print ("Training Complete")

