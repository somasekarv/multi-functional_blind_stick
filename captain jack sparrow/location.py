import pyttsx3
import speech_recognition as sr
import json
import pyautogui
import torch
import cv2
from selenium import webdriver
from cabe_booking import*
from time import sleep


engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', 150)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.runAndWait()

def takeCommand():
    recog = sr.Recognizer()

    with sr.Microphone() as source:
        recog.energy_threshold = 1000
        recog.adjust_for_ambient_noise(source, 1.2)
        print("Listening....")
        audio = recog.listen(source)

    try:
        print("Recognizing...")
        query = recog.recognize_google(audio)
        print(f"User said: {query}\n")

    except:
        print("Unable to Recognize your voice.")
        speak("Unable to Recognize your voice.")
        return "  "

    return query

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

recog = sr.Recognizer()

def ob_ject():
    for _ in range(3):
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
                   

def curr_loc():
    areas = "city: Salem,street: Junction Main Road,Area: Tamilnadu,country: India."
    return areas

def loc_tofind(query):
        print("It will take few minutes,please wait.")
        speak("It will take few minutes,please wait.")
        drive = webdriver.Chrome(executable_path=r'#####################chrome drive path############')
        #drive.minimize_window()
        drive.get(url='https://www.google.com/maps/@10.8211663,78.2897649,7z?authuser=0')
        sleep(8)
        drive.find_element('xpath','//*[@id="hArJGc"]').click()
        sleep(3)
        current = curr_loc()
        drive.find_element('xpath','//*[@id="sb_ifc51"]/input').send_keys(current)
        sleep(2)
        drive.find_element('xpath','//*[@id="sb_ifc52"]/input').send_keys(query)
        sleep(2)
        drive.find_element('xpath','//*[@id="directions-searchbox-1"]/button[1]').click()
        sleep(6)
        print("finding the best root to travel.")
        speak("finding the best root to travel.")
        drive.find_element('xpath','//*[@id="omnibox-directions"]/div/div[2]/div/div/div/div[2]/button').click()
        sleep(5)
        root = drive.find_element('xpath','//*[@id="section-directions-trip-0"]/div[1]/div[1]/div[1]/div[2]/div')
        time = drive.find_element('xpath','//*[@id="section-directions-trip-0"]/div[1]/div[1]/div[1]/div[1]/span[1]')
        print(f"from your location to {query} the total kilometer is : {root.text}, and it will take time to travel : {time.text}")
        speak(f"from your location to {query} the total kilometer is : {root.text}, and it will take time to travel : {time.text}")
        sleep(3)
        print(f"The {root.text} from your destination.can i book a cab for you?")
        speak(f"The {root.text} from your destination.can i book a cab for you?")
        booking = takeCommand().lower()
        if "yes" in booking or "book the cab" in booking or "okay book" in booking or "ok book the cab" in booking:
            print("finding the cab.")
            speak("finding the cab.")
            finding = cab(query)
            print(finding)
            return " "
        else:
            print("okay i think you will decided to walk?")
            speak("okay i think you will decided to walk?")
            decision = takeCommand().lower()
            if "yes" in decision or "yes i decide to walk" in decision or "decide walk" in decision or "decided to walk" in decision or "decide to walk" in decision:
                print("can i help you to reach the destination.")
                speak("can i help you to reach the destination.")
                help = takeCommand().lower()
                if "sure" in help or "yes" in help or "definately" in help or "fine help me" in help or "fine help" in help:   
                    print("okay i will help you to reach the destination.")
                    speak("okay i will help you to reach the destination.")
                    print("The object also on to reach your desination without any disturbances.")
                    speak("The object also on to reach your desination without any disturbances.")
                    drive.find_element('xpath','//*[@id="omnibox-directions"]/div/div[2]/div/div/div/div[4]/button').click()
                    sleep(2)
                    drive.find_element('xpath','//*[@id="section-directions-trip-details-msg-0"]').click()
                    sleep(2)
                    speaker1 = drive.find_element('xpath','//*[@id="group_0_0"]/div/div/div[1]/div/div[1]')
                    print(f"{speaker1.text}")
                    speak(f"{speaker1.text}")
                    meter1 = drive.find_element('xpath','//*[@id="group_0_0"]/div/div/div[1]/div/div[3]/div[2]')
                    print(f"just {meter1.text} meters.")
                    speak(f"just {meter1.text} meters.")
                    sleep(3)
                    print("keep walking...")
                    speak("keep walking...")
                    ob_ject()
                    sleep(30)
                    speaker2 = drive.find_element('xpath','//*[@id="group_0_0"]/div/div/div[2]/div/div[1]')
                    print(f"{speaker2.text}")
                    speak(f"{speaker2.text}")
                    meter2 = drive.find_element('xpath','//*[@id="group_0_0"]/div/div/div[2]/div/div[3]/div[2]')
                    print(f"just {meter2.text} meters.")
                    speak(f"just {meter2.text} meters.")
                    sleep(3)
                    print("keep walking..")
                    speak("keep walking..")
                    ob_ject()
                    sleep(30)
                    speaker3 = drive.find_element('xpath','//*[@id="group_0_0"]/div/div/div[3]/div/div[1]')
                    print(f"{speaker3.text}")
                    speak(f"{speaker3.text}")
                    meter3 = drive.find_element('xpath','//*[@id="group_0_0"]/div/div/div[3]/div/div[3]/div[2]')
                    print(f"just {meter3.text} meters.")
                    speak(f"just {meter3.text} meters.")
                    sleep(3)
                    print("keep walking..")
                    speak("keep walking..")
                    pyautogui.hotkey('win', 'down','down')
                    return " "
                else:
                    print("okay Byee and be carefull.")
                    speak("okay Byee and be carefull.")
                    return " "

