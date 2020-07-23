import time
import pyaudio
import speech_recognition as sr
from playsound import playsound
from pynput.keyboard import Key, Controller
import pynput
import os
import configparser
import unidecode
import webbrowser

config = configparser.ConfigParser()
config.read('settings.ini')
dingOn = 'F:/Projekty/Python/3.6.SI/dingOn.mp3'

r = sr.Recognizer()
m = sr.Microphone()
with m as source:
    r.adjust_for_ambient_noise(source)
print("Zaczynamy zabawe!")


def check(text):
    text = text.lower()
    text = unidecode.unidecode(text)
    print(text)
    split = text.split(' ')

    if split[0] == 'odpal':
        text = text.replace('odpal ', '')
        if text in config['odpal']:
            os.startfile(config['odpal'][text], 'open')
    elif split[0] == 'otworz':
        text = text.replace('otworz ', '')
        if text in config['otworz']:
            os.startfile(config['otworz'][text], 'open')
    elif split[0] == 'wejdz':
        text = text.replace('wejdz na ', '')
        if text in config['wejdz']:
            webbrowser.open(config['wejdz'][text])


def callback(recognizer, audio):
    try:
        text = recognizer.recognize_google(audio, language='pl-PL')
        check(text)
    except sr.UnknownValueError:
        print("Nie rozumiem co mowisz!")
    except sr.RequestError as e:
        print("Blad z requestem; {0}".format(e))


def listen():
    playsound(dingOn)
    stop_listening = r.listen_in_background(m, callback)
    for _ in range(30): time.sleep(0.1)
    stop_listening(wait_for_stop=False)


def on_release(key):
    if key == Key.f8:
        listen()
    if key == Key.esc:
        return False


with pynput.keyboard.Listener(
        on_release=on_release) as listener:
    listener.join()
