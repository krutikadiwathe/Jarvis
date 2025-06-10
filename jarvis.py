import pyttsx3
import datetime
import wikipedia
import webbrowser
import subprocess
import os
import requests
import speech_recognition as sr

import spotipy
from spotipy.oauth2 import SpotifyOAuth


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice', voices[1].id)



def play_spotify_playlist():
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
        client_id='b97707897cd94f4f95846e0afe23307d',
        client_secret='800cf4d7daae4d0093b8ea472c05ddbd',
        redirect_uri='http://127.0.0.1:8888/callback',
        scope='user-read-playback-state user-modify-playback-state'
    ))

    devices = sp.devices()
    print("Devices:", devices)

    if devices['devices']:
        device_id = devices['devices'][0]['id']  # pick first device
        sp.start_playback(device_id=device_id, context_uri="spotify:playlist:7sNVJ2OGqfZQubxu2NrjfT")
    else:
        print("⚠️ No active Spotify device found. Open Spotify and play something once.")

def pause_spotify_music():
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
        client_id='b97707897cd94f4f95846e0afe23307d',
        client_secret='800cf4d7daae4d0093b8ea472c05ddbd',
        redirect_uri='http://127.0.0.1:8888/callback',
        scope='user-read-playback-state user-modify-playback-state'
    ))

    sp.pause_playback()


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def tell_joke():
    headers = {"Accept": "application/json"}
    res = requests.get("https://icanhazdadjoke.com/", headers=headers)
    if res.status_code == 200:
        joke = res.json()['joke']
        speak(joke)
    else:
        speak("Sorry, I couldn't find a joke right now.")

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

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said:{query}\n")

    except Exception as e:
       # print(e)

        print("Say that again please...")
        return "None"
    return query

if __name__ == "__main__":
    wishMe()
    while True:
    
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=1)  
            speak("According to Wikipedia")
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open('youtube.com')

        elif 'open google' in query:
            webbrowser.open('google.com')

        elif 'open stackoverflow' in query:
            webbrowser.open('stackoverflow.com')

        elif 'open linkedin' in query:
            webbrowser.open('linkedin.com')

        elif 'play music' in query or 'open spotify' in query:
            speak("Playing your playlist on Spotify...")
            play_spotify_playlist()

        elif 'pause music' in query or 'stop music' in query:
            speak("Pausing music on Spotify...")
            pause_spotify_music()

        elif 'open spotify' in query:
            speak("Opening Spotify app.")
            subprocess.Popen(
                r'explorer shell:AppsFolder\SpotifyAB.SpotifyMusic_zpdnekdrzrea0!Spotify'
            )

        elif 'the time'in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Kay, the time is {strTime}")

        elif "open code" in query:
            codePath = r"C:\Users\KRUTIKA\AppData\Local\Programs\Microsoft VS Code\Code.exe"
            os.startfile(codePath)

        elif 'tell me a joke' in query:
            speak("Sure! Here's one:")
            tell_joke()

        elif 'stop' in query or 'exit' in query or 'quit' in query:
            speak("Okay Kay, shutting down. Have a great day!")
            break

        elif 'my name' in query:
            speak("Your name is Krutika, Everyone calls you kay")




        

