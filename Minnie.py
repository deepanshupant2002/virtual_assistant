import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour <12:
        speak("Gud Morning!")
    elif hour >=12 and hour <18:
        speak("Gud Afternoon!")
    else:
        speak("Gud Evening!")

    speak("I am Minnie. Sir,please tell me how may i help you!")

def takeCommand():
    # it takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognising...")
        query = r.recognize_google(audio,language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query


wishMe()
while True:
    query = takeCommand().lower()
    if 'wikipedia' in query:
        speak('Searching Wikipedia..')
        query = query.replace("wikipedia","")
        results = wikipedia.summary(query,sentences=2)
        speak("According to Wikipedia")
        speak(results)
        print(results)
# logic for executing task based on query
    elif "quit" in query:
        break
    
    elif 'open youtube' in query:
        webbrowser.open("youtube.com")
    elif "open google" in query:
        webbrowser.open('google.com')
    elif 'open stack overflow' in query:
        webbrowser.open('stackoverflow.com')
    elif 'the time' in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"Sir,the time is {strTime}")
    # elif 'email to deepu' in query:
    #     try:
    #         speak("what should i say")
    #         content =takeCommand()
    #         to ="deepupant2002@gmail.com"
    #         sendEmail(to,content)
    #         speak("email has been sent!")
    #     except Exception as e:
    #         print(e)
    #         speak("sorry my bro i m unable1")