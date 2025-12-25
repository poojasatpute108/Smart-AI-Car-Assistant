import speech_recognition as sr
import pyttsx3

# ------------------------------
# Initialize Text-to-Speech Engine
engine = pyttsx3.init()

def speak(text):
    """Convert text to speech"""
    engine.say(text)
    engine.runAndWait()

# ------------------------------
# Initialize Speech Recognizer
recognizer = sr.Recognizer()

# ------------------------------
# Assistant Welcome
print("🤖 Assistant: Smart Assistant started")
speak("Smart Assistant started")

speak("Hi Pooja, how can I help you?")
print("🤖 Assistant: Hi Pooja, how can I help you?")

# ------------------------------
# Listen to User
try:
    with sr.Microphone() as source:
        print("🎤 Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source, timeout=5)
        
        # Recognize speech using Google Speech Recognition
        command = recognizer.recognize_google(audio)
        print(f"🗣 You said: {command}")
        speak(f"You said: {command}")

except sr.WaitTimeoutError:
    print("🤖 Assistant: No command received.")
    speak("No command received.")

except sr.UnknownValueError:
    print("🤖 Assistant: Sorry, I could not understand.")
    speak("Sorry, I could not understand.")

except sr.RequestError:
    print("🤖 Assistant: Could not request results; check your internet connection.")
    speak("Could not request results; check your internet connection.")

# ------------------------------
# Assistant Shutting Down
print("🤖 Assistant: Assistant shutting down.")
speak("Assistant shutting down.")