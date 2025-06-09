import pyttsx3
import datetime
import speech_recognition as sr

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning Kay!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon Kay!")

    else:
        speak("Good Evening Kay!")

    speak("Hii, I am Optimus, Please tell me how may I help you ")

def takeCommand():
    
if __name__ == "__main__":
    wishMe()
