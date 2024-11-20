import os
import datetime
import pyttsx3
import speech_recognition as sr
import webbrowser
import wikipedia
import smtplib

def say(text):
    pyttsx3.speak(text)

def wishing(name):
    hour= int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        say('Good Morning' + name)
    elif hour>=12 and hour<16:
        say('Good afternoon' + name)
    elif hour>=16 :
        say ('Good Evening' + name)

def knowing():
    pass

def takecommand():
    r =sr.Recognizer()
    with sr.Microphone() as source:
        print('listening...')
        audio =r.listen(source)
        print('')
    try:
        print('Recongnizing...')
        query= r.recognize_google(audio, language= 'en=in')
        print(f'\nuser said: {query}\n')

    except Exception as e:
        print('can you say that again for me')
        say('can you say that again for me')

    return query

# def emailsend():
#     server = smtplib.SMTP('smtp.gmail.com', 587)

if __name__=='__main__':
    print('Initializing Assistent...')
    say('Initializing Assistant...')
    print("May i know your name?")
    say("May i know your name?")
    master =str(takecommand()).lower()
    wishing(master)
    query=str(takecommand()).lower()

    if 'vcs' not in master and 'how are you' in str(query).lower():
        print('Iam fine', master)
        say('Iam fine' + master)
        say('can you call VCS')

    # else :
    #     say('where are you gone..!')

    path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
    if 'open youtube' in query:
        url = 'youtube.com'
        webbrowser.open(url,2)
    elif 'open google' in query:
        url='google.com'
        webbrowser.open(url,2)
        # webbrowser.get(path).open(url,2)

    # elif 'play music' in query:
    #     songspath=r''
    #     songs = os.listdir(songspath)
    #     os.startfile(os.path.join(songspath,songs[0]))
    
    elif 'time' in query:
        time=datetime.datetime.now().strftime('%H:%M')
        say(f'{master} the time is {time}')

    elif 'open vscode' in query:
        codepath=r'C:\Users\chara\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Visual Studio Code'
        os.startfile(codepath)
