import pyttsx3
import speech_recognition as sr
import pyaudio
import datetime
import wikipedia
import webbrowser
import os


chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe %s" 

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice',voices[1].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>= 0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
            speak("Good Afternoon")
    else:
                speak("Good Evening!")
                
    speak("I am Melon sir! , How may I help you")
def takeCommand():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 1
            audio = r.listen(source)
            
            try:
                print("recognizing...")
                query = r.recognize_google(audio, language='tr-tr')
                query = r.recognize_google(audio, language='en-tr')
                print(query)
            except Exception as e:
                print(e)
                print("say that again please..")
                return "none"
            return query
if __name__ == "__main__":
   wishMe()
   while True:
       query = takeCommand().lower()
       
       if 'wikipedia' in query:
           speak('Searching Wikipedia...')
           query = query.replace("Wikipedia","")
           results = wikipedia.summary(query, sentences=2)
           speak("According to Wikipedia")
           print(results)
           speak(results)
       elif 'open youtube' in query:
           webbrowser.get(chrome_path).open("youtube.com")
       elif 'open google' in query:
           webbrowser.get(chrome_path).open("google.com")
       elif 'who are you' in query:
           speak('You already know who I am sir')
       elif 'time' in query:
           strTime = datetime.datetime.now().strftime("%H:%M:%S")
           print(strTime)
           speak(strTime)
       elif 'are you still there' in query:
           speak('Of course sir')
       elif 'are you there' in query:
           speak('Of course sir')
       elif 'melon' in query:
           speak('sir')
       elif 'how are you' in query:
           speak('I am fine sir , how are you')
       elif 'fine' in query:
           speak('Glad to hear that sir')
       elif 'bad' in query:
           speak('Is there anything I can help, sir') 
       elif 'no thank' in query:
           speak('Roger sir') 
       elif 'no thanks' in query:
           speak('Roger sir') 
       elif 'search google' in query:
           speak('Searching in google...')
           query = query.replace("search google","")
           webbrowser.get(chrome_path).open("https://www.google.com/search?q=" + query)
       elif 'thank you' in query:
           speak('No problem sir')
       elif 'hello' in query:
           speak('hello sir')
       elif 'in youtube' in query:
           speak('opening in youtube..')
           query = query.replace("in youtube","")
           webbrowser.get(chrome_path).open("https://www.youtube.com/results?search_query=" + query)
       elif 'system off' in query:
           speak('Goodbye sir')
           break;
       elif 'bye' in query:
           speak('Goodbye sir')
           break;
       elif 'goodbye' in query:
           speak('Goodbye sir')
           break;
       elif 'what\'s your name' in query:
           speak("My name is melon sir")
       