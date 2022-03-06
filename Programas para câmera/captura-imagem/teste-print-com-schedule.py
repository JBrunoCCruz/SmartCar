import schedule
import time
import cv2

cam = cv2.VideoCapture(0)

cv2.namedWindow("test")

img_counter = 0

def printAutomatico():
    global img_counter
    img_name = "opencv_frame_{}.png".format(img_counter)
    cv2.imwrite(img_name, frame)
    print("{} written!".format(img_name))
    img_counter += 1

#Seta o schedule para rodar a função a cada 30 segundos
schedule.every(5).seconds.do(printAutomatico)

while True:
    ret, frame = cam.read()
    cv2.imshow("test", frame)
    if not ret:
        break
    k = cv2.waitKey(1)

    if k%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
    
    schedule.run_pending()
    time.sleep(1)

cam.release()

cv2.destroyAllWindows()
