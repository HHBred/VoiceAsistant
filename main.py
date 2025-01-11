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

def dosya_taramasi_tum_surucu(dizin, aranan_kelime):
    for root, _, files in os.walk(dizin):
        for file in files:
            if aranan_kelime.lower() in file.lower():
                return os.path.join(root, file)  # İlk eşleşmeyi döndür
    return None

def uygulama_calistir():
    """
    "darkorbit" anahtar kelimesiyle tüm `C:` sürücüsünde bir dosya arar ve bulursa çalıştırır.
    """
    dizin_yolu = "C:\\"  # Tarama yapılacak sürücü
    aranan_kelime = "darkorbit.exe"  # Aranacak anahtar kelime
    
    print("Tüm sürücülerde arama yapılıyor, lütfen bekleyin...")
    
    # Dosyayı tara ve bul
    uygulama_yolu = dosya_taramasi_tum_surucu(dizin_yolu, aranan_kelime)

def uygulama_calistir1():
    """
    "MAFYA2" anahtar kelimesiyle tüm `E:` sürücüsünde bir dosya arar ve bulursa çalıştırır.
    """
    dizin_yolu = "C:\\"
    dizin_yolu = "D:\\"
    dizin_yolu = "E:\\"
    dizin_yolu = "F:\\"  # Tarama yapılacak sürücü
    aranan_kelime = "mafia2.exe"  # Aranacak anahtar kelime
    
    print("Tüm sürücülerde arama yapılıyor, lütfen bekleyin...")
    
    # Dosyayı tara ve bul
    uygulama_yolu = dosya_taramasi_tum_surucu(dizin_yolu, aranan_kelime)
    
    if uygulama_yolu:
        print(f"Uygulama bulundu: {uygulama_yolu}")
        os.startfile(uygulama_yolu)  # Uygulamayı çalıştır
        speak("İstediğin uygulamayı çalıştırıyorum.")
    else:
        speak(f"{aranan_kelime} adlı dosya bulunamadı") 

def uygulama_calistir2():
    """
    "gta sa" anahtar kelimesiyle tüm `E:` sürücüsünde bir dosya arar ve bulursa çalıştırır.
    """
    dizin_yolu = "C:\\"
    dizin_yolu = "D:\\"
    dizin_yolu = "E:\\"
    dizin_yolu = "F:\\"  # Tarama yapılacak sürücü
    aranan_kelime = "gta-sa.exe"  # Aranacak anahtar kelime
    
    print("Tüm sürücülerde arama yapılıyor, lütfen bekleyin...")
    
    # Dosyayı tara ve bul
    uygulama_yolu = dosya_taramasi_tum_surucu(dizin_yolu, aranan_kelime)
    
    if uygulama_yolu:
        print(f"Uygulama bulundu: {uygulama_yolu}")
        os.startfile(uygulama_yolu)  # Uygulamayı çalıştır
        speak("İstediğin uygulamayı çalıştırıyorum.")
    else:
        speak(f"{aranan_kelime} adlı dosya bulunamadı") 
 
def uygulama_calistir3():
    """
    "speed.exe" anahtar kelimesiyle tüm `E:` sürücüsünde bir dosya arar ve bulursa çalıştırır.
    """
    dizin_yolu = "C:\\"
    dizin_yolu = "D:\\"
    dizin_yolu = "E:\\"
    dizin_yolu = "F:\\" # Tarama yapılacak sürücü
    aranan_kelime = "speed.exe"  # Aranacak anahtar kelime
    
    print("Tüm sürücülerde arama yapılıyor, lütfen bekleyin...")
    
    # Dosyayı tara ve bul
    uygulama_yolu = dosya_taramasi_tum_surucu(dizin_yolu, aranan_kelime)
    
    if uygulama_yolu:
        print(f"Uygulama bulundu: {uygulama_yolu}")
        os.startfile(uygulama_yolu)  # Uygulamayı çalıştır
        speak("İstediğin uygulamayı çalıştırıyorum.")
    else:
        speak(f"{aranan_kelime} adlı dosya bulunamadı")

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
        elif "tek kol" in runApp:
           os.startfile("steam://rungameid/2551020")
           speak("İstediğin uygulamayı çalıştırıyorum.")
        elif "GTA V" in runApp:
           os.startfile("com.epicgames.launcher://apps/0584d2013f0149a791e7b9bad0eec102%3A6e563a2c0f5f46e3b4e88b5f4ed50cca%3A9d2d0eb64d5c44529cece33fe2a46482?action=launch&silent=true")
           speak("İstediğin uygulamayı çalıştırıyorum.")
        elif "spotify" in runApp:
           webbrowser.get().open(url2)
           url2 = "https://open.spotify.com/"
           speak("İstediğin uygulamayı çalıştırıyorum.")
        elif "mafya2" in runApp:
           uygulama_calistir1()
           speak("İstediğin uygulamayı çalıştırıyorum.")
        elif "darkorbit" in runApp:
           uygulama_calistir()
        elif "need" in runApp:
           uygulama_calistir3()
           speak("İstediğin uygulamayı çalıştırıyorum.")
        elif "asetto" in runApp:
           os.startfile("steam://rungameid/244210")
           speak("İstediğin uygulamayı çalıştırıyorum.")
        elif "gta san andreas" in runApp:
              uygulama_calistir2()
              speak("İstediğin uygulamayı çalıştırıyorum.")
        else:
            speak("İstediğin uygulama çalıştırma listemde yok.")
        
    if "not et" in voice:
        speak("Dosya ismi ne olsun?")
        txtFile = record() + "a.txt"
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
        voice = voice.lower()
        print(voice.capitalize())
        response(voice)
