import tkinter as tk
from tkinter import ttk
import pyttsx3
import webbrowser
import geocoder
import matplotlib.pyplot as plt

# ---------------- VOICE ENGINE ----------------
engine = pyttsx3.init()
engine.setProperty('rate', 165)

def speak(text):
    engine.say(text)
    engine.runAndWait()

# ---------------- MAP FUNCTION ----------------
def open_live_map():
    g = geocoder.ip('me')
    if g.latlng:
        lat, lng = g.latlng
        url = f"https://www.google.com/maps/@{lat},{lng},15z?entry=ttu"
        webbrowser.open(url)
        speak("Showing your live location on map")
    else:
        speak("Unable to fetch live location")

# ---------------- AI ANALYSIS ----------------
def analyze():
    fuel = fuel_var.get()
    traffic = traffic_var.get()
    road = road_var.get()

    result = ""
    reason = ""

    if fuel < 5 and traffic == "High":
        result = "Fuel is low and traffic is high."
        reason = "High traffic increases fuel consumption."
    elif road == "Poor":
        result = "Road condition is poor."
        reason = "Bad roads increase accident risk."
    else:
        result = "Everything looks safe."
        reason = "Fuel, traffic and road conditions are normal."

    output_label.config(text=f"Decision:\n{result}\n\nReason:\n{reason}")
    speak(result + " " + reason)

    show_graph(fuel, traffic, road)

# ---------------- GRAPH (UNIQUE FEATURE) ----------------
def show_graph(fuel, traffic, road):
    traffic_score = {"Low": 2, "Medium": 5, "High": 8}
    road_score = {"Good": 8, "Average": 5, "Poor": 2}

    labels = ["Fuel Level", "Traffic Risk", "Road Safety"]
    values = [fuel, traffic_score[traffic], road_score[road]]

    plt.figure(figsize=(6,4))
    plt.bar(labels, values)
    plt.title("AI Driving Condition Analysis")
    plt.ylabel("Risk / Safety Score")
    plt.show()

# ---------------- UI WINDOW ----------------
root = tk.Tk()
root.title("Smart Car AI Assistant – Page 3")
root.geometry("900x600")

# ---------------- MAIN FRAME ----------------
frame = tk.Frame(root, bg="#1e1e2f")
frame.pack(fill="both", expand=True)

title = tk.Label(
    frame,
    text="SMART CAR AI – ADVANCED ANALYSIS",
    font=("Segoe UI", 20, "bold"),
    bg="#1e1e2f",
    fg="white"
)
title.pack(pady=20)

# ---------------- INPUTS ----------------
input_frame = tk.Frame(frame, bg="#1e1e2f")
input_frame.pack(pady=20)

fuel_var = tk.IntVar(value=6)
traffic_var = tk.StringVar(value="Medium")
road_var = tk.StringVar(value="Average")

tk.Label(input_frame, text="Fuel Level (Liters)", font=("Segoe UI", 14),
         bg="#1e1e2f", fg="white").grid(row=0, column=0, padx=20, pady=10)
tk.Entry(input_frame, textvariable=fuel_var, font=("Segoe UI", 14),
         width=10).grid(row=0, column=1)

tk.Label(input_frame, text="Traffic", font=("Segoe UI", 14),
         bg="#1e1e2f", fg="white").grid(row=1, column=0, pady=10)
ttk.Combobox(input_frame, values=["Low","Medium","High"],
             textvariable=traffic_var, width=12).grid(row=1, column=1)

tk.Label(input_frame, text="Road Condition", font=("Segoe UI", 14),
         bg="#1e1e2f", fg="white").grid(row=2, column=0, pady=10)
ttk.Combobox(input_frame, values=["Good","Average","Poor"],
             textvariable=road_var, width=12).grid(row=2, column=1)

# ---------------- BUTTONS ----------------
btn_frame = tk.Frame(frame, bg="#1e1e2f")
btn_frame.pack(pady=20)

tk.Button(btn_frame, text="Analyze AI Decision",
          font=("Segoe UI", 14, "bold"),
          bg="#00adb5", fg="white",
          command=analyze).grid(row=0, column=0, padx=20)

tk.Button(btn_frame, text="Open Live Map",
          font=("Segoe UI", 14, "bold"),
          bg="#393e46", fg="white",
          command=open_live_map).grid(row=0, column=1, padx=20)

# ---------------- OUTPUT ----------------
output_label = tk.Label(
    frame,
    text="AI Decision will appear here",
    font=("Segoe UI", 14),
    bg="#1e1e2f",
    fg="#eeeeee",
    justify="center"
)
output_label.pack(pady=30)

# ---------------- START ----------------
speak("Smart Car AI Page three loaded. Ready for advanced analysis.")
root.mainloop()
# ---------------- ACCIDENT PRONE DATA ----------------
accident_prone_areas = ["highway", "bridge", "ghat", "sharp turn"]
def accident_warning(route_condition):
    route_condition = route_condition.lower()

    for area in accident_prone_areas:
        if area in route_condition:
            warning_text = "Warning! You are entering an accident prone area. Drive carefully."
            print("🚨", warning_text)
            speak(warning_text)
            return

    safe_text = "Route seems safe. Continue driving normally."
    print("✅", safe_text)
    speak(safe_text)
accident_warning("highway")
