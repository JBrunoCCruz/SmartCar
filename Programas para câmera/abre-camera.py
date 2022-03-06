Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:43:08) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import cv2
>>> 
>>> cap = cv2.VideoCapture(0)
>>> 
>>> while True:
	ret, frame = cap.read()

	
	cv2.imshow('Frame', frame)

	if cv2.waitKey(1) & 0xFF == ord('q'): break

cap.release()
cv2.destroyAllWindows()
