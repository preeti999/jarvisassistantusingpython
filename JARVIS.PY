import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os




engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
#print(voices)
engine.setProperty('voice',voices[0].id)



def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("I am Jarvis Sir.Please tell me how may i help you") 
def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio=r.listen(source)
    try:
        print("Recognising...")
        query=r.recognize_google(audio,language='en=in')
        print(f"user said:(query)\n")
    except Exception as e:
        print(e)
        print('Say that again please')
        return "None"
    return query
def sendEmail(to,content):
    server = smptlib.SMTP('smpt.gamil.com',587)  
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com','your-password')
    server.sendEmail('youremail@gmail.com',to,content)
    server.close()


if __name__ == "__main__":
    wishMe()
    #while True:
    if 1:
        query=takeCommand().lower()
        if 'wikipedia' in query:
            speak('Searching wikipedia...')
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        elif 'play music' in query:
            music_dir="D:\\songs"
            songs=os.listdir(music_dir)                
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))
        elif 'the time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir,the time is {strTime}")    
        elif 'open code' in query:
            codePath="C:\\users\\ashis\\AppData\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath) 
        elif "Email to kindi" in query:
            try:
                speak("What shoud i write?")
                content=takeCommand()
                to="TomyourEmail@gmail.com"
                sendEmail(to,content)
                speak("Email has been sent")
            except Exception as e:
                print(e)
                speak("Sorry mr tom I am not able to sent this Email")

                