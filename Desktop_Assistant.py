import pyttsx3 #pip install pyttsx3
import datetime
import speech_recognition as sr #pip install speechRecognition  #pip install pipwin  #pip install pyaudio
import wikipedia # pip install wikipedia
import webbrowser
import os
import tkinter as tk
from PIL import Image,ImageTk
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voices",voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def hello():
    hour = int(datetime.datetime.now().hour)
    if hour>0 and hour<12:
        speak("Good Morning")
    elif hour>12 and hour<18:
        speak("Good Afternoon ")
    else:
        speak("Good Evening")
    
    speak("Hello Sir, I am your desktop assistant, How may i help you")

def UserCommand():
    #it takes microphone input and rerturn string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        speak("What's your Query Sir")
        print("Listening...")
        r.pause_threshold = 1
        audio = r. listen(source)
    try:
        print("Recognizing...")
        speak(" Okay Sir")
        query = r.recognize_google(audio,language="en-in")
        print(f"User said:{query}\n")
    except Exception as e:
        print(e)
        print("Say that again please...")
        return "None"
    return query
def start():
    
    hello()
    
    #logic to execute task based on query
    while True:
        query = UserCommand().lower()
        if "wikipedia" in query:
            speak("searching wikipedia")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif "open youtube" in query:
            webbrowser.open("youtube.com")

        elif "open google" in query:
            webbrowser.open("google.com")

        elif "open stackoverflow" in query:
            webbrowser.open("stackoverflow.com")

        elif "time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir time is {strTime}")

        elif "open vs code" in query:
            codePath="C:\\Users\\Gaurav Dutt Misra\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
            
        elif "quit" in query:
            speak('It feels great to help you, come back again when needed')
            exit()
        


if __name__=="__main__":
    decision1=tk.Tk()
    decision1.geometry('400x400')
    decision1.configure(background='black')
    username_label=tk.Label(decision1,text="This is your Desktop Assistant",font="calibre 20 bold",fg="black")
    username_label.pack()
    button=tk.Button(decision1,text="Let's Start",command=start)
    button.pack()
    
