import pyttsx3
import cv2
import pyautogui
import speech_recognition as sr

engine = pyttsx3.init('sapi5')
rate = engine.getProperty('rate')
engine.setProperty('rate',180)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.runAndWait()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def trafic_signal():
    cap = cv2.VideoCapture(0)
    count=0;
    while True:
        img = cap.read()[1]
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

        red_lower = (0, 50, 50)
        red_upper = (10, 255, 255)
        green_lower = (50, 50, 50)
        green_upper = (70, 255, 255)
        yellow_lower = (20, 50, 50)
        yellow_upper = (30, 255, 255)

        red_mask = cv2.inRange(hsv, red_lower, red_upper)
        green_mask = cv2.inRange(hsv, green_lower, green_upper)
        yellow_mask = cv2.inRange(hsv, yellow_lower, yellow_upper)

        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
        red_mask = cv2.morphologyEx(red_mask, cv2.MORPH_OPEN, kernel)
        green_mask = cv2.morphologyEx(green_mask, cv2.MORPH_OPEN, kernel)
        yellow_mask = cv2.morphologyEx(yellow_mask, cv2.MORPH_OPEN, kernel)


        red_contours, _ = cv2.findContours(red_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        green_contours, _ = cv2.findContours(green_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        yellow_contours, _ = cv2.findContours(yellow_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        light= " "
        for contour in red_contours:

            (x, y, w, h) = cv2.boundingRect(contour)
            cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)
            light="green light"
            cv2.putText(img, "green Light", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
        cv2.imshow('Video',img)
        cv2.waitKey(10)

 
        if "red light"==light:
            print("The signal is red,so you should stop and wait til the green signal.")
            speak("The signal is red,so you should stop and wait til the green signal.")
        else:
            print("The signal is green you can cross the road.")
            speak("The signal is green you can cross the road.")
        pyautogui.hotkey('win', 'down','down')
        return " "
