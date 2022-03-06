import cv2
import numpy as np

#camera = cv2.VideoCapture(0)

video = cv2.VideoCapture("video-teste-pessoas.mp4")
full_body_cascade = cv2.CascadeClassifier('haarcascade_fullbody.xml')

#while True:
while (video.isOpened()):
    #_, frame = camera.read()
    _, frame = video.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow("frame", frame)

    bodies = full_body_cascade.detectMultiScale(gray, 1.3, 5)

    for(x, y, w, h) in bodies:
        cv2.rectangle(frame, (x,y), (x+w,y+h), (255,0,0), 2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]

    cv2.imshow("frame", frame)

    key = cv2.waitKey(1)

    if key == 27:
        break

#camera.release()
cv2.destroyAllWindows()
