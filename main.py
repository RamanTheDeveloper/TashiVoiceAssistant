import pyjokes as pyjokes
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia

listener = sr.Recognizer()
engine = pyttsx3.init()


# Changing voice to female
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print("listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'tashi' in command:
                command = command.replace('tashi', '')
                print(command)
            elif 'time' in command:
                time = datetime.datetime.now().strftime('%I:%M %p')
                talk('current time is' + time)
            elif 'tell me about' in command:
                result = command.replace('tell me about', '')
                info = wikipedia.summary(result, 1)
                talk(info)
            elif 'i love you' in command:
                talk('i love you too Raman')
            elif 'joke' in command:
                talk(pyjokes.get_joke())
            else:
                talk('i beg your pardon')
    except:
        pass

    return command


def run_tashi():
    command = take_command()
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)


run_tashi()