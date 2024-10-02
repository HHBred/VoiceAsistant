from playsound import playsound
from gtts import gTTS
import speech_recognition as sr
import os
import time
from datetime import datetime
import webbrowser
import pyautogui

r = sr.Recognizer()

def record(ask=False):
    with sr.Microphone() as source:
        if ask:
            print(ask)
        audio = r.listen(source)
        voice = ""
        try:
            voice = r.recognize_google(audio, language="tr-TR")
        except sr.UnknownValueError:
            print("Asistan: Anlayamadım")
            speak("bekliyorum")
        except sr.RequestError:
            print("Asistan: Sistem çalışmıyor")
        return voice  # return the recognized voice

def take_screenshot():
    screenshot = pyautogui.screenshot()
    screenshot.save("ekran_goruntusu.png")
    speak("Ekran görüntüsü alındı ve kaydedildi.")

def response(voice):
    if "merhaba" in voice:
        speak("sanada merhaba")
    if "selam" in voice:
        speak("sanada selam")
    if "teşekkür ederim" in voice or "teşekkürler" in voice:
        speak("rica ederim")
    if "görüşürüz" in voice:
        speak("bay bay")
        exit()
    if "kapat" in voice:
        speak("kapanıyorum")
        exit()

    if "saat kaç" in voice:
        speak("Saat şu an :")
        speak(datetime.now().strftime("%H:%M"))

    if "bilgisayarı kapat" in voice:
       os.system("shutdown /s /t 1")

    if "ekran görüntüsü al" in voice:
        take_screenshot()  
       

    if "günlerden ne" in voice or "bugün günlerden ne" in voice:
       today = time.strftime("%A")
       today = today.capitalize()  
       if today == "Monday":
        today = "Pazartesi"
       elif today == "Tuesday":
        today = "Salı"
       elif today == "Wednesday":
        today = "Çarşamba"
       elif today == "Thursday":
        today = "Perşembe"
       elif today == "Friday":
        today = "Cuma"
       elif today == "Saturday":
        today = "Cumartesi"
       elif today == "Sunday":
        today = "Pazar"

       speak(today)

    if "youtube aç" in voice:
     webbrowser.open("https://www.youtube.com")
     speak("YouTube açıldı.")



    if "google'da ara" in voice or "internet'te ara"in voice:
       speak("ne aramamı istersin?")
       search = record()
       url = "https://www.google.com/search?q={}".format(search)
       webbrowser.get().open(url)
       speak("internet'te bulabildik'lerim")
    if "aşağı kaydır"in voice:
          pyautogui.scroll(-500)
          speak("tamam")
    if "yukarı kaydır"in voice:
          pyautogui.scroll(500)
          speak("tamam")
    if  "ileri git" in voice:
       speak("ileri gidiliyor")
       for _ in range(10):
         pyautogui.press('w')
    if  "geri git" in voice:
       speak("geri gidiliyor")
       for _ in range(10):
         pyautogui.press('s')
    if  "sağa git" in voice:
       speak("sağa gidiliyor")
       for _ in range(10):
         pyautogui.press('d')
    if  "sola git" in voice:
       speak("sola gidiliyor")
       for _ in range(10):
         pyautogui.press('a')

    if "uygulama aç" in voice:
        speak("Hangi uygulamayı açmamı istiyorsun?")
        runApp = record()
        runApp = runApp.lower()
        if "valorant" in runApp:
            os.startfile("D:\\Riot Games\\Riot Client\\RiotClientServices.exe")
            speak("İstediğin uygulamayı çalıştırıyorum.")
        elif "life is strange" in runApp:
            os.startfile("steam://rungameid/319630")
            speak("İstediğin uygulamayı çalıştırıyorum.")
        elif "mafya" in runApp:
           os.startfile("steam://rungameid/40990")
           speak("İstediğin uygulamayı çalıştırıyorum.")
        elif "tek kol" in runApp:
           os.startfile("steam://rungameid/2551020")
           speak("İstediğin uygulamayı çalıştırıyorum.")
        elif "GTA V" in runApp:
           os.startfile("com.epicgames.launcher://apps/0584d2013f0149a791e7b9bad0eec102%3A6e563a2c0f5f46e3b4e88b5f4ed50cca%3A9d2d0eb64d5c44529cece33fe2a46482?action=launch&silent=true")
           speak("İstediğin uygulamayı çalıştırıyorum.")
        elif "spotify" in runApp:
           os.startfile("steam://rungameid/2551020")
           speak("İstediğin uygulamayı çalıştırıyorum.")
        elif "mafya 2" in runApp:
           os.startfile("D:\\Games\\Mafia 2\\launcher.exe")
           speak("İstediğin uygulamayı çalıştırıyorum.")
        elif "darkorbit" in runApp:
           os.startfile("C:\\Users\\ali osman\\Dark Orbit\\DarkOrbit.exe")
           speak("İstediğin uygulamayı çalıştırıyorum.")
        elif "asetto" in runApp:
           os.startfile("steam://rungameid/244210")
           speak("İstediğin uygulamayı çalıştırıyorum.")
        elif "gta san andreas" in runApp:
           os.startfile("C:\Program Files (x86)\MTA San Andreas 1.6")
           speak("İstediğin uygulamayı çalıştırıyorum.")

        else:
            speak("İstediğin uygulama çalıştırma listemde yok.")
        
    if "not et" in voice:
        speak("Dosya ismi ne olsun?")
        txtFile = record() + ".txt"
        speak("Başla")
        theText = record()
        
        # Correct file handling
        with open(txtFile, "w", encoding="utf-8") as f:
            f.write(theText)




def speak(string):
    tts = gTTS(text=string, lang="tr", slow=False)
    file = "answer.mp3"
    tts.save(file)
    playsound(file)
    os.remove(file)

playsound("DING.mp3")
speak("Sizi dinliyorum")



while True:
    voice = record()
    if voice:
        voice =voice.lower()
        print(voice.capitalize())
        response(voice)

