import speech_recognition as sr

print("🤖 Assistant: Smart Assistant started")

r = sr.Recognizer()

try:
    with sr.Microphone() as source:
        print("🤖 Assistant: I am listening. Please speak now.")
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source, timeout=5)

        print("🤖 Assistant: Recognizing...")
        text = r.recognize_google(audio)

        print("👤 You said:", text)

except sr.WaitTimeoutError:
    print("⏱ No speech detected")

except sr.UnknownValueError:
    print("❌ Sorry, I could not understand")

except sr.RequestError as e:
    print("⚠ Google API error:", e)

except Exception as e:
    print("⚠ Error:", e)

print("🤖 Assistant: Assistant shutting down.")

