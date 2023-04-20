import pyttsx3
import webbrowser 
import datetime 
import os
import speech_recognistion
import smtplib

engine= pyttsx3.init ('sapi5')
voices=engine.getproperty('voices')
print(voices[1].id)
engine.setproprty('voices',voices[1].id)


def speak(audio):
engine.say(audio)
engine.runAndawait()

def wish():
    hour=int(datetime.datetime.now().hour)

    if hour>0 and hour<=12:
        speak("good morning sir")

    elif hour>12 and hour<=6:
        speak("good afternoon")
    
    else:
        speak("good evening")




def take():

    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("i am recognizing")
        r.pause_threshould=1
        audio=r.listen(source)

        try:
            print('listening')
            query=r.recognize_google(audio,language='en-ln')

            print(f"you said{query}")

        except Exception as a:
            print(a)

            print("i cannot recognize please will you say that again")
            return "none"
            return query

        def sendEmail():
            server=smtplib.SMTP(smptp.gamil.com,587)
            server.login("youremail2gmail.com","yourpassword")
            server.sendEmail("youremail@gmail.com",to,content)
            server.close()

sendEmail()
if __name__=="__main__"
wish()
while True :
    query =take.lower()
    if "wikipedia" in query:
        speak("searching results")
        query=query.replace("wikipedia" "")
        result=wikipedia.summary (query,sentances=20)
        speak("according to wikipedia")
        speak(result)

    elif 'open youtube ' in query:
        webbrowser.open ("youtube.com")

    elif 'open google ' in query:
        webbrowser.open ("google.com")

    elif 'open spotify ' in query:
        webbrowser.open ("spotify.com")

    elif 'play music ' in query:
        music_dir="D\\Non ciritical\\songs\Favourite songs2"
        songs=os.listdir(music_dir)
        print(songs)
        os.starttimeos.path.join(music_dir,songs[1])

    elif 'what is the time' in query:
        strTime=datetime.datetime.now().strtime("%H",:"%M":"%S")
        speak(f"{strTime} is hte cuurent time")
        
    elif 'open vscode' in query:
        codepath="C:\\User\\Maris\\Appdata\\Local\\Microsoft vs code\\Code.exe"
        os.startfile(codepath)

    elif 'email to admin' in query:
        try:
            speak("what can i do sir?")
            content=take()
            to="vankar262@gmail.com"

            sendEmail(to,content)
            speak("email has been sent")

        except Exception as e:
            print(e)
            speak("I am not able to send email")

