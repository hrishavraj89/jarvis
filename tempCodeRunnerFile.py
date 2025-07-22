import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests
import pyaudio
from google import genai


recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "a62e6d323b0f4708abfcb67798c89a79"

def speak(text):
    engine.say(text)
    engine.runAndWait()

def aiProcess(command):
    client = genai.Client(api_key="AIzaSyAnXX_6HHbgS8DLqDyPjCpuMZGq0ww6J2M")
    response = client.models.generate_content(
    model="gemini-2.5-flash", contents=command)
    return response.text

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open instagram" in c.lower():
        webbrowser.open("https://instagram.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)
    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}")
        if r.status_code == 200:
            #Parse the json response
            data = r.json()
            #Extract the articles
            articles = data.get("articles", [])
            #Print the headlines
            print("Top News Headlines:\n")
            for idx, article in enumerate(articles, 1):
                speak(article['title'])

    else:
        #Let gemini handle the request!
        speak("Let me think...")
        output = aiProcess(c)