import torch
import cv2
import pyttsx3
import pandas
import psutil
import torchvision
import seaborn
import matplotlib
import pyautogui
from time import sleep
engine = pyttsx3.init('sapi5')
rate = engine.getProperty('rate')
engine.setProperty('rate',180)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.runAndWait()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def objectfinding(strings): 
            if strings == "stop":
                 return " "
            else:
                for _ in range(5):
                    #model = torch.hub.load('yolov5', 'yolov5n', source= 'local')
                    model=torch.hub.load('ultralytics/yolov5','yolov5n')
                    cap = cv2.VideoCapture(0)
                    img = cap.read()[1]
                    if img is None:
                        break
                    result = model(img)
                    df = result.pandas().xyxy[0]
                    for ind in df.index:
                        x1, y1 = int(df['xmin'][ind]), int(df['ymin'][ind])
                        x2, y2 = int(df['xmax'][ind]), int(df['ymax'][ind])
                    
                        conf = df['confidence'][ind]
                        label = df['name'][ind]
                        print(label)
                        speak(label)
                        text = label + ' ' + str(conf.round(decimals= 2))
                        cv2.rectangle(img, (x1, y1), (x2, y2), (255, 255, 0), 2)
                        cv2.putText(img, text, (x1, y1 - 5), cv2.FONT_HERSHEY_PLAIN, 2, (255, 255, 0), 2)

                    cv2.imshow('Video',img)
                    cv2.waitKey(20)
                return " "
                   

    