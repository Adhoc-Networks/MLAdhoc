#!/usr/bin/python3

import cv2

cap=cv2.VideoCapture(0)
cascade=cv2.CascadeClassifier('face.xml')
#print(dir(cascade))

while cap.isOpened():
	status,frame=cap.read()
	gray_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	faces=cascade.detectMultiScale(gray_frame)
	#print(faces)
	#print ("Number of faces detected: " + str(faces.shape[0]))
	#print ("number of faces detected=" + str (faces.shape[0]))
	for  (x,y,w,h) in  faces:
		cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
		#  gray face image data
		gray_region_face=gray_frame[y:y+h,x:x+w]
		#  original face image data
		origin_region_face=frame[y:y+h,x:x+w]
		#print ('face detected')
		cv2.imwrite('facesss.jpg',origin_region_face)
		cv2.putText(frame, "Number of faces detected: " + str(faces.shape[0]), (0,frame.shape[0] -10), cv2.FONT_HERSHEY_TRIPLEX, 0.5, (255,255,255), 1)
		break
	#print('no faces')
	cv2.imshow('live',frame)

	if cv2.waitKey(2) &  0xFF == ord('q') :
		break
cv2.destroyAllWindows()
cap.release()
