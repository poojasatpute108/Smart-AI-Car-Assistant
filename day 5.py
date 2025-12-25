import speech_recognition as sr
import pyttsx3

# ---------- TTS ----------
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 150)

def speak(text):
    print("🤖 Assistant:", text)
    engine.say(text)
    engine.runAndWait()

# ---------- Speech ----------
recognizer = sr.Recognizer()

def listen():
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=1)
        try:
            audio = recognizer.listen(source, timeout=8, phrase_time_limit=4)
            text = recognizer.recognize_google(audio)
            print("🗣 You said:", text)
            return text.lower()
        except:
            return None

# ---------- START ----------
speak("Assistant started")

# ---------- FUEL ----------
speak("Please say fuel level in liters")
fuel_text = listen()

try:
    fuel = float(fuel_text)
except:
    speak("Fuel not clear. Please type fuel level.")
    fuel = float(input("Enter fuel level: "))

# ---------- TRAFFIC ----------
speak("Please say traffic condition. Low medium or high")
traffic = listen()

if traffic not in ["low", "medium", "high"]:
    speak("Traffic not clear. Please type traffic condition.")
    traffic = input("Enter traffic (low/medium/high): ").lower()

# ---------- DECISION ----------
speak("Analyzing situation")

if fuel < 5 and traffic == "high":
    speak("Fuel is low and traffic is heavy. Finding petrol pump is recommended.")
elif fuel < 5:
    speak("Fuel is low. Please refuel soon.")
elif traffic == "high":
    speak("Traffic is heavy. Consider alternate route.")
else:
    speak("Everything looks good. Drive safely.")

speak("Assistant stopped")
