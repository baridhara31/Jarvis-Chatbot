import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary

recognize = sr.Recognizer()
engine = pyttsx3.init()

# female_voice_id = 'HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\SPEECH_OneCore\\Voices\\Tokens\\MSTTS_V110_enUS_ZiraM'
# engine.setProperty('voice', female_voice_id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)


if __name__=='__main__':
    speak("Initializing Jarvis...")
    while True:
        #Listen for the wake word "Jarvis"
        #Obtain audio from the microphone
        r=sr.Recognizer()
        print("Recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listining...")
                audio=r.listen(source, timeout=3, phrase_time_limit=3)
            word=r.recognize_google(audio)
            if word.lower()=="jarvis":
                speak("Yes Bari")
                #Listen for command
                with sr.Microphone() as source:
                    print("Jarvis is active.......")
                    audio=r.listen(source)
                    command = r.recognize_google(audio)
                    processCommand(command)
        except Exception as e:
            print("Error; {0}".format(e))



