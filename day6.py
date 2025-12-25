import speech_recognition as sr
import pyttsx3
import re

# ---------------- TTS SETUP ----------------
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Zira
engine.setProperty('rate', 150)
engine.setProperty('volume', 1.0)

def speak(text):
    print("🤖 Assistant:", text)
    engine.say(text)
    engine.runAndWait()

# ---------------- SPEECH SETUP ----------------
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
            return ""

# ---------------- START ----------------
speak("Assistant started")
speak("Please tell fuel level and traffic condition")

user_input = listen()

# ---------------- PROCESS INPUT ----------------
fuel = None
traffic = None

# Extract fuel number
numbers = re.findall(r'\d+', user_input)
if numbers:
    fuel = int(numbers[0])

# Detect traffic
if "high" in user_input:
    traffic = "high"
elif "medium" in user_input:
    traffic = "medium"
elif "low" in user_input:
    traffic = "low"

# ---------------- DECISION ----------------
speak("Analyzing situation")

if fuel is None:
    speak("Fuel level not detected")
elif traffic is None:
    speak("Traffic condition not detected")
else:
    if fuel < 5 and traffic == "high":
        speak("Fuel kam hai aur traffic zyada hai. Turant petrol pump dhundhna better hoga.")
    elif fuel < 5:
        speak("Fuel kam hai. Jaldi petrol bharna chahiye.")
    elif traffic == "high":
        speak("Traffic zyada hai. Alternate route le sakte ho.")
    else:
        speak("Sab kuch theek hai. Drive safely.")

speak("Assistant stopped")
