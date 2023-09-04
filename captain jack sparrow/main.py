import pyttsx3
import speech_recognition as sr
import  os
import datetime
import pyautogui
import random
import pywhatkit
import subprocess
import pyjokes
import requests
import json
import operator
import webbrowser
import shutil
import sys
import torch
import cv2
import pandas
import psutil
import torchvision
import seaborn
import matplotlib
from object_detector import*
from message import*
from weather import*
from wikipedia import*
from location import*
from cabe_booking import*
from emergency_call import*
from swiggy_create import*
from swiggy_login import*
from trafic_detection import*
from selenium import webdriver
from time import sleep
from PyQt5 import QtGui
from PyQt5.QtCore import*
from PyQt5.QtGui import*
from PyQt5.QtWidgets import*
from GUIFINAL import Ui_Form

engine = pyttsx3.init('sapi5')
rate = engine.getProperty('rate')
engine.setProperty('rate',180)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.runAndWait()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

class MainThread(QThread):
    def __init__(self):
        super(MainThread,self).__init__()
    
    def run(self):
        self.TaskExection()

    def takeCommand(self):
        recog = sr.Recognizer()

        with sr.Microphone() as source:
            recog.energy_threshold = 1
            recog.adjust_for_ambient_noise(source, duration=1.2)
            print("Listening....")
            audio = recog.listen(source)

        try:
            print("Recognizing...")
            query = recog.recognize_google(audio,language='en-in')
            print(f"User said: {query}\n")

        except:
            print("Unable to Recognize your voice.")
            speak("Unable to Recognize your voice.")
            return "  "

        return query

    today_date=datetime.datetime.now()

    def wakeUpCommands(self):
        recog = sr.Recognizer()

        with sr.Microphone() as source:
            recog.energy_threshold = 1
            recog.adjust_for_ambient_noise(source, duration=1.2)
            print("Luna is sleeping....")
            audio = recog.listen(source)

        try:
            print("Recognizing...")
            query = recog.recognize_google(audio,language='en-in')
            print(f"User said: {query}\n")

        except:
            print("Please tell me again")
            query="none"

        return query

    def wishings(self):
        hour=int(datetime.datetime.now().hour)
        if hour>=0 and hour<12:
            print("Good Morning...")
            speak("Good Morning...")
        elif hour>=12 and hour<17:
            print("Good Afternoon...")
            speak("Good Afternoon...")
        elif hour>=17 and hour<21:
            print("Good Evening...")
            speak("Good Evening...")
        else:
            print("Good Night...")
            speak("Good Night...")

    def note(text):
        date= datetime.datetime.now()
        file_name = str(date).replace(":","") + "-note.txt"
        with open(file_name, "w") as f:
            f.write(text)

        subprocess.Popen(["notepad.exe", file_name])


    def TaskExection(self):
        while True:
            self.text = self.wakeUpCommands().lower()
            if "luna" in self.text or "hey luna" in self.text or "hello luna" in self.text or "hai luna" in self.text or "hai" in self.text or "hello" in self.text or "hey" in self.text:
                self.wishings()
                print("yes , how can i help you...")
                speak ("yes , how can i help you...")
                while True:
                    self.text = self.takeCommand().lower()

                    if "date" in self.text or "day" in self.text:
                        print("The date is " + self.today_date.strftime("%d") +" "+ self.today_date.strftime("%B"))
                        speak("The date is " + self.today_date.strftime("%d") + self.today_date.strftime("%B"))
                        
                    elif "detect the object" in self.text or "detect object" in self.text or "object detect" in self.text:
                        detection = objectfinding("start")
                        pyautogui.hotkey('win', 'down','down')
                        break

                    elif "stop detecting" in self.text or "stop detect" in self.text:
                        detection = objectfinding("stop")
                        break
                    elif "find the signal" in self.text or "what signal" in self.text or "tell me the signal color" in self.text or "signal color" in self.text:
                        trafic = trafic_signal()
                        print(trafic)
                        break
                    
                    elif "what is your name" in self.text:
                        print("My name is LUNA...")
                        speak("My name is LUNA...")
                        
                    elif "who are you" in self.text:
                        print("i am your personal assistant")
                        speak("i am your personal assistant")
                        
                    elif "who i am" in self.text:
                        print("If you talk then definitely your human.")
                        speak("If you talk then definitely your human.")
                        
                    elif "i love you" in self.text or "love you" in self.text:
                        print("It is 7th sense that destroy all other senses")
                        speak("It is 7th sense that destroy all other senses")
                        
                    elif "for what purpose you exist" in self.text:
                        print("to useful for blind people.")
                        speak("to useful for blind people.")
                           
                    #elif "what are tasks you perform" in self.text or "what is your work" in self.text:
                       # print("saying the date and time ,daily weather report,search anythink you need,playing music,share daily news,jokes also,transulate any language,taking notes.")
                       # speak("saying the date and time ,daily weather report,search anythink you need,playing music,share daily news,jokes also,transulate any language,taking notes.")
                        #print("checking the body conduction and sharing location until you reach the destination,book the cab for your travel,and order the what ever you want.")
                       #speak("checking the body conduction and sharing location until you reach the destination,book the cab for your travel,and order the what ever you want.")
                        
                    elif "who is inverted you" in self.text:
                        print("for fortune term.")
                        speak("for fortune term.")
            
                    elif "time" in self.text:
                        print(self.today_date.strftime("%I") + " : " + self.today_date.strftime("%M") + " : " + self.today_date.strftime("%p"))
                        speak("sir the current time is," + self.today_date.strftime("%I") + self.today_date.strftime("%M") + self.today_date.strftime("%p"))
                        
                    elif "joke" in self.text or "jokes" in self.text:
                        print(pyjokes.get_joke())
                        speak(pyjokes.get_joke())
                        
                    elif 'how are you' in self.text:
                        print("I am fine, Thank you")
                        speak("I am fine, Thank you")
                        print("How are you?")
                        speak("How are you?")
                        
                    elif 'fine' in self.text:
                        print("It's good to know that your fine")
                        speak("It's good to know that your fine")
                        
                    elif "write a note" in self.text or "take a note" in self.text:
                        print("tell me file name.")
                        speak("tell me file name.")
                        title = self.takeCommand().lower()
                        print("What should i write,sir?")
                        speak("What should i write,sir?")
                        note = self.takeCommand().lower()
                        print(note)
                        date = datetime.datetime.now()
                        file_name = (f"{title}") + "-note.txt"
                        with open(file_name, "w") as f:
                            f.write(note)

                        subprocess.Popen(["notepad.exe", file_name])
                        pyautogui.hotkey('win', 'down','down') 

                    elif "you are my gf" in self.text or "you are my bf" in self.text or "you are my girlfriend" in self.text or "you are my boyfriend" in self.text:
                        print("I'm not sure about, may be you should give me some time")
                        speak("I'm not sure about, may be you should give me some time")
                        
                    elif "news" in self.text:
                        url = ('https://newsapi.org/v2/top-headlines?'
                            'country=in&'
                            'apiKey=c7bce012901b43529e9bd2e90367b5ac')
                        try:
                            response = requests.get(url)
                        except:
                            speak("Please check your connection")

                        news = json.loads(response.text)
                        
                        for new in news["articles"]:
                            print(str(new["title"]), "\n")
                            speak(str(new["title"]))
                            engine.runAndWait()
                            print(str(new["description"]), "\n")
                            speak(str(new["description"]))
                            engine.runAndWait()
                            print(str(new["title"]), "\n")
                            speak(str(new["title"]))
                            engine.runAndWait()
                            print(str(new["description"]), "\n")
                            speak(str(new["description"]))
                            engine.runAndWait()
                            
                    elif "weather" in self.text:
                        print("The weather is ," + str(temp()))
                        speak("The weather is ," + str(temp()))
                        print("And the description is," + str(des()))
                        speak("And the description is," + str(des()))

                    elif "transulate" in self.text or "transulated" in self.text or "translate" in self.text:
                        drive = webdriver.Chrome(executable_path=r'########################chrome drive path####################')
                        drive.get(url='https://translate.google.com/?sl=auto&tl=ta&op=translate')
                        sleep(8)
                        print("what should i transulate?")
                        speak("what should i transulate?")
                        name = self.takeCommand().lower()
                        print(name)
                        print("which language do you want to transulate?")
                        speak("which language do you want to transulate?")
                        name1 = self.takeCommand().lower()
                        print(name1)
                        drive.find_element('xpath','//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[1]/c-wiz/div[1]/c-wiz/div[5]/button/div[3]').click()
                        sleep(3)
                        drive.find_element('xpath','//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[1]/c-wiz/div[2]/c-wiz/div[2]/div/div[2]/input').send_keys(name1)
                        sleep(3)
                        drive.find_element('xpath','//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[1]/c-wiz/div[2]/c-wiz/div[2]/div/div[4]/div').click()
                        sleep(3)
                        drive.find_element('xpath','//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[3]/c-wiz[1]/span/span/div/textarea').send_keys(name)
                        sleep(6)
                        drive.find_element('xpath','//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[3]/c-wiz[2]/div/div[9]/div/div[4]/div[1]/div[2]/span/button/div[3]').click()
                        sleep(3)
                        drive.minimize_window()
                        
                    elif "my location" in self.text or "current location" in self.text:
                        print("city: Salem\n,street: Junction Main Road\n,Area: Tamilnadu\n,country: India.\n")
                        speak("city: Salem\n,street: Junction Main Road\n,Area: Tamilnadu\n,country: India.\n")
                        
                    elif "i want to go some where" in self.text or "i need to go some where" in self.text or "i need to go some place" in self.text or "go some where" in self.text or "i need to go some place" in self.text or "go some place" in self.text or "i want to go" in self.text:
                        print("where you want to go.")
                        speak("where you want to go.")
                        place=self.takeCommand().lower()
                        find_loc = loc_tofind(place)
                        print(" ")
                        break
                            
                    elif "song" in self.text or "music" in self.text or "play song" in self.text or "play music" in self.text:
                        print("Which song would you like to play?")
                        speak("Which song would you like to play?")
                        song = self.takeCommand().lower()
                        print(f"Sure, searching for '{song}' on YouTube.")
                        speak(f"Sure, searching for '{song}' on YouTube.")
                        pywhatkit.playonyt(song)
                        sleep(3)
                        #pyautogui.press('space')
                        pyautogui.hotkey('win', 'down','down')

                    elif "happy mood" in self.text or "i am happy mood" in self.text or "i am happy" in self.text:
                        print("ooh really")
                        speak("ooh really")
                        print("what happend?")
                        speak("what happend?")
                        self.takeCommand().lower()
                        print("it's party time i will play the song for you.")
                        speak("it's party time i will play the song for you.")
                        print("say yes or noo")
                        speak("say yes or noo")
                        party = self.takeCommand().lower()
                        if "yes" in party or "play the song" in party or "play" in party or "sure" in party or "sure play" in self.text:
                            pywhatkit.playonyt("kuthu songs")
                            sleep(30)
                            pyautogui.press('space')
                            pyautogui.hotkey('win', 'down','down')
                            
                        else:
                            print("okay enjoy and have fun.")
                            speak("okay enjoy and have fun.")
                            
                    elif "stop the song" in self.text or "pause" in self.text or "halt" in self.text:
                        pyautogui.press('space') 
                        pyautogui.hotkey('win', 'down','down')
                        print("Song paused.")
                        speak("Song paused.")
                        
                    elif "stop music" in self.text or "stop song" in self.text:
                        pyautogui.press('space')
                        pyautogui.hotkey('win', 'down','down')
                        print("Song stopped.")
                        speak("Song stopped.")
                                        
                    elif "message" in self.text or "messages" in self.text:
                        speak("to whome will send a message")
                        person = self.takeCommand().lower()
                        print(person)
                        speak("what message will send")
                        mess = self.takeCommand().lower()
                        ptr = meaasge(mess)
                        print(f"{ptr} to {person}...")
                        speak(f"{ptr} to {person}...")
                        
                    elif "search" in self.text or "information" in self.text:
                        print("you need information related to which topic?")
                        speak("you need information related to which topic?")
                        search = self.takeCommand().lower()
                        print(search)
                        print(f"searching information {search} in wikipedia")
                        speak(f"searching information {search} in wikipedia")
                        info = get_info(search)
                        print(f"{info.text}")
                        speak(f"{info.text}")
                        pyautogui.hotkey('win', 'down','down')
                       
                    
                    elif "cool" in self.text or "nice" in self.text or "awsome" in self.text or "thank you" in self.text:
                        speak("Yes sir, That's my Pleasure!")

                    elif "book the cab" in self.text or "cab" in self.text or "can you book me a cab" in self.text:
                        print("where you want to go..")
                        speak("where you want to go..")
                        book = self.takeCommand().lower()
                        printing = cab(book)
                        print(printing)
                        speak(printing)
                        break

                    elif "i am not good" in self.text or "i am feeling bad" in self.text or "i am not okay" in self.text:
                        print("are you okay or any problem")
                        speak("are you okay or any problem")
                        take = self.takeCommand().lower()
                        if "okay" in take or "ok" in take:
                            print("don't vary i will play the song for you.")
                            speak("don't vary i will play the song for you.")
                            print("say yes or no")
                            speak("say yes or no")
                            pywhatkit.playonyt("sad songs")
                            pyautogui.hotkey('win', 'down','down')
                            sleep(30)
                            pyautogui.press('space')
                            
                        else:
                            print("okay byee and take care..")
                            speak("okay byee and take care..")
                            

                    elif "call my guardian" in self.text or "call guardian" in self.text:
                        mobile_phone()
                        print("The call is placed.")
                        speak("The call is placed.")
                        

                    elif "stop listening" in self.text or "don't listen" in self.text or "do not listen" in self.text:
                        break

                    elif "exit" in self.text or "quit" in self.text:
                        exit()


startExecution = MainThread()

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.ui.startpushButton.clicked.connect(self.startTask)

    def startTask(self):
        self.ui.movie = QtGui.QMovie("################image path###############")
        self.ui.back_animation.setMovie(self.ui.movie)
        self.ui.movie.start()

        self.ui.movie = QtGui.QMovie("################image path###############")
        self.ui.voice_input.setMovie(self.ui.movie)
        self.ui.movie.start()

        self.ui.movie = QtGui.QMovie("################image path###############")
        self.ui.start_button.setMovie(self.ui.movie)
        self.ui.movie.start()

        self.ui.movie = QtGui.QMovie("################image path###############")
        self.ui.side_loding.setMovie(self.ui.movie)
        self.ui.movie.start()

        self.ui.movie = QtGui.QMovie("################image path###############")
        self.ui.label_3.setMovie(self.ui.movie)
        self.ui.movie.start()

        self.ui.movie = QtGui.QMovie("################image path###############")
        self.ui.bar_loding.setMovie(self.ui.movie)
        self.ui.movie.start()

        self.ui.movie = QtGui.QMovie("################image path###############")
        self.ui.human_body.setMovie(self.ui.movie)
        self.ui.movie.start()

        self.ui.movie = QtGui.QMovie("################image path###############")
        self.ui.loding_circle.setMovie(self.ui.movie)
        self.ui.movie.start()

        startExecution.start()

app = QApplication(sys.argv)
assistant = Main()
assistant.show()
exit(app.exec_())
