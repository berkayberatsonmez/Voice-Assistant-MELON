#-------This Code written by BBS-------#
import pyttsx3
import speech_recognition as sr
import pyaudio
import datetime
import wikipedia
import webbrowser
import os
import requests
import smtplib
import platform,re,json,psutil
import wmi
import time
import getpass
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import pyautogui
from subprocess import call
import winshell
import pyjokes


base= "C:\\Users\\berka\\Desktop\\melonfiles\\melonfiles" #change this part

file="C:\\Users\\berka\\Desktop\\Masaüstü\\melon\\melon.py" #change this part

computer = wmi.WMI()
computer_info = computer.Win32_ComputerSystem()[0]
os_info = computer.Win32_OperatingSystem()[0]
proc_info = computer.Win32_Processor()[0]
gpu_info = computer.Win32_VideoController()[0]

os_name = os_info.Name.encode('utf-8').split(b'|')[0]
os_version = ' '.join([os_info.Version, os_info.BuildNumber])
system_ram = float(os_info.TotalVisibleMemorySize) / 1048576 

weather_url="http://api.openweathermap.org/data/2.5/weather?q=Eskisehir,tr&APPID=346e058598e615649450c4eafa477ae7"
response= requests.get(weather_url)
jsonResponse = json.loads(response.text)
temperature = jsonResponse["main"]["temp"] - 273
b = str(round(temperature,2))

chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe %s" #change this part

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
engine.setProperty('rate', 175)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('senin mail adresin', 'şifren')
    server.sendmail('senin mail adresin', to, content)
    server.close()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>= 6 and hour<12:
        speak("Good Morning ")
    elif hour>=12 and hour<18:
            speak("Good Afternoon ")
    elif hour>=18 and hour<24:
            speak("Good evening ")
    else:
                speak("Good Night ")

    speak("Today,"+ datetime.datetime.now().strftime("%d %B ,%Y ,%A"))
    speak("it's "+ datetime.datetime.now().strftime("%H:%M:%S")+ " o'clock ")
    speak("the weather is " + b + " centigrade"+ " today" )
    if 0<temperature<15:
        speak("The weather is not bad today, you still be careful ")
    elif -15<temperature<0:
        speak("It might be cold today, be careful ")
    elif temperature<-15:
        speak("It's very cold today, I think you should dress warmly ")
    else:
        speak("The weather is hot and nice today, be careful, don't sweat too much ")

    speak("When you need me, just say melon sir")

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
                print("say that again please..")
                return "none"
            return query

if __name__ == "__main__":      # melon commands are here. You can do whatever you want to do to melon.
   wishMe()

   while True:
     query = takeCommand().lower()
    
     if 'melon' in query:
       speak("How can ı help you sir")
       while True:
           
        query = takeCommand().lower()
        if 'wikipedia' in query:
           speak('Searching Wikipedia...')
           query = query.replace("wikipedia","")
           results = wikipedia.summary(query, sentences=2)
           webbrowser.get(chrome_path).open("https://en.wikipedia.org/wiki/" + query)
           speak("According to Wikipedia")
           print(results)
           speak(results)

        elif 'open youtube' in query:
           webbrowser.get(chrome_path).open("youtube.com")

        elif 'open google' in query:
           webbrowser.get(chrome_path).open("google.com")

        elif 'who are you' in query:
           speak('You already know who I am sir')

        elif 'what is time' in query:
           strTime = datetime.datetime.now().strftime("%H:%M:%S")
           print(strTime)
           speak(strTime + "o'clock")
       
        elif "what's time" in query:
           strTime = datetime.datetime.now().strftime("%H:%M:%S")
           print(strTime)
           speak(strTime + "o'clock")
       
        elif 'what is the time' in query:
           strTime = datetime.datetime.now().strftime("%H:%M:%S")
           print(strTime)
           speak(strTime + "o'clock")
       
        elif 'are you still there' in query:
           speak('Of course sir')
       
        elif 'I miss you' in query:
               speak('I miss you too sir')
      
        elif 'are you there' in query:
           speak('Of course sir')
      
        elif 'league of legends' in query:
           speak("league of legends is opening")
           lolPath  = "C:\\Riot Games\\League of Legends\\LeagueClient.exe" #change this part
           os.startfile(lolPath)
      
        elif 'how are you' in query:
           speak('I am fine sir , how are you?')
       
        elif 'fine' in query:
           speak('Glad to hear that sir')
      
        elif 'bad' in query:
           speak('Is there anything I can help, sir')
           speak("Would you like to listen to something sir?")
           query = takeCommand().lower()
           if 'yes' in query:
               speak("what would you like to listen sir?")
               query = takeCommand().lower()
               speak("I will open" + query)
               music(query.split('play')[1])
           else:
                speak("If you need anything, I'm here sir") 
      
        elif 'no thank' in query:
           speak('Roger sir') 
      
        elif 'no thanks' in query:
           speak('Roger sir') 
      
        elif 'search google' in query:
           speak('Searching in google...')
           query = query.replace("search google","")
           webbrowser.get(chrome_path).open("https://www.google.com/search?q=" + query)
        elif 'search' in query:
           speak('Searching in google...')
           query = query.replace("search","")
           webbrowser.get(chrome_path).open("https://www.google.com/search?q=" + query)
        elif 'what is the' in query:
           query = query.replace("what is the","")
           speak('I am searching'+query+'in google...')
           query = query.replace("what is the","")
           webbrowser.get(chrome_path).open("https://www.google.com/search?q=" + query)

        elif 'thank you' in query:
           speak('whenever you want sir')
      
        elif 'hello' in query:
           speak('hello sir')
       
        elif 'in youtube' in query:
           speak('opening in youtube..')
           query = query.replace("in youtube","")
           webbrowser.get(chrome_path).open("https://www.youtube.com/results?search_query=" + query)
      
        elif 'system off' in query or 'bye' in query or 'you can go for now' in query or 'quit' in query or 'goodbye' in query or 'exit' in query:
           speak('Goodbye sir')
           break;
            
        elif 'i love you' in query:
           speak('I love you too sir')
      
        elif 'what\'s your name' in query:
           speak("My name is melon sir")
      
        elif 'when were you born' in query:
           speak('I was born in 16 March , 2020')
      
        elif 'who is admin' in query:
           speak("I don't know but everybody usually call him BBS ")
      
        elif 'open code' in query:
           codePath = "C:\\Users\\berka\\Desktop\\Masaüstü\\melon\\melon.py" #change this part
           os.startfile(codePath)
           speak('this is my code')
      
        elif 'email to' in query:
            try:
                speak("What should I say sir")
                content = takeCommand()
                to = "kime gönderilcekse buraya gir ama google maildan daha az güvenli uygulamaları etkinleştir i unutma"    
                sendEmail(to, content)
                speak("Email has been sent sir")
            except Exception as e:
                print(e)
                speak("Sorry my sir. I am not able to send this email")  
      
        elif 'open linked' in query:
            webbrowser.get(chrome_path).open("https://www.linkedin.com/in/berkay-berat-s%C3%B6nmez-4b43181a7/")
      
        elif 'open github' in query:
            webbrowser.get(chrome_path).open("https://github.com/berkayberatsonmez") 
      
        elif 'open binance' in query:
            webbrowser.get(chrome_path).open("https://www.binance.com/tr")
      
        elif 'open website' in query:
            query = query.replace("open website","")
            speak(query+"is opening")
            webbrowser.get(chrome_path).open(query+".com")
      
        elif 'weather' in query:
            speak("the weather is " + b + " centigrade"+ " now" )
            if 0<temperature<15:
                speak("The weather is not bad today, you still be careful sir")
            elif -15<temperature<0:
                speak("It might be cold today, be careful sir")
            elif temperature<-15:
                speak("It's very cold today, I think you should dress warmly sir")
            else:
                speak("The weather is hot and nice today, be careful, don't sweat too much sir")
      
        elif 'are you ready' in query:
            speak("I have already ready sir")        
       
        elif 'open translate' in query:
            webbrowser.get(chrome_path).open("https://translate.google.com/")
      
        elif 'when file change' in query:  
            print("last modified: %s" % time.ctime(os.path.getmtime(file)))          
            speak("last modified: %s" % time.ctime(os.path.getmtime(file)))

        elif 'when file create' in query:  
            print("created: %s" % time.ctime(os.path.getctime(file)))          
            speak("created: %s" % time.ctime(os.path.getctime(file)))
     
        elif 'system info' in query:
            speak('OS Name is: {0}'.format(os_name))
            speak('OS Version is: {0}'.format(os_version))
            speak('CPU is: {0}'.format(proc_info.Name))
            speak('RAM is: ' + str(round(psutil.virtual_memory().total / (1024.0 **3))) + "GigaByte")
            speak('Graphics Card is: {0}'.format(gpu_info.Name))
      
        elif 'shut down computer' in query:
            speak("Do you wish to shutdown your computer sir?")
            query = takeCommand().lower()
            if 'yes' in query:
                speak("computer shuts down, goodbye sir")
                os.system("shutdown /s /t 1")
                break
            else:
                speak("The shutdown process has been aborted sir.")
      
        elif 'reboot computer' in query:
            speak("Do you wish to reboot your computer sir?")
            query = takeCommand().lower()
            if 'yes' in query:
                speak("computer rebooting, goodbye sir")
                os.system("shutdown -t 0 -r -f")
                break
            else:
                speak("The reboot process has been aborted sir.")
      
        elif 'sleep time' in query:
            speak("Do you wish to sleep your computer sir?")
            query = takeCommand().lower()
            if 'yes' in query:
                speak("have a nice sleep sir")
                os.system("shutdown -h")
            else:
                speak("The sleep process has been aborted sir.")
       
        elif 'start over yourself' in query:
            speak("system rebooting")
            wishMe()
      
        elif 'change file name' in query:
            speak("Be careful, The files should be in the melonfiles.")
            speak("what is the file extansion")
            query = takeCommand().lower()
            while True:
                if 'py' in query:
                    extansion="py"
                    break
                elif 'txt' in query:
                    extansion ="txt"
                    break
                elif 'text' in query:
                    extansion ="txt"
                    break
                elif 'png' in query:
                    extansion ="png"
                    break
                elif 'jpg' in query:
                    extansion ="jpg"
                    break
                elif 'images' in query:
                    extansion ="jpg"
                    break
                elif 'jpeg' in query:
                    extansion ="jpeg"
                    break
                elif 'mp4' in query:
                    extansion ="mp4"
                    break
                elif 'video' in query:
                    extansion ="mp4"
                    break
                elif 'mp3' in query:
                    extansion ="mp3"
                    break
                elif 'gif' in query:
                    extansion ="gif"
                    break
                elif 'webp' in query:
                    extansion ="webp"
                    break
                elif 'html' in query:
                    extansion ="html"   
                    break 
                else:
                    speak("sorry sir, ı don't know this extansion")
                    speak("what is the file extansion")
                    query = takeCommand().lower()
            speak("Which file's name will change sir?")
            query = takeCommand().lower()
            if 'melon' in query:
                speak("are you sure about that sir, cause this is my code file's name, If I change it, I may not be able to work again")
                query = takeCommand().lower()
                if 'yes' in query:
                    speak("sorry ı can not do this sir")
                    break
                else:
                    speak("okey sir")
                    break
            else:
                firstfilename=query
                speak("What is the new file name sir?")
                query = takeCommand().lower()
                secondfilename=query
                speak("the replacement process is starting..")
                os.rename(os.path.join(base,firstfilename+"."+extansion), os.path.join(base,secondfilename+"."+extansion))
                speak("the replacement process is finished..")

        elif 'countdown' in query:
           t=5
           while t >= 0:
               speak(t)
               t-=1
               time.sleep(0.1)

        elif 'create new file' in query:
            speak("Be careful, you need have a file which name is melonfiles in your desktop")
            speak("what is the file extansion sir")
            query = takeCommand().lower()
            while True:
                if 'py' in query:
                    extansion="py"
                    break
                elif 'txt' in query:
                    extansion ="txt"
                    break
                elif 'text' in query:
                    extansion ="txt"
                    break
                elif 'png' in query:
                    extansion ="png"
                    break
                elif 'images' in query:
                    extansion ="jpg"
                    break
                elif 'jpg' in query:
                    extansion ="jpg"
                    break
                elif 'jpeg' in query:
                    extansion ="jpeg"
                    break
                elif 'mp4' in query:
                    extansion ="mp4"
                    break
                elif 'video' in query:
                    extansion ="mp4"
                    break
                elif 'mp3' in query:
                    extansion ="mp3"
                    break
                elif 'gif' in query:
                    extansion ="gif"
                    break
                elif 'webp' in query:
                    extansion ="webp"
                    break
                elif 'html' in query:
                    extansion ="html" 
                    break   
                else:
                    speak("sorry sir, ı don't know this extansion")
                    speak("what is the file extansion")
                    query = takeCommand().lower()
            speak("What is the file name sir?")
            query = takeCommand().lower()
            newfilename=query  
            speak("I'm creating a new file.")
            newfile= open(os.path.join(base,newfilename+"."+extansion,),'a+')
            speak("Do you want to write anything in this file sir?")
            query = takeCommand().lower()
            if 'yes' in query:
                speak("what would you like me to write sir?")
                query = takeCommand().lower()
                newfile.write(query)
                newfile.close()
                speak("Would you like me to read what you wrote sir?")
                query = takeCommand().lower()
                if 'yes' in query:
                    f= open(os.path.join(base,newfilename+"."+extansion,),'r')
                    speak(f.read())
                    speak("Do you want to add anything in this file sir?")
                    query = takeCommand().lower()
                    if 'yes' in query:
                        speak("what would you like me to write sir?")
                        query = takeCommand().lower()
                        newfile.write(query)
                        newfile.close()
                        speak("please check your melonfiles in your desktop")
                    else:
                        newfile.close()
                        speak("please check your melonfiles in your desktop")
                else:  
                    newfile.close()                  
                    speak("please check your melonfiles in your desktop")               
            else:
                newfile.close()
                speak("please check your melonfiles in your desktop")
                
        elif 'play' in query:
            speak("If you want to play something please close your browsers but don't worry ı will open a browser for you.")
            options = webdriver.ChromeOptions()
            options.add_argument("user-data-dir=C:\\Users\\" + getpass.getuser() + "\\AppData\\Local\\Google\\Chrome\\User Data")
            driver = webdriver.Chrome("C:\\Users\\berka\\Desktop\\Masaüstü\\melon\\chromedriver.exe", chrome_options=options)
            def music(song):
                driver.get("https://www.youtube.com/results?search_query=" + song)
                delay = 3
                myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, 'video-title')))
                driver.find_element_by_css_selector("a[id='video-title']").click()
                speak(song + " is playing")
            music(query.split('play')[1])

        elif "I am tired" in query:
           speak('Is there anything I can help')
           speak("Would you like to listen to something sir?")
           query = takeCommand().lower()
           if 'yes' in query: 
               speak("If you want to play something please close your browsers but don't worry ı will open a browser for you.")
               options = webdriver.ChromeOptions()
               options.add_argument("user-data-dir=C:\\Users\\" + getpass.getuser() + "\\AppData\\Local\\Google\\Chrome\\User Data")
               driver = webdriver.Chrome("C:\\Users\\berka\\Desktop\\Masaüstü\\melon\\chromedriver.exe", chrome_options=options)       
               speak("what would you like to listen sir?")
               query = takeCommand().lower()
               speak("I will open" + query)
               def music(song):
                    driver.get("https://www.youtube.com/results?search_query=" + song)
                    delay = 3
                    myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, 'video-title')))
                    driver.find_element_by_css_selector("a[id='video-title']").click()
                    speak(song + " is playing")
               music(query.split()[1])
               
           else:
               speak("If you need anything, I'm here sir")

        elif 'return to the previous song' in query:       
            driver.back()

        elif 'turn off sound' in query:       
            driver.quit()  

        elif 'open clip' in query:       
            driver.maximize_window()

        elif 'take screenshot' in query:
            while True:
                speak("what is the screenshot name sir?")
                query = takeCommand().lower()
                time.sleep(3)
                t=3
                while t >= 0:
                    speak(t)
                    t-=1
                    time.sleep(0.1)
                pyautogui.screenshot("C:\\Users\\berka\\Masaüstü\\melonfiles\\"+query+".png")
                speak("you can check melon files")
                break
        
        elif 'open calculator' in query:
            speak("calculator is opening")
            call(["calc.exe"])

        elif 'open' in query:
            query = query.replace("open","")
            speak(query+"is opening")
            call([query+".exe"])

        elif 'find' in query:
            query = query.replace("find","")
            speak(query+"is finding")
            webbrowser.get(chrome_path).open("https://google.nl/maps/place/"+query+"/&amp;")
            
        elif 'empty recycle' in query:
            winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)
            speak("Recycle Bin Recycled")
        
        elif "where is" in query:
            query = query.replace("where is", "")
            location = query
            speak(query+"is here")
            webbrowser.open("https://www.google.nl/maps/place/" + location + "")
        
        elif 'joke' in query:
            speak(pyjokes.get_joke())

        else:
            speak("Do you need anything else sir?")
            query = takeCommand().lower()
            if 'yes' in query:
                speak("I am listening you sir")
                continue
            else:    
                speak("When you need me, just say melon and wait sir")
                break
                             
     elif 'turn off yourself' in query:
        speak("if you need me, just run my file.")
        speak("Goodbye sir.")
        break       
