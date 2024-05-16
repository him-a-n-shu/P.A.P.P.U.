from __future__ import unicode_literals
from Automation import TimeTable
from keyboard import press
from keyboard import press_and_release
import Automation
from asyncore import write
from pydoc import cli
import statistics
import click
import qrcode
import cv2
import smtplib, ssl
import string
import random
import wolframalpha
import webbrowser,requests,zipfile, io
from winsound import PlaySound
import winsound
from gtts import gTTS
from translate import Translator
from email.mime import base
import pytube
import re
import urllib.request
import numpy as np
import time
import cv2
import speedtest
import psutil
import pyautogui
import pywikihow
import operator
from cProfile import run
import datetime
from email import message
import ipaddress
import json
import numbers
import sys
from time import time
from tkinter import E, W
from urllib.request import urlopen
from venv import create
from flask import request
import googlesearch
import speech_recognition as sr
import pyttsx3
import wikipedia
import webbrowser
import os
from PyDictionary import PyDictionary
from googlesearch import search
import pywhatkit as kit
import pyjokes
import pyautogui
import requests
import PyPDF2
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTimer, QTime, QDate, Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from bs4 import BeautifulSoup



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 180-200)
contacts = {} #Add your contacts here!!!
what_grp_diary = {}



def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")

    speak("I am PAPPU Sir. Please tell me how may I help you")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listenning ...")
        r.pause_threshold = 1
        audio = r.listen(source)
    
    try:
        print("Rcognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)
        print("Say that again please...")
        return "None"
    return query

def sendEmail(from_em,password_em,to,content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(from_em,password_em)
    server.sendmail(from_em,to,content)
    server.close()

def whatsapp_grp(group_id,message):
    open_chat = "https://web.whatsapp.com/accept?code=" + group_id
    webbrowser.open(open_chat)
    time.sleep(15)
    pyautogui.write(message)
    pyautogui.press('enter')

def TaskExecution():
    wishMe()
    while True:
        query = takeCommand().lower()

        #searching something from google and wikipedia
        if 'wikipedia' in query:
            speak("Searching Wikipedia.. Please Wait")
            query = query.replace("Wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
    
        elif 'search' in query:
            speak("Searching google... Please Wait")
            tabUrl="https://www.google.com/search?q="
            term = query.replace("search", '')
            webbrowser.open(tabUrl+term)

        #TimeTable
        elif 'timetable' in query:
            TimeTable()

        #QR Code
        elif 'generate qr' in query:
            print("please tell the data for QR code")
            speak("please tell the data for QR code")
            data = takeCommand()
            data = f"{data}"
            print("please tell the name for QR code png")
            speak("please tell the name for QR code png")
            img_raw = takeCommand()
            img = f"{img_raw}.png"
            Automation.QR_Code_Generator(data,img)
            print(f"{img} is saved in the folder.")
            speak(f"{img} is saved in the folder.")
        
        elif 'read qr' in query:
            print("please tell the name of QR code png")
            speak("please tell the name of QR code png")
            img_raw = takeCommand()
            img = f"{img_raw}.png"
            Automation.QR_reader(img)
        
        elif 'game' in query:
            query.replace("download","")
            query.replace("game","")
            game_name = query
            Automation.game_download(game_name)

        #stats
        elif 'open stats' in query:
            print("Opening statistics calculator...")
            speak("Opening statistics calculator...")
            l1 = eval(input("Enter data in List or Tuple --> "))
            print("what do you want to find?")
            speak("what do you want to find?")
            stat_what = takeCommand().lower()
            stat_what = stat_what.lower()
            if 'median' in stat_what:
                Automation.median(l1)
            elif 'mean' in stat_what:
                Automation.mean(l1)
            elif 'mode' in stat_what:
                Automation.mode(l1)
            elif 'variance' in stat_what:
                Automation.variance(l1) 
            elif 'standard deviation' in stat_what:
                Automation.stdev(l1)
            elif 'range' in stat_what:
                Automation.range(l1)
            else:
                print("Error, there is no such operator in statistics.")
                speak("Error, there is no such operator in statistics.")
            pass
        
        elif 'join class' in query:
            print("Joining class, please wait for a while")
            speak("Joining class, please wait for a while")
            Automation.OnlineClasses()

        #ChromeAuto
        elif 'auto chrome mode' in query:
            print("Auto chrome mode is enabled, please tell what should I do")
            speak("Auto chrome mode is enabled, please tell what should I do")
            chro_query = takeCommand().lower()
            chro_query = chro_query.lower()
            Automation.ChromeAuto(chro_query)
        
        #YoutubeAuto
        elif 'auto youtube mode' in query:
            print("Auto youtube mode is enabled, please tell what should I do")
            speak("Auto youtube mode is enabled, please tell what should I do")
            you_query = takeCommand().lower()
            you_query = you_query.lower()
            Automation.YoutubeAuto(you_query)

        #Send Email
        elif 'send email to' in query:
            try:
                print("Enter your Email.")
                speak("Enter your Email.")
                your_em = takeCommand()
                your_em = your_em.lower()
                your_em = your_em.replace("at the rate", "@")
                your_em = your_em.replace(" ", "")
                speak("Enter Password")
                password_em = input("Enter Password --> ")
                print("To whom?")
                speak("To whom?")
                to_em = takeCommand()
                to_em = to_em.lower()
                to_em = to_em.replace("at the rate", "@")
                to_em = to_em.replace(" ", "")
                print("What should I say?")
                speak("What should I say?")
                content = takeCommand()
                sendEmail(your_em,password_em,to_em,content)
            except Exception as e:
                print(e)
                print("Sorry sir, I am not able to send this email")
                speak("Sorry sir, I am not able to send this email")

        #GoogleMaps
        elif 'my location' in query:
            Automation.My_Location()

        elif 'where is' in query:
            place = query.replace("where is","")
            place = query.replace("PAPPU","")
            Automation.Google_maps(place)

        #Remote Connection
        elif 'remote connection' in query:
            os.startfile("Desktop\\AnyDesk.exe")
            click(x=708, y=47)
            speak("please tell ID")
            RC_ID = takeCommand()
            write(RC_ID)
            press('enter')
            speak("Please wait a while and enter the password. Thank you!")

        #Download music from youtube
        elif 'download music from youtube' in query:
            speak("Please Enter Code")
            ytm_code = input("Enter Code (For example: BaW_jenozKc in 'http://www.youtube.com/watch?v=BaW_jenozKc': ")
            yt_url = pytube.YouTube(f'http://www.youtube.com/watch?v={ytm_code}')

            try:
                print("Downloading...")
                speak("Downloading...")
                video = yt_url.streams.filter(only_audio=True).first()
                out_file = video.download()

                base, ext = os.path.splitext(out_file)
                new_file = base + ".mp3"
                os.rename(out_file, new_file)
                print("Successfully Downloaded")
                speak("Successfully Downloaded")
                
            except:
                print("Something went wrong! Please try again")
                speak("Something went wrong! Please try again")
            pass

        #password generator
        elif 'password generator' in query:
            s1 = string.ascii_lowercase
            s2 = string.ascii_uppercase
            s3 = string.digits
            s4 = string.punctuation
            #print(s1,s2,s3,s4)
            list1 = list(s1)
            list2 = list(s2)
            list3 = list(s3)
            list4 = list(s4)
            #print(list1,list2,list3,list4)
            random.shuffle(list1)
            random.shuffle(list2)
            random.shuffle(list3)
            random.shuffle(list4)
            speak("Enter password length")
            pass_len = int(input("Enter Password length --> "))
            print("Number of uppercase letters?")
            speak("Number of uppercase letters?")
            pass_upp_len = int(input("U: "))
            print("Number of lowercase letters?")
            speak("Number of lowercase letters?")
            pass_low_len = int(input("L: "))
            print("Number of digits?")
            speak("Number of digits?")
            pass_dig_len = int(input("D: "))
            print("Number of special characters?")
            speak("Number of special characters?")
            pass_pun_len = int(input("P: "))
            up_pass = list2[0:pass_upp_len]
            lo_pass = list1[0:pass_low_len]
            di_pass = list3[0:pass_dig_len]
            pu_pass = list4[0:pass_pun_len]
            password = up_pass+lo_pass+di_pass+pu_pass
            p = ("".join(random.sample(password, pass_len)))
            print(p)
            print("Do you want to save password?")
            speak("Do you want to save password?")
            y_n = takeCommand().lower()
            if 'yes' in y_n:
                username = input("Enter Username: ")
                remember = open('Passwords.txt','a+')
                remember.write(f"\n\nUsername --> {username}\nPassword --> {p}")
                remember.close()
            else:
                pass

        #Movie subtitle downloader
        elif 'subtitle' in query:
            try:
                print("Tell me the movie name!")
                speak("Tell me the movie name")
                movie_name = takeCommand()
                print("Language?")
                speak("Language?")
                language_subtitle = takeCommand().lower()
                language_subtitle = language_subtitle.lower()
                legal_movie_name = movie_name.replace(" ","-")
                url = requests.get('https://www.subscene.com/subtitles/'+legal_movie_name+f"/{language_subtitle}")
                url_soup = BeautifulSoup(url.content,'html.parser')
                urls = []
                for link in url_soup.select('.a1 a', href=True):
                    urls.append(link['href'])
                sub_link = 'https://www.subscene.com/'+urls[0]
                sub_url = requests.get(sub_link)
                sub_url_soup = BeautifulSoup(sub_url.content,'html.parser')
                dl_btn = sub_url_soup.select('.download a')
                dl_link = dl_btn[0]['href']
                download_link = 'https://www.subscene.com/'+dl_link
                r = requests.get(download_link)
                z = zipfile.ZipFile(io.BytesIO(r.content))
                z.extractall()
                print("Subtitles Downloaded.Check The Folder where this python file is stored.")
                speak("Subtitles Downloaded.Check The Folder where this python file is stored.")
            except IndexError:
                print("No File Found For:"+movie_name)

        #Inside temperature
        elif 'temperature' in query:
            Automation.Temp(query)

        #Remember
        elif 'remember that' in query:
            rememberMsg  = query.replace("remember that", "")
            rememberMsg  = query.replace("i", "you")
            speak("Tell me the time to remember you about your work")
            remember_time = takeCommand().upper()
            print("you told me to remind you that :", rememberMsg)
            speak(f"you told me to remind you that : {rememberMsg}")
            print("I will remember you at ", remember_time)
            speak(f"I will remember you at {remember_time}")
            remember = open('data.txt','w')
            remember.write(rememberMsg)
            remember.close()
            remember_time = remember_time.replace(".", "")
            remember_time = remember_time.upper()
            Automation.Alarm(remember_time)
            pass

        elif 'find' in query:
            query = query.replace("find","")
            Result = Automation.WolfRam(query)
            speak(Result)

        #Camera
        elif 'open camera' in query:
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam', img)
                k = cv2.waitKey(50)
                if k==27:
                    break
            cap.release()
            cv2.destroyAllWindows()

        #Translator
        elif 'open translator' in query:
            translator= Translator(from_lang="english",to_lang="hindi")
            print("Tell me the line")
            TraRd = takeCommand()
            translation = translator.translate(TraRd)
            print(translation)
            speak(translation)

        #open mobile camera
        elif 'open mobile camera' in query:
            URL = ""
            while True:
                img_arr = np.array(bytearray(urllib.request.urlopen(URL).read()),dtype=np.uint8)
                img = cv2.imdecode(img_arr,-1)
                cv2.imshow('IPWebcam',img)
                q = cv2.waitKey(1)
                if q==ord("q"):
                    break;

        #alarm
        elif 'set alarm for' in query:
            Automation.Alarm(query)

        #volume mixer
        elif 'volume' in query:
            print("what should I do, up or down or mute")
            speak("what should I do, up or down or mute")
            v_udm = takeCommand().lower()
            if 'up' in v_udm:
                pyautogui.press("volumeup")
            elif 'down' in v_udm:
                pyautogui.press("volumedown")
            elif 'mute' in v_udm:
                pyautogui.press("volumemute")
            pass

        #internet speed check
        elif 'internet speed' in query:
            st = speedtest.Speedtest()
            dl = st.download()
            dl1 = int((dl)*((9.537)*(10**-7)))
            up = st.upload()
            up1 = int((up)*((9.537)*(10**-7)))
            print(f"sir we have {dl1} mbps downloading speed and {up1} mbps uploading speed")
            speak(f"sir we have {dl1} mbps downloading speed and {up1} mbps uploading speed")

        #battery percentage
        elif 'how much power is left' in query or 'battery percentage' in query:
            battery = psutil.sensors_battery()
            percentage = battery.percent
            print(f"sir our system have {percentage} percent battery left.")
            speak(f"sir our system have {percentage} percent battery left.")
            if percentage>=75:
                print("we have enough power to continue our work")
                speak("we have enough power to continue our work")
            elif percentage>=40 and percentage<75:
                print("we should connnect our system to charging point to charge our battery")
                speak("we should connnect our system to charging point to charge our battery")
            elif percentage>=15 and percentage<30:
                print("we don't have enough power to work, please connect to charging")
                speak("we don't have enough power to work, please connect to charging")
            else:
                print("we have very low power, please connect to charging the system will shutdown very soon")

        #Calculator
        elif 'calculate' in query:
            r = sr.Recognizer()
            with sr.Microphone() as source:
                speak("Say what you want to calculate, example: 3 plus 3")
                print("listening...")
                r.adjust_for_ambient_noise(source)
                audio = r.listen(source)
            my_string = r.recognize_google(audio)
            print("Recognizing...")
            print("User said: ", my_string)
            def get_operator_fn(op):
                return {
                    '+' : operator.add,
                    '-' : operator.sub,
                    'x' : operator.mul,
                    'divided' : operator.__truediv__,
                }[op]
            def eval_binary_expr(op1, oper, op2):
                op1,op2 = int(op1), int(op2)
                return get_operator_fn(oper)(op1, op2)
            speak("your result is")
            speak(eval_binary_expr(*(my_string.split())))
            pass
        
        #How to do mod
        elif 'activiate how to do mod' in query:
            speak("How to do mod is activated.")
            print("How to do mod is activated.")
            while True:
                speak("Please tell me what you want to know?")
                print("Please tell me what you want to know?")
                how = takeCommand().lower()
                try:
                    if 'exit' in how or 'close' in how:
                        speak("okay sir, how to do mod is closed")
                        break
                    else:
                        max_results = 1
                        how_to = pywikihow.search_wikihow(how, max_results)
                        assert len(how_to) == 1
                        how_to[0].print()
                        speak(how_to[0].summary)
                        print(how_to[0].summary)
                except Exception as e:
                    speak("sorry sir, I am not able to find this.")

        #Weather Forecast
        elif 'weather' in query:
            search_weather = "weather in delhi"
            url = f"https://www.google.com/search?q={search_weather}"
            req = requests.get(url)
            data = BeautifulSoup(req.text, "html.parser")
            temp = data.find("div", class_="BNeawe").text
            speak(f"current {search_weather} is {temp}")
        
        #greetings
        elif 'your day' in query:
            speak("Its been ok, thanks for asking")

        elif 'hello PAPPU' in query:
            wishMe()
        
        elif 'how are you' in query:
            speak("I am fine sir, what about you")
        
        elif 'i am also good' in query or 'fine' in query:
            speak("that's great to hear from you")
        
        elif 'thank you' in query:
            speak("it's my pleasure sir.")

        #open applications and tabs
        elif 'open google' in query:
            webbrowser.open("google.com")
        
        elif 'open whatsapp' in query:
            webbrowser.open("https://web.whatsapp.com/")

        elif 'open gmail' in query:
            webbrowser.open("https://mail.google.com/mail/u/0/#inbox")

        elif 'open olabs' in query:
            webbrowser.open("olabs.edu.in")

        elif 'open class' in query:
            webbrowser.open("https://app.classroom.live/student-live-list")
        
        elif ' open classroom' in query:
            webbrowser.open("https://classroom.google.com/u/0/h")
        
        elif 'open youtube' in query:
            webbrowser.open("https://www.youtube.com/")
        
        elif 'open adobe' in query:
            codePath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Adobe Acrobat 9 Pro.lnk"
            os.startfile(codePath)

        elif 'open onenote' in query:
            codePath = "C:\\Program Files\\Microsoft Office\\root\\Office16\\ONENOTE.EXE"
            os.startfile(codePath)

        elif 'open chrome' in query:
            codePath = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(codePath)
        
        elif 'open edge' in query:
            codePath = "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"
            os.startfile(codePath)
        
        elif 'open code' in query:
            codePath = "C:\\Users\\HIMI\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'open zoom' in query:
            codePath = "C:\\Users\\HIMI\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe"
            os.startfile(codePath)
            Automation.zoom()
        
        elif 'open python' in query:
            codePath = "C:\\Users\\HIMI\\AppData\\Local\\Programs\\Python\\Python310\\pythonw.exe"
            os.startfile(codePath)
        
        elif 'open winrar' in query:
            codePath = "C:\\Program Files\\WinRAR\\WinRAR.exe"
            os.startfile(codePath)
        
        elif 'open unity hub' in query:
            codePath = "C:\\Program Files\\Unity Hub\\Unity Hub.exe"
            os.startfile(codePath)
        
        elif 'open calculator' in query:
            codePath = "C:\\Windows\\System32\\calc.exe"
            os.startfile(codePath)
        
        elif 'open notepad' in query:
            codePath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Accessories\\Notepad.lnk"
            os.startfile(codePath)
            speak("what should I write")
            write_note = takeCommand()
            write(write_note)
            speak("please tell name for file")
            note_name = takeCommand()
            np.save(f"{note_name}.txt")

        elif 'open word' in query:
            codePath = "C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE"
            os.startfile(codePath)
        
        elif 'open keyboard' in query:
            codePath = "C:\\Users\\HIMI\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Accessibility\\On-Screen Keyboard.lnk"
            os.startfile(codePath)

        elif 'open cmd' in query:
            codePath = "C:\\Users\\HIMI\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\System Tools\\Command Prompt.lnk"
            os.startfile(codePath)
        
        elif 'open control panel' in query:
            codePath = "C:\\Users\\HIMI\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\System Tools\\Control Panel.lnk"
            os.startfile(codePath)
        
        elif 'open run' in query:
            codePath = "C:\\Users\\HIMI\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\System Tools\\Run.lnk"
            os.startfile(codePath)
        
        elif 'open this pc' in query:
            codePath = "C:\\Users\\HIMI\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\System Tools\\computer.lnk"
            os.startfile(codePath)

        elif 'open excel' in query:
            codePath = "C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE"
            os.startfile(codePath)
        
        elif 'open math input panel' in query:
            codePath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Accessories\\Math Input Panel.lnk"
            os.startfile(codePath)
        
        elif 'open paint' in query:
            codePath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Accessories\\Paint.lnk"
            os.startfile(codePath)
        
        elif 'open snip' in query:
            codePath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Accessories\\Snipping Tool.lnk"
            os.startfile(codePath)

        elif 'open powerpoint' in query:
            codePath = "C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE"
            os.startfile(codePath)

        elif 'my important documents' in query:
            codePath = "D:\\Himanshu"
            os.startfile(codePath)
        
        elif 'open my builds' in query:
            codePath = "D:\\Game Engine\\Builds"
            os.startfile(codePath)

        elif 'open studio' in query:
            codePath = "C:\\Program Files\\Microsoft Visual Studio\\2022\\Community\\Common7\\IDE\\devenv.exe"
            os.startfile(codePath)

        #play music, movies and tell time
        elif 'play music' in query:
            music_dir = 'D:\\Songs'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, The time is {strTime}")

        elif 'the date' in query:
            strDay = datetime.datetime.now().date()
            speak(f"Sir, The Day is {strDay}")
        
        elif 'about today' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            strDay = datetime.datetime.now().date()
            speak(f"Sir, The Day is {strDay} and current time is {strTime}")

        elif 'play Harry Potter' in query:
            movies_dir = 'D:\\Harry Potter'
            HP = os.listdir(movies_dir)
            print(HP)
            os.startfile(os.path.join(movies_dir, HP))

        elif 'play stone' in query:
            movies_dir = 'D:\\Harry Potter'
            HP = os.listdir(movies_dir)
            print(HP[0])
            os.startfile(os.path.join(movies_dir, HP[0]))
        
        elif 'play chamber of secrets' in query:
            movies_dir = 'D:\\Harry Potter'
            HP = os.listdir(movies_dir)
            print(HP[1])
            os.startfile(os.path.join(movies_dir, HP[1]))
        
        elif 'play prisoner of azkaban' in query:
            movies_dir = 'D:\\Harry Potter'
            HP = os.listdir(movies_dir)
            print(HP[2])
            os.startfile(os.path.join(movies_dir, HP[2]))
        
        elif 'play goblet of fire' in query:
            movies_dir = 'D:\\Harry Potter'
            HP = os.listdir(movies_dir)
            print(HP[3])
            os.startfile(os.path.join(movies_dir, HP[3]))
        
        elif 'play order of phoenix' in query:
            movies_dir = 'D:\\Harry Potter'
            HP = os.listdir(movies_dir)
            print(HP[4])
            os.startfile(os.path.join(movies_dir, HP[4]))
        
        elif 'play half blood prince' in query:
            movies_dir = 'D:\\Harry Potter'
            HP = os.listdir(movies_dir)
            print(HP[5])
            os.startfile(os.path.join(movies_dir, HP[5]))
        
        elif 'play deathly hallows part 1' in query:
            movies_dir = 'D:\\Harry Potter'
            HP = os.listdir(movies_dir)
            print(HP[6])
            os.startfile(os.path.join(movies_dir, HP[6]))
        
        elif 'play deathly hallows part 2' in query:
            movies_dir = 'D:\\Harry Potter'
            HP = os.listdir(movies_dir)
            print(HP[7])
            os.startfile(os.path.join(movies_dir, HP[7]))
        
        elif 'play songs on youtube' in query:
            speak("which song do you want hear?")
            song = takeCommand().lower()
            kit.playonyt(song)
        
        #send whatsapp messages
        elif 'send a message to' in query:
            query = query.replace("send","")
            query = query.replace("message","")
            query = query.replace("to","")
            query = query.replace(" ","")
            query = query.replace("a","")
            Automation.whatsapp(query,contacts)
        
        elif 'make whatsapp call to' in query:
            from time import sleep
            query = query.replace("call","")
            query = query.replace(" ","")
            query = query.replace("make","")
            query = query.replace("whatsapp","")
            query = query.replace("to","")
            reci_name = query
            webbrowser.open("https://web.whatsapp.com/")
            sleep(15)
            click(x=195, y=115)
            sleep(2)
            write(reci_name)
            sleep(1)
            click(x=188, y=249)
            sleep(1)
            click(x=571, y=690)
            speak("Call starting 2 seconds")
            sleep(2)
            click(x=1198, y=63)

        elif 'send message in group' in query:
            print("In which group?")
            speak("In which group?")
            recipent_grp = takeCommand().lower()
            print(f"what message do you want to send to {recipent_grp}?")
            speak(f"what message do you want to send to {recipent_grp}?")
            message_grp = takeCommand().lower()
            grp = what_grp_diary[recipent_grp]
            whatsapp_grp(grp,message_grp)

        #set alarm   
        elif 'set alarm' in query:
            nn = int(datetime.datetime.now().hour)
            if nn==20:
                music_dir = 'D:\\Songs'
                songs = os.listdir(music_dir)
                os.startfile(os.path.join(music_dir, songs[0]))
    
        #tell jokes
        elif 'tell me a joke' in query:
            joke = pyjokes.get_joke()
            speak(joke)

        #Close applications
        elif 'close notepad' in query:
            speak("okay sir, closing notepad")
            os.system("TASKKILL /F /IM notepad.exe")
        
        elif 'close word' in query:
            speak("okay sir, closing word")
            os.system("TASKKILL /F /IM WINWORD.exe")
        
        elif 'close excel' in query:
            speak("okay sir, closing excel")
            os.system("TASKKILL /F /IM EXCEL.exe")

        elif 'close powerpoint' in query:
            speak("okay sir, closing powerpoint")
            os.system("TASKKILL /F /IM POWERPNT.exe")

        elif 'close chrome' in query:
            speak("okay sir, closing chrome")
            os.system("TASKKILL /F /IM chrome.exe")

        elif 'close keyboard' in query:
            speak("okay sir, closing keyboard")
            os.system("TASKKILL /F /IM osk.exe")

        elif 'close edge' in query:
            speak("okay sir, closing edge")
            os.system("TASKKILL /F /IM msedge.exe")
        
        elif 'close winrar' in query:
            speak("okay sir, closing winrar")
            os.system("TASKKILL /F /IM WinRaR.exe")

        elif 'close code' in query:
            speak("okay sir, closing code")
            os.system("TASKKILL /F /IM code.exe")

        elif 'close calculator' in query:
            speak("okay sir, closing calculator")
            os.system("TASKKILL /F /IM calc.exe")

        elif 'close zoom' in query:
            speak("okay sir, closing zoom")
            os.system("TASKKILL /F /IM zoom.exe")

        elif 'close math input panel' in query:
            speak("okay sir, closing math input panel")
            os.system("TASKKILL /F /IM mip.exe")

        elif 'close paint' in query:
            speak("okay sir, closing paint")
            os.system("TASKKILL /F /IM mspaint.exe")

        elif 'close snip' in query:
            speak("okay sir, closing snipping tool")
            os.system("TASKKILL /F /IM Snipping Tool.exe")

        elif 'close python' in query:
            speak("okay sir, closing python")
            os.system("TASKKILL /F /IM pythonw.exe")
        
        elif 'close adobe' in query:
            speak("okay sir, closing adobe")
            os.system("TASKKILL /F /IM acrobat.exe")

        elif 'close onenote' in query:
            speak("okay sir, closing onenote")
            os.system("TASKKILL /F /IM onenote.exe")
        
        elif 'close unity hub' in query:
            speak("okay sir, closing unity hub")
            os.system("TASKKILL /F /IM Unity Hub.exe")

        elif 'close studio' in query:
            speak("okay sir, closing studio")
            os.system("TASKKILL /F /IM devenv.exe")

        elif 'close cmd' in query:
            speak("okay sir, closing command prompt")
            os.system("TASKKILL /F /IM cmd.exe")
        
        elif 'close run' in query:
            speak("okay sir, closing run")
            os.system("TASKKILL /F /IM run.exe")

        #Perform functions like Shutdown, Restart or sleep
        elif 'shutdown pc' in query:
            os.system("shutdown /s /t 5")

        elif 'restart pc' in query:
            os.system("restart /s /t 5")

        elif 'send pc to sleep' in query:
            os.system("sleep /s /t 5")
        
        elif 'switch window' in query:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.keyUp("alt")
        
        #tell latest news
        elif 'tell me some news' in query:
            speak("please wait sir, fetching latest news")
            main_url = 'http://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=83263a48521a48a797182dbc3926e513'
            main_page = requests.get(main_url).json()
            articles = main_page["articles"]
            head = []
            day = ["first","second","third","fourth","fifth"]
            for ar in articles:
                head.append(ar["title"])
            for i in range(len(day)):
                speak(f"today's {day[i]} news is: {head[i]}")
        
        #ip address
        elif 'ip address' in query:
            print("your IP address is 47.31.128.168")
            speak(f"your IP address is 47.31.128.168")    

        #tell our info like ip address, city and country
        elif 'info' in query:
            url = 'http://ipinfo.io/json'
            response = urlopen(url)
            data = json.load(response)

            IP=data['ip']
            org=data['org']
            city = data['city']
            country=data['country']
            region=data['region']
            print ('Your IP detail\n ')
            print ('IP : {4} \nRegion : {1} \nCountry : {2} \nCity : {3} \nOrg : {0}'.format(org,region,country,city,IP))
            speak(f"your IP address is 47.31.128.168, your location is in {city} city of {country}.")

        #takes screenshot
        elif 'screenshot' in query:
            speak("sir, please tell me the name of screenshot")
            name_ss = takeCommand().lower()
            speak("please hold the screen for a while, I am taking screenshot")
            myScreenshot = pyautogui.pyscreeze.screenshot()
            myScreenshot.save(f"{name_ss}.png")
            speak("I am done sir, you can continue your work")
            
        #audiobook
        elif 'read pdf' in query:
            speak("which pdf do you want read?")
            path = eval(input("Which pdf do you want read? --> "))
            book = open(f"{path}", 'rb')
            pdfReader = PyPDF2.PdfFileReader(book)
            tot_pages = pdfReader.numPages
            speak(f"Total numbers of pages in this book are {tot_pages} ")
            speak("In which language, I should read?")
            lang = takeCommand().lower()
            speak("sir please tell the page number i have to read")
            pg = int(takeCommand().lower())
            speak("till which page")
            pages = int(takeCommand().lower())
            if 'english' in lang:
                for page_num in range(pg, pages):
                    page = pdfReader.getPage(page_num)
                    text = page.extractText()
                    speak(text)
            elif 'Hindi' in lang:
                for page_num in range(pg, pages):
                    page = pdfReader.getPage(page_num)
                    text = page.extractText()
                    transl = Translator()
                    textHin = transl.translate(text, 'hi')
                    textm = textHin.text
                    speech = gTTS(text = textm)
                    try:
                        speech.save('book.mp3')
                        PlaySound('book.mp3')
                    except:
                        winsound.PlaySound('book.mp3')
        
        #working with pdf
        elif 'give me pdf details' in query:
            speak("which pdf info do you want?")
            path = eval(input("Which pdf info do you want?  --> "))    
            with open(path, 'rb') as f:
                pdf = PyPDF2.PdfFileReader(f)
                information = pdf.getDocumentInfo()
                number_of_pages = pdf.getNumPages()

            txt = (f"Information about {path}, Author: {information.author}, Creator: {information.creator}, Subject: {information.subject}, Number of Pages: {number_of_pages}")
            print(txt)
            speak(txt)
        
        elif 'rotate pages' in query:
            speak("of which pdf, do you want to rotate pages?")
            path = eval(input("of which pdf, do you want to rotate pages?"))
            book = open(path, 'rb')
            pdfReader = PyPDF2.PdfFileReader(book)
            pages = pdfReader.numPages
            speak(f"Total numbers of pages in this book are {pages} ")
            speak("sir please tell the page number i have to read")
            pg = int(takeCommand().lower())
            for page_num in range(pg, pages):
                page = pdfReader.getPage(page_num)
                text = page.extractText()
                speak(text)
        
        elif 'merge pdf' in query:
            def merge_pdf(paths, output):
                pdf_writer = PyPDF2.PdfFileWriter()
                for path in paths:
                    pdf_reader = PyPDF2.PdfFileReader(path)
                    for page in range(pdf_reader.getNumPages()):
                        pdf_writer.addPage(pdf_reader.getPage(page))
                with open(output, 'wb') as out:
                    pdf_writer.write(out)
            
            speak("write name of pdf you want to merge in list")
            paths = eval(input("Write name of pdf you want to merge in a list --> "))
            speak("give name for merged pdf")
            pdf_mergedname = takeCommand().lower()    
            merge_pdf(paths, output= f'{pdf_mergedname}.pdf')

        #send PAPPU on sleep
        elif 'sleep' in query:
            speak("Okay sir, I am going to sleep you can call me anytime.")
            pass

        '''else:
            from Chatbot import ChatterBot
            reply = ChatterBot(query)
            speak(reply)
            if 'bye' in query:
                pass
            elif 'exit' in query:
                pass
            elif 'go' in query:
                pass'''

if __name__ == "__main__":
    permission = takeCommand().lower()
    if 'wake up' in permission:
        TaskExecution()
    elif 'goodbye' in permission:
        speak("Goodbye sir!")
        sys.exit()
