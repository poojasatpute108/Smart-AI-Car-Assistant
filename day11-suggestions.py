import tkinter as tk
from tkinter import messagebox
import pyttsx3
import speech_recognition as sr

# -----------------------------
# Initialize TTS engine
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Zira female
engine.setProperty('rate', 150)
engine.setProperty('volume', 1.0)

def speak(text):
    engine.say(text)
    engine.runAndWait()

# -----------------------------
# Speech recognizer
recognizer = sr.Recognizer()

def listen_command(prompt):
    speak(prompt)
    print(prompt)
    try:
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source, duration=1)
            print("🎤 Listening...")
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
            command = recognizer.recognize_google(audio)
            print(f"🗣 You said: {command}")
            return command.lower()
    except:
        print("🎤 Could not understand. Please type the value.")
        return None

# -----------------------------
# Analyze function
def analyze():
    # --- Fuel ---
    fuel_val = listen_command("Please say current fuel level in liters")
    if fuel_val is None or not fuel_val.replace('.','',1).isdigit():
        fuel_val = fuel_entry.get()
        if fuel_val == "":
            fuel_val = "6"
    fuel_level = float(fuel_val)

    # --- Traffic ---
    traffic_val = listen_command("Please say traffic condition: low, medium, or high")
    if traffic_val not in ["low", "medium", "high"]:
        traffic_val = traffic_entry.get().lower()
        if traffic_val not in ["low", "medium", "high"]:
            traffic_val = "medium"

    # --- Road ---
    road_val = listen_command("Please say road condition: good, average, or poor")
    if road_val not in ["good", "average", "poor"]:
        road_val = road_entry.get().lower()
        if road_val not in ["good", "average", "poor"]:
            road_val = "average"

    # -----------------------------
    # Fuel Alert & Suggestion
    if fuel_level < 5:
        msg_fuel = f"⚠️ Fuel is low ({fuel_level} liters). Refuel soon!"
        suggestion_fuel = "Nearest petrol pump is recommended."
    else:
        msg_fuel = f"✅ Fuel level is sufficient ({fuel_level} liters)."
        suggestion_fuel = "No fuel action needed."

    # -----------------------------
    # Traffic Alert & Suggestion
    if traffic_val == "high":
        msg_traffic = "⚠️ Traffic is heavy ahead. Consider alternate route."
        suggestion_traffic = "Suggest taking a different route to save time."
    elif traffic_val == "medium":
        msg_traffic = "🚗 Traffic is moderate. Drive normally."
        suggestion_traffic = "No traffic action needed."
    else:
        msg_traffic = "✅ Traffic is smooth."
        suggestion_traffic = "Enjoy smooth driving."

    # -----------------------------
    # Road Alert & Suggestion
    if road_val == "poor":
        msg_road = "⚠️ Road condition ahead is poor. Drive carefully."
        suggestion_road = "Consider safer alternate roads if possible."
    elif road_val == "average":
        msg_road = "🚗 Road condition is average. Moderate caution advised."
        suggestion_road = "Drive carefully."
    else:
        msg_road = "✅ Road condition is good."
        suggestion_road = "No road concerns."

    # -----------------------------
    # Combine messages
    final_msg = f"{msg_fuel}\n{msg_traffic}\n{msg_road}\n\nSuggestions:\n- {suggestion_fuel}\n- {suggestion_traffic}\n- {suggestion_road}"
    print(final_msg)
    
    # Speak all messages
    speak(msg_fuel)
    speak(msg_traffic)
    speak(msg_road)
    
    # Speak final result summary
    speak("Analysis complete. Here is the summary and suggestions.")
    speak(f"Fuel: {msg_fuel}")
    speak(f"Traffic: {msg_traffic}")
    speak(f"Road: {msg_road}")
    speak(f"Suggestions: {suggestion_fuel}. {suggestion_traffic}. {suggestion_road}.")

    # Popup
    messagebox.showinfo("Analysis Result & Suggestions", final_msg)

# -----------------------------
# Tkinter GUI
root = tk.Tk()
root.title("Smart Car Assistant – Hybrid Version")
root.geometry("550x450")

tk.Label(root, text="Smart Car Assistant 🚗", font=("Helvetica", 18, "bold")).pack(pady=10)

# Fuel
tk.Label(root, text="Fuel Level (liters):").pack()
fuel_entry = tk.Entry(root)
fuel_entry.pack(pady=5)

# Traffic
tk.Label(root, text="Traffic (low, medium, high):").pack()
traffic_entry = tk.Entry(root)
traffic_entry.pack(pady=5)

# Road
tk.Label(root, text="Road Condition (good, average, poor):").pack()
road_entry = tk.Entry(root)
road_entry.pack(pady=5)

# Analyze Button
analyze_btn = tk.Button(root, text="Analyze & Suggest", font=("Helvetica", 14), bg="green", fg="white", command=analyze)
analyze_btn.pack(pady=20)

tk.Label(root, text="*You can speak or type values*", font=("Helvetica", 10, "italic")).pack(pady=10)

# Run GUI
root.mainloop()
