from selenium import webdriver
import speech_recognition as sr
from time import sleep
import pyttsx3

engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', 150)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.runAndWait()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

recog = sr.Recognizer()

def logined():
    drive = webdriver.Chrome(executable_path=r'#######################chrome drive path################')
    drive.get(url='https://www.swiggy.com/')
    sleep(2)
    # opening login page
    speak("opening login page")
    drive.find_element('xpath','//*[@id="root"]/div[1]/div[1]/div/div[1]/div[1]/div/div[1]/div/a[1]').click()
    sleep(2)
    # enter your phone number
    speak("entering your phone number")
    number = "9159365133"
    drive.find_element('xpath','//*[@id="mobile"]').send_keys(number)
    drive.find_element('xpath','//*[@id="overlay-sidebar-root"]/div/div/div[2]/div/div/div/form/div[2]/a').click()
    sleep(2)
    # say the otp
    # automatic sms receiving
    sleep(15)
    # verifiy otp
    speak("verifing the OTP")
    drive.find_element('xpath','//*[@id="overlay-sidebar-root"]/div/div/div[2]/div/div/div/div[2]/form/div[2]/div[2]/a').click()
    sleep(15)
    drive.find_element('xpath', '//*[@id="root"]/div[1]/div[1]/div/div[1]/div[1]/div/div[2]/div/button').click()
    sleep(8)
    # to click the search icon
    drive.find_element('xpath','//*[@id="root"]/div[1]/header/div/div/ul/li[5]/div/span[2]').click()
    sleep(3)
    # to search restarurant
    speak("which restarurant do you want?")
    speak("say restaruant name fully.")
    with sr.Microphone() as source:
        recog.energy_threshold = 1000
        recog.adjust_for_ambient_noise(source, 1.2)
        print("Listening....")
        audio = recog.listen(source)
        restarurant = recog.recognize_google(audio)
        print(restarurant)
    drive.find_element('xpath', '//*[@id="root"]/div[1]/div[1]/div[1]/div/form/div/div[1]/input').send_keys(restarurant)
    speak(f"searching the {restarurant}.")
    sleep(3)
    # selecting the restarurant
    speak(f"selecting the {restarurant}")
    drive.find_element('xpath', '//*[@id="root"]/div[1]/div[1]/div[2]/div/div/button[1]').click()
    sleep(3)
    drive.find_element('xpath', '//*[@id="root"]/div[1]/div[1]/div[2]/div/div/div[3]/div[1]/div/a').click()
    sleep(3)
    speak(f"select you liked dishes on {restarurant}")
    # how many dishes to order
    speak("And how many dishes do you want to select?")
    item_lis = 0

    with sr.Microphone() as source:
        recog.energy_threshold = 1000
        recog.adjust_for_ambient_noise(source, 1.2)
        print("Listening....")
        audio = recog.listen(source)
        items = recog.recognize_google(audio)
        print(items)
        item_lis = int(items)
        # selecting the dishes
        if item_lis > 0:
            for i in range(item_lis):
                speak(f"select the {i} dish")
                with sr.Microphone() as source:
                    recog.energy_threshold = 1000
                    recog.adjust_for_ambient_noise(source, 1.2)
                    print("Listening....")
                    audio = recog.listen(source)
                    dish = recog.recognize_google(audio)
                    print(dish)
                drive.find_element('xpath','//*[@id="root"]/div[1]/div[1]/div[1]/div[3]/div[2]/div/div/div[2]/span[2]/input').send_keys(dish)
                sleep(3)
                speak(f"selecting the dish{dish}")
                # The dishes was adding to the cart
                speak("The dishes was adding to the cart")
                drive.find_element('xpath', '//*[@id="h-1956821465"]/div[2]/div[1]/div[1]/div/div[2]/div/div').click()
                sleep(3)
                # to increase the quanitiy
                speak("would you like to increase the quanitiy?")
                with sr.Microphone() as source:
                    recog.energy_threshold = 1000
                    recog.adjust_for_ambient_noise(source, 1.2)
                    print("Listening....")
                    audio = recog.listen(source)
                    quantity = recog.recognize_google(audio)
                    print(quantity)
                    qtn_item = 0
                    if "yes" or "increase the quanitiy" in quantity:
                        with sr.Microphone() as source:
                            recog.energy_threshold = 1000
                            recog.adjust_for_ambient_noise(source, 1.2)
                            print("Listening....")
                            audio = recog.listen(source)
                            quan = recog.recognize_google(audio)
                            print(quan)
                            qty_item = int(quan)
                            if qty_item > 0:
                                speak(f"Adding {qty_item} for your dish")
                                for i in range(qty_item):
                                    drive.find_element('xpath','//*[@id="h-1956821465"]/div[2]/div[1]/div[1]/div/div[2]/div/div/div[2]').click()
                                    sleep(3)
                    elif "no" or "can't increase" or "can not increase" in quantity:
                        print("okay going to next process")

    speak("going to check out process")
    drive.find_element('xpath', '//*[@id="menu-content"]/div[2]/div/div[3]/button').click()
    sleep(5)
    total = drive.find_element('xpath', '//*[@id="root"]/div[1]/div[1]/div/div[2]/div/div[2]/div[2]')
    speak(f"The total amount of the dishes are{total.text}.")
    speak("can i conform the order or not")
    with sr.Microphone() as source:
        recog.energy_threshold = 1000
        recog.adjust_for_ambient_noise(source, 1.2)
        print("Listening....")
        audio = recog.listen(source)
        conf = recog.recognize_google(audio)
        print(conf)
        if "yes" or "conform" or "conform the order" in conf:
            speak("pament process going on.")
        else:
            exit()
    drive.maximize_window()
    str2 = "your order is placed delivering soon"
    return str2
