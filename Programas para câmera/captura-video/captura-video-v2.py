import numpy as np
import os
import cv2

filename = 'video_0.avi'
frames_per_second = 20.0
res = '480p'

def change_res(cap, width, height):
    cap.set(3, width)
    cap.set(4, height)

STD_DIMENSIONS = {
    "480p": (640, 480),
    "720p": (1280, 720),
    "1080p": (1920, 1080),
    "4k": (3840, 2160),
}

def get_dims(cap, res='1080p'):
    width, height = STD_DIMENSIONS["480p"]
    if res in STD_DIMENSIONS:
        width, height = STD_DIMENSIONS[res]

    change_res(cap, width,  height)
    return width, height

VIDEO_TYPE = {
    'avi': cv2.VideoWriter_fourcc(*'XVID'),
    'mp4': cv2.VideoWriter_fourcc(*'XVID'),
}

def get_video_type(filename):
    filename, ext = os.path.splitext(filename)
    if ext in VIDEO_TYPE:
        return VIDEO_TYPE[ext]
    return VIDEO_TYPE['avi']

cap = cv2.VideoCapture(0)
#out = cv2.VideoWriter(filename, get_video_type(filename), frames_per_second, get_dims(cap, res))

record = False
video_counter = 1

while True:
    ret, frame = cap.read()
    cv2.imshow('frame', frame)

    if not ret:
        break

    if record == True:
        out.write(frame)

    k = cv2.waitKey(1)
    
    if k%256 == 81 or k%256 == 113: #pressionou letra 'Q' ou 'q' para sair do programa
        break

    elif k%256 == 80 or k%256 == 112: #pressionou letra 'P' ou 'p' para play/stop
        record = (True if record == False else False)
        if record == True:
            filename = "video_{}.avi".format(video_counter)
            print("{} gravando...".format(filename))
            video_counter += 1
            out = cv2.VideoWriter(filename, get_video_type(filename), frames_per_second, get_dims(cap, res))
        else:
            print("{} finalizado.".format(filename))
            out.release()

cap.release()
#out.release()
cv2.destroyAllWindows()
