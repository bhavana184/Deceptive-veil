#1.get a background image
#2.select a colour
import cv2
cap=cv2.VideoCapture(0) #capture photo from my camera -0 is for camera

while cap.isOpened():
	ret, back = cap.read() #true if able to read the image else false
	if ret:
		#back is image what the camera is reading
		#ret is telling what you are reading is read or not
		cv2.imshow("image",back)
		if cv2.waitKey(5) == ord('q'):#press q to click the image
			#save the image
			cv2.imwrite('image.jpg', back)
			break
cap.release()
cv2.destroyAllWindows()
