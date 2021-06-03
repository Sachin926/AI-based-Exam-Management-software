import cv2 as cv
from PyQt5 import QtCore, QtGui, QtWidgets

class capture:

	def show_cam(self, cap, cam, roll):
		face_recognition = cv.CascadeClassifier("haarcascade_frontalface_default.xml")
		count = 0
		pic_count = 1
		while (1):
			_, self.frame = cap.read()
			self.frame = cv.resize(self.frame, (340, 340))
			try:
				face = face_recognition.detectMultiScale(self.frame, scaleFactor = 1.8, minNeighbors = 5)
				print (face)
			except:
				cv.imwrite("disable.jpg", self.frame)
				cam.setPixmap(QtGui.QPixmap("disable.jpg"))	
				cv.waitKey(1)
				

			try:
				cv.rectangle(img = self.frame, pt1 = (face[0][0], face[0][1]), 
					pt2 = (face[0][0] + face[0][2], face[0][1] + face[0][3]), color = (255, 0, 0))
				count = count + 1
				if (count % 10 == 0):
					image = self.frame[face[0][1] : (face[0][1] + face[0][3]),face[0][0] : (face[0][0] + face[0][2]), :]
					image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
					cv.imwrite(f"C://Attendance_System//face//{roll}//{pic_count}.jpg", image)
					pic_count = pic_count + 1
				cv.imwrite("disable.jpg", self.frame)
				cam.setPixmap(QtGui.QPixmap("disable.jpg"))	
				cv.waitKey(1)
			except:
				continue

			if (pic_count == 30):
				cap.release()
				break
