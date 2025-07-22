import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests
import pyaudio
from google import genai


recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "YOUR API KEY"

def speak(text):
    engine.say(text)
    engine.runAndWait()

def aiProcess(command):
    client = genai.Client(api_key="YOUR API KEY")
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
        speak(output)


if __name__ == "__main__":
    speak("Initializing Jarvis..!")
    while True:
        #Listen for the wake word "Jarvis"
        #obtain audio from the microphone
        r = sr.Recognizer() 
        print("Recognizing...")

        # recognize speech using Google
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=2, phrase_time_limit=1)
            word = r.recognize_google(audio)
            
            #Catch the wake command "jarvis"
            if(word.lower() == "jarvis"):
                speak("Yes")

                #Listen for command
                with sr.Microphone() as source:
                    print("Jarvis Active... ")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processCommand(command)

        except Exception as e:
            print("Error; {0}".format(e))




