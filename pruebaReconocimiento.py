import cv2
import numpy

#Cargamos el archivo clasificador
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')



while(True):
    ret, frame = cap.read()
    #Convertimos la imagen a escala de grises
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #Activamos el detector
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    #Iniciamos un bucle for para que cada cara que detecte,
    #nos proporcione coordenadas y dibujemos rectangulos
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)

    cv2.imshow('Haar', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'): # Indicamos que al pulsar "q" el programa se cierre
        break

cap.release()
cv2.destroyAllWindows()