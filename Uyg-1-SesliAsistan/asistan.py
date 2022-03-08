# -*- coding: utf-8 -*-
#Öncelikle kurulması gerekenler
#pip install SpeechRecognition
#pip install gTTS
#pip install playsound

import speech_recognition as sr
import webbrowser as webbrowser
import datetime as datetime
import time 
from gtts import gTTS
from playsound import playsound
import random
import os

r= sr.Recognizer()

def record(ask=False):
    with sr.Microphone() as source:
        if ask:
            speak (ask)
            
        audio=r.listen(source)
        voice=''
        
        try:
            voice=r.recognize_google(audio,language="tr-TR")
            
        except sr.UnknownValueError():
            speak("Ne dediğini anlayamadım.")
        
        except sr.RequestError():
            speak("Sana Bozuğum")
        
        return voice

def response(voice):
    if 'nasılsın' in voice:
        speak("İyiyim Sen nasılsın")
    if 'ne haber' in voice:
        speak("iyilik sende ne var ne yok")
    if 'saat kaç' in voice:
        speak(datetime.datetime.now().strftime("%H:%M"))
        
    if 'arama yap' in voice:
        search=record("ne aramak istemiştiniz")
        url="https://google.com/search?q="+search  
        webbrowser.get().open(url)
        speak(search + " ile ilgili bulduklarım")

        exit()



def speak(string):
    tts=gTTS(string,lang="tr")
    rand=random.randint(1, 10000)
    file='audio-'+str(rand)+'.mp3'
    tts.save(file)
    playsound(file)
    os.remove(file)

speak('Nasıl yardımcı olabilirim')

#time.sleep(1)

while 1:
    voice=record()
    print(voice)
    response(voice)














