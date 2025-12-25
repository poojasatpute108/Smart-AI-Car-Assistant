import tkinter as tk
from tkinter import messagebox
import pyttsx3
from datetime import datetime

# ---------- Voice Engine ----------
engine = pyttsx3.init()
engine.setProperty("rate", 165)

def speak(text):
    engine.say(text)
    engine.runAndWait()

# ---------- Special Days Dictionary ----------
SPECIAL_DAYS = {
    "26-01": "Today is Republic Day of India",
    "08-03": "Today is International Women's Day",
    "15-08": "Today is Independence Day of India",
    "05-09": "Today is Teachers Day",
    "02-10": "Today is Gandhi Jayanti",
    "14-11": "Today is Children's Day",
    "25-12": "Today is Christmas"
}

# ---------- Check Special Day ----------
def check_special_day():
    today = datetime.now().strftime("%d-%m")
    if today in SPECIAL_DAYS:
        msg = SPECIAL_DAYS[today]
        status_label.config(text=msg)
        speak(msg)
    else:
        msg = "No special event today. Have a safe and productive day."
        status_label.config(text=msg)
        speak(msg)

# ---------- Reminder ----------
def set_reminder():
    date = date_entry.get()
    note = note_entry.get()

    if date == "" or note == "":
        speak("Please provide date and reminder message")
        messagebox.showwarning("Missing", "Please fill all fields")
        return

    msg = f"Reminder saved for {date}. Message is {note}"
    speak(msg)
    messagebox.showinfo("Reminder Saved", msg)

# ---------- GUI ----------
root = tk.Tk()
root.title("Pooja AI Assistant – Welcome")
root.geometry("900x500")
root.resizable(False, False)

# Background color (blur style simulation)
root.configure(bg="#1e1e2f")

# ---------- Title ----------
title = tk.Label(
    root,
    text="Welcome Pooja 💙\nAI Assistant Started",
    font=("Segoe UI", 22, "bold"),
    fg="white",
    bg="#1e1e2f"
)
title.pack(pady=20)

# ---------- Status ----------
status_label = tk.Label(
    root,
    text="Detecting today's information...",
    font=("Segoe UI", 14),
    fg="lightblue",
    bg="#1e1e2f"
)
status_label.pack(pady=10)

# ---------- Reminder Frame ----------
frame = tk.Frame(root, bg="#2a2a40")
frame.pack(pady=20)

tk.Label(frame, text="Reminder Date (DD-MM):",
         font=("Segoe UI", 12),
         fg="white", bg="#2a2a40").grid(row=0, column=0, padx=10, pady=10)

date_entry = tk.Entry(frame, font=("Segoe UI", 12), width=20)
date_entry.grid(row=0, column=1, pady=10)

tk.Label(frame, text="Reminder Note:",
         font=("Segoe UI", 12),
         fg="white", bg="#2a2a40").grid(row=1, column=0, padx=10, pady=10)

note_entry = tk.Entry(frame, font=("Segoe UI", 12), width=20)
note_entry.grid(row=1, column=1, pady=10)

tk.Button(
    root,
    text="Save Reminder",
    font=("Segoe UI", 13, "bold"),
    bg="#4CAF50",
    fg="white",
    command=set_reminder
).pack(pady=15)

# ---------- Start Voice ----------
root.after(1000, lambda: speak("Welcome Pooja. AI assistant started"))
root.after(2000, check_special_day)

root.mainloop()
