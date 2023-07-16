import pyttsx3 # pip install pyttsx3
import datetime
import speech_recognition as sr # pip install speechRecognition
import wikipedia
import webbrowser
import os
import smtplib

'''
    Commands provided :--

    1.) Search <anything> on wikipedia
    2.) Open Youtube
    3.) Open Google
    4.) Open StackOverFlow
    5.) Play Music
    6.) The time
    7.) Open code
    8.) What you can do
    9.) Email for me
    10.) Exit
'''

engine = pyttsx3.init('sapi5') # Voices set in variable engine.
voices = engine.getProperty('voices') # Get all the voices in voices variable
# print(voices) # Two voices available bydefault (Male & Female)
engine.setProperty('voice',voices[1].id) # Voice 0 for male & Voice 1 for female

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour < 12:
        speak("Good Morning User, Hii i am your assistance. What can i do for you ??")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon User, Hii i am your assistance. What can i do for you ??")
    else:
        speak("Good Evening User, Hii i am your assistance. What can i do for you ??")

def takeCommand():
    '''
        It takes microphone input from the user and and returns string output.
    '''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print("User said", query)

    except Exception as e:
        print(e)
        print("Say that again please !!!")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('<sender-gmail>', '<sender-gmail-password>')
    server.sendmail('<sender-gmail>', to, content)
    server.close()


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        ''' Till now we get the query and now we will work on performing tasks '''
        if 'wikipedia' in query:
            speak("Searching for result on wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences = 2)
            print(results)
            speak("According to wikipedia")
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("Youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")
        
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        
        elif 'play music' in query:
            music_dir = 'C:\\Device Data\\Python\\Jarvis\\favourite'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
            break

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak("Hey user, The time is")
            speak(strTime)

        elif 'open code' in query:
            codePath = 'C:\\Users\\verma\\AppData\\Local\\Programs\\Microsoft VS Code\\code.exe'
            os.startfile(codePath)

        elif 'what you can do' in query:
            speak("I am happy to inform you that you can ask me to search anything on wikipedia, open youtube, google or stackoverflow, play music or open VS code")
            speak("Working on sending email also but it will take some time & you can say exit to close the program")

        elif 'email for me' in query:
            try:
                speak("What should i say?")
                content = takeCommand()
                to = '<receiver-gmail-id>'
                sendEmail(to, content)
                speak("Email has been sent!!")

            except Exception as e:
                print(e)
                speak("Sorry looks like we are facing some issue. We will work on this to fix it as soon as possibl")

        elif query == 'exit':
            speak("Thanks for your time. Have a good day. Bye")
            break

        else:
            speak("Sorry the query does not match with any of my operations. You can try again")


