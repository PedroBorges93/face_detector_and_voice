import speech_recognition as sr
import pyttsx3
import cv2
import numpy as np
import testinho
import threading
import time

 
def speak(text):
        engine = pyttsx3.init() # object creation
        rate = engine.getProperty('rate')   # getting details of current speaking rate
        engine.setProperty('rate', 125)
        voices = engine.getProperty('voices')       #getting details of current voice
        engine.setProperty('voice', voices[1].id)      #changing index, changes voices. 1 for female
        engine.say(text)
        engine.runAndWait()
def camera():
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    cap = cv2.VideoCapture(0)
    while(True):
            ret, frame = cap.read()
            frame = cv2.flip(frame, 1)
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray,scaleFactor = 1.2, minNeighbors = 5)
            font = cv2.FONT_HERSHEY_SIMPLEX
            put_text_pos_ppl = (360,470)
            put_text_color = (18,0,255)
            for (x,y,w,h) in faces:
                testinho.draw_box(frame, x, y, w, h)
                roi_gray= gray[y:y+h, x:x+w]
                ppl_det = int(faces.shape[0])
                ppl_val = "{} Faces detected ".format(ppl_det)
                cv2.putText(frame,"Person detected",(x,y), font, 1,(255,0,0),4,cv2.LINE_AA)
                cv2.putText(frame, ppl_val,put_text_pos_ppl, font, 1 , put_text_color, 2, cv2.LINE_AA)
                #jatevi = False
                if ppl_det <=1:
                    #jatevi=True
                    #time.sleep(0.5)
                    speak("Hello Human ")        
            cv2.imshow('frame', frame)
            cv2.imshow('gray', gray)            
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    cap.release()
    cv2.destroyAllWindows()     


t1 = threading.Thread(target=camera, name="t1")

t2 = threading.Thread(target=speak, name="t2")   


t1.start()

t2.start()


