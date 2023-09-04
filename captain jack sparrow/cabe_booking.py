import pyttsx3
import json
import pyautogui
from selenium import webdriver
import speech_recognition as sr
from time import sleep


engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', 150)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.runAndWait()

def curr_loc():
    areas = "#############"
    return areas
    

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

def cab(dest):
    print("it will take few minutes,please wait..")
    speak("it will take few minutes,please wait..")
    drive = webdriver.Chrome(executable_path=r'###################chrome driver path##############')
    drive.get(url='https://m.uber.com/looking')
    sleep(8)
    mail_id = "somasekar.v2021ecec@sece.ac.in"
    drive.find_element('xpath','//*[@id="PHONE_NUMBER_or_EMAIL_ADDRESS"]').send_keys(mail_id)
    drive.find_element('xpath','//*[@id="forward-button"]').click()
    sleep(5)
    start = curr_loc()
    drive.find_element('xpath','//*[@id="wrapper"]/div[2]/div/div/div[1]/div[2]/div[2]/div/div/div/div[2]').click()
    #pass_word = input()
    sleep(35)

    sleep(5)
    drive.find_element('xpath','/html/body/div[1]/div/div/div[1]/div/div[2]/div[2]/div/span/div/div[2]/div[1]/div[1]/div/div[2]/input').send_keys(start)
    sleep(4)
    drive.find_element('xpath','/html/body/div[1]/div/div/div[1]/div/div[2]/div[2]/div/span/div/div[3]/ul/li[1]/div[2]').click()
    sleep(5)
    drive.find_element('xpath','//*[@id="wrapper"]/div[1]/div/div[2]/div[2]/div/span/div/div[2]/div[1]/div[3]/div/div[2]/input').send_keys(dest)
    sleep(4)
    drive.find_element('xpath','/html/body/div[1]/div/div/div[1]/div/div[2]/div[2]/div/span/div/div[3]/ul/li[1]/div[2]').click()
    sleep(5)
    print("searching the cab for you.")
    speak("searching the cab for you.")
    auto = drive.find_element('xpath','//*[@id="wrapper"]/div[1]/div/div[2]/div[2]/div/span/div/div[3]/div/ul/li[1]/div[2]/div[1]/p[1]')
    auto_amount = drive.find_element('xpath','//*[@id="wrapper"]/div[1]/div/div[2]/div[2]/div/span/div/div[3]/div/ul/li[1]/div[2]/div[2]/div/p[1]')
    cab = drive.find_element('xpath','//*[@id="wrapper"]/div[1]/div/div[2]/div[2]/div/span/div/div[3]/div/ul/li[2]/div[2]/div[1]/p[1]')
    cab_amount = drive.find_element('xpath','//*[@id="wrapper"]/div[1]/div/div[2]/div[2]/div/span/div/div[3]/div/ul/li[2]/div[2]/div[2]/div/p[1]')
    sleep(2)
    print(f"the total amount of {auto.text} is {auto_amount.text}.")
    speak(f"the total amount of {auto.text} is {auto_amount.text}.")
    sleep(2)
    print(f"the total amount of {cab.text} is {cab_amount.text}.")
    speak(f"the total amount of {cab.text} is {cab_amount.text}.")
    sleep(3)
    print("if you okay with the cost of cab , i will book it or not.")
    speak("if you okay with the cost of cab , i will book it or not.")
    text = takeCommand().lower()
    if "no" in text or "it's expansive" in text or "too expansive" in text or "no need" in text or "no need o book" in text:
        print("okay byee and take care..")
        speak("okay byee and take care..")
        pyautogui.hotkey('ctrl','w')
        return " "
    else:
        print(f"which cab you need it's {auto_amount.text} or {cab_amount.text}.")
        speak(f"which cab you need it's {auto_amount.text} or {cab_amount.text}.")
        text=takeCommand().lower()
        if "first" in text or "auto" in text or "okay uberauto" in text or "lowest cost" in text or "lowest price" in text or "lowest" in text:
            book_finesh = "The cab is one the way for you."
            pyautogui.hotkey('ctrl','w')
            return book_finesh
    

