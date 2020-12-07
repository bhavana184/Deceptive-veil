import cv2
import numpy as np

cap=cv2.VideoCapture(0)
back=cv2.imread('./image.jpg')

while cap.isOpened():
	#take each frame
	ret,frame=cap.read()

	if ret:
		#how do we convert rgb to hsv
		hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
		#cv2.imshow("hsv",hsv)
		#how to get hsv value
		#lower:hue-10, 100, 100, higher:h+10, 255,255
		red=np.uint8([[[0,0,255]]]) #B:blue, g:green, r:red value
		hsv_red=cv2.cvtColor(red,cv2.COLOR_BGR2HSV)
		#print(hsv_red)

		#threshold the hsv value to get only red colors
		#l_red=np.array([0,100,100])
		#u_red=np.array([10,255,255])
		#l_red=np.array([161,155,84])
		#u_red=np.array([179,255,255])
		l_red=np.array([0,120,70])
		u_red=np.array([10,255,255])
		mask1=cv2.inRange(hsv,l_red,u_red)

		l_red=np.array([170,120,70])
		u_red=np.array([180,255,255])
		mask2=cv2.inRange(hsv,l_red,u_red)

		#mask=cv2.inRange(hsv,l_red,u_red)
		mask=mask1+mask2 #overloading + operator for bitwise or
		#any shade of redbetween 0 to 10 or 170 to 180 that wil be separated
		mask=cv2.morphologyEx(mask,cv2.MORPH_OPEN,np.ones((3,3),np.uint8),iterations=2)
		#noise removal
		mask=cv2.morphologyEx(mask,cv2.MORPH_DILATE,np.ones((3,3),np.uint8),iterations=1)
		mask=cv2.morphologyEx(mask,cv2.MORPH_CLOSE,np.ones((3,3),np.uint8),iterations=1)
		cv2.imshow('mask',mask)

		#part1:all things are read
		part1 = cv2.bitwise_and(back,back,mask=mask)
		cv2.imshow("part1",part1)

		mask=cv2.bitwise_not(mask)
		#part2: all things not read
		part2=cv2.bitwise_and(frame,frame,mask=mask)
		cv2.imshow("part2",part2)
		cv2.imshow("cloak",part1+part2)
		
		#https://docs.opencv.org/master/d9/d61/tutorial_py_morphological_ops.html
		#try morphology for better view

		if cv2.waitKey(5)==ord('q'):
			#save the image
			cv2.imwrite('frame.jpg', frame)
			break

cap.release()
cap.destroyAllWindows()