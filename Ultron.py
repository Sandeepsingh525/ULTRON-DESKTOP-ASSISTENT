import pyttsx3
# pip install pyttsx3 convert text data into speech
import datetime
import speech_recognition as sr
# pip install SpeechRecognition speech from mic to text
import smtplib
from secrets import senderemail, epwd, to
from email.message import EmailMessage
import pyautogui
import webbrowser as wb
from time import sleep
import wikipedia
import os
import cv2
import sys
from requests import get
import pywhatkit
import pyjokes
import random
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTimer, QTime, QDate, Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from fro import Ui_MainWindow
import numpy as np


engine = pyttsx3.init()


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def get_voices(voice):
    voices = engine.getProperty('voices')
    # print(voices[0].id)
    if voice == 1:
        engine.setProperty('voice', voices[0].id)
        speak("Hello this is Ultron")
    if voice == 2:
        engine.setProperty('voice', voices[1].id)
        speak("Hello this is friday")


def Time():
    time = datetime.datetime.now().strftime("%I:%M:%S")
    # hour=I minutes=M seconds=S
    speak("The current time is:")
    speak(time)


def Date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("the current date is:")
    speak(date)
    speak(month)
    speak(year)


def greeting():
    hour = int(datetime.datetime.now().hour)
    if 6 <= hour < 12:
        speak("Good Morning sir!")
    elif 12 <= hour < 18:
        speak("Good Afternoon sir!")
    elif 18 <= hour < 24:
        speak("Good Evening sir!")
    else:
        speak("Good Night sir!")


def wishme():
    speak("welcome back sir!")
    Time()
    Date()
    greeting()
    speak("Ultron at your services,please tell me how may i help you!")


def takeCommandCMD():
    query = input("please tell me how may i help you?")
    return query


def sendEmail(receiver, subject, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(senderemail, epwd)
    email=EmailMessage()
    email['From'] = senderemail
    email['To'] = receiver
    email['Subject'] = subject
    email.set_content(content)
    server.send_message(email)
    # server.sendmail(senderemail, to, content)
    server.close()


def sendwhatsmsg(phone_no, message):
    Message = message
    wb.open('https://web.whatsapp.com/send?phone='+phone_no+'&text='+Message)
    sleep(10)
    pyautogui.press('enter')


class MainThread(QThread):
    def __init__(self):
        super(MainThread, self).__init__()

    def run(self):
        self.TaskExecution()

    def takeCommandMic(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening.....")
            r.pause_threshold = 1
            audio = r.listen(source)
        try:
            print("Recognizing..")
            query = r.recognize_google(audio, language='en-IN')
            print(query)
        except Exception as e:
            print(e)
            speak("Say that again please.......")
            return "None"
        return query

    def TaskExecution(self):
        # pyautogui.press('esc')
        # speak("verification successful")
        # speak("Welcome back sandeep")
        get_voices(1)
        wishme()
        while True:
            self.query = self.takeCommandMic().lower()
            if 'time' in self.query:
                Time()
            elif 'date' in self.query:
                Date()
            elif 'email' in self.query:
                email_list = {
                    # 'sandeep': 'sandeepsingh261099@gamil.com',
                    'mehak': 'mehakpreetsingh036@gmail.com'
                }
                try:
                    speak("To whom you want to send mail?")
                    name = self.takeCommandMic()
                    receiver = email_list[name]
                    speak("what is the subject of the mail?")
                    subject = self.takeCommandMic()
                    speak("what should i say?")
                    content = self.takeCommandMic()
                    sendEmail(receiver, subject, content)
                    speak("email has been send")
                except Exception as e:
                    print(e)
                    speak("Unable to send the email")
            elif 'message' in self.query:
                user_name = {
                    'mehak': '+919306927774',
                    
                }
                try:
                    speak("To whom you want to send whatsapp message?")
                    name = self.takeCommandMic()
                    phone_no = user_name[name]
                    speak("what is the Message")
                    message = self.takeCommandMic()
                    sendwhatsmsg(phone_no, message)
                    speak("message has been send")
                except Exception as e:
                    print(e)
                    speak("Unable to send the message")
            elif 'wikipedia' in self.query:
                speak('Searching on Wikipedia...')
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)
            elif "open camera" in self.query:
                cap = cv2.VideoCapture(0)
                while True:
                    ret, img = cap.read()
                    cv2.imshow('webcam', img)
                    k = cv2.waitKey(50)
                    if k == 27:
                        break;
                cap.release()
                cv2.destroyAllWindows()
            elif 'open youtube' in self.query:
                wb.open("www.youtube.com")
            elif 'open facebook' in self.query:
                wb.open("www.facebook.com")
            elif 'open instagram' in self.query:
                wb.open("www.instagram.com")
            elif 'open Telegram' in self.query:
                wb.open("www.telegram.com")
            elif 'open stack overflow' in self.query:
                wb.open("stackoverflow.com")
            elif "shut down the system" in self.query:
                os.system("shutdown/s/t 5")
            elif "restart the system" in self.query:
                os.system("shutdown/s/t 5")
            elif "sleep the system" in self.query:
                os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
            elif "switch the window" in self.query:
                pyautogui.keyDown("alt")
                pyautogui.press("tab")
                # time.sleep(1)
                pyautogui.keyUp("alt")
            elif 'Maps' in app:
                wb.open(
                    "https://www.google.com/maps/place/Abohar,+Punjab/@30.1525304,74.1621987,13z/data=!3m1!4b1!4m5!3m4!1s0x3917a79154f86721:0x4ce09ae52bb2fd93!8m2!3d30.1468621!4d74.2008233")
            elif 'offline' in self.query:
                quit()


startExecution = MainThread()


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask)
        self.ui.pushButton_2.clicked.connect(self.close)

    def startTask(self):
        self.ui.movie = QtGui.QMovie("bh.jpg")
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("rebort.gif")
        self.ui.label_2.setMovie(self.ui.movie)
        self.ui.movie.start()
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(2500)
        startExecution.start()

    def showTime(self):
        current_time = QTime.currentTime()
        current_date = QDate.currentDate()
        label_time = current_time.toString('hh:mm:ss')
        label_date = current_date.toString(Qt.ISODate)
        self.ui.textBrowser.setText(label_date)
        self.ui.textBrowser_2.setText(label_time)


app = QApplication(sys.argv)
ultron = Main()
ultron.show()
exit(app.exec_())




