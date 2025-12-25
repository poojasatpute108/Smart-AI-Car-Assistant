import speech_recognition as sr
import pyttsx3
import time

# ------------------ TTS SETUP ------------------
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Zira (female)
engine.setProperty('rate', 150)
engine.setProperty('volume', 1.0)

def speak(text):
    print("🤖 Assistant:", text)
    engine.say(text)
    engine.runAndWait()
    time.sleep(1)   # VERY IMPORTANT pause

# ------------------ MIC SETUP ------------------
recognizer = sr.Recognizer()

def listen():
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=1)
        print("🎤 Listening...")
        audio = recognizer.listen(source)
    try:
        text = recognizer.recognize_google(audio)
        print("🗣 You said:", text)
        return text.lower()
    except:
        return None

# ------------------ START ------------------
speak("Assistant started")

# ---------- FUEL ----------
speak("Please say fuel level in liters")
fuel_text = listen()

if fuel_text is None:
    fuel = 6
else:
    try:
        fuel = float(fuel_text)
    except:
        fuel = 6

# ---------- TRAFFIC ----------
speak("Please say traffic condition. Low, medium or high")
traffic = listen()
if traffic not in ["low", "medium", "high"]:
    traffic = "medium"

# ---------- ROAD ----------
speak("Please say road condition. Good, average or poor")
road = listen()
if road not in ["good", "average", "poor"]:
    road = "average"

# ---------- OUTPUT ----------
if fuel < 5:
    speak(f"Fuel is low. Only {fuel} liters remaining.")
else:
    speak(f"Fuel level is sufficient. {fuel} liters available.")

if traffic == "high":
    speak("Heavy traffic ahead. Please take alternate route.")
elif traffic == "medium":
    speak("Traffic is moderate. Drive carefully.")
else:
    speak("Traffic is clear.")

if road == "poor":
    speak("Road condition is poor. Drive slowly.")
elif road == "average":
    speak("Road condition is average.")
else:
    speak("Road condition is good.")

speak("Assistant stopped")
