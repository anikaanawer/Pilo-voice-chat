import speech_recognition as sr
import pyttsx3
import datetime
import pywhatkit
import wikipedia
import pyjokes

listener = sr.Recognizer()
pilo = pyttsx3.init()
voices = pilo.getProperty('voices')
pilo.setProperty('voice', voices[1].id)

def talk(text):
    pilo.say(text)
    pilo.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'pilo' in command:
                command = command.replace('pilo', '')

    except:
        pass
    return command

def run_pilo():
    command = take_command()

    if 'are you here' in command:
        print('yes,How can i help you')
        talk('yes,How can i help you')

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Current time is ' + time)

    elif 'joke' in command:
        print(pyjokes.get_joke())
        talk(pyjokes.get_joke())

    elif 'tell me about' in command:
        look_for = command.replace('tell me about', '')
        info = wikipedia.summary(look_for, 1)
        print(info)
        talk(info)

    elif 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)

    else:
        talk('I did not get it but I am going to search it for you')
        pywhatkit.search(command)

while True:

        run_pilo()