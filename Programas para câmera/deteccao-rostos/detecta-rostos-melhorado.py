import cv2

#image_path = 'rosto.jpg'
#image_path = 'formatura.jpg'
image_path = 'varios.png'
cascade_path = 'haarcascade_frontalface_default.xml' #modelo de reconhecimento

clf = cv2.CascadeClassifier(cascade_path) #cria o classificador

#cv2.namedWindow("Teste_reconhecimento_face")

img = cv2.imread(image_path) #Lê a imagem

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #Converter para grayscale / preto e branco

faces = clf.detectMultiScale(gray)
#faces = clf.detectMultiScale(gray,1.3,10)

for(x, y, w, h) in faces:
    img = cv2.rectangle(img, (x,y), (x+w, y+h), (255,255,0), 2)

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
