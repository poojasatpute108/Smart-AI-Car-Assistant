import tkinter as tk
from tkinter import messagebox

# -----------------------------
# Main Window
# -----------------------------
app = tk.Tk()
app.title("Smart Vehicle Assistant")
app.geometry("450x400")
app.resizable(False, False)

# -----------------------------
# Title
# -----------------------------
title_label = tk.Label(
    app,
    text="🚗 Smart Vehicle Assistant",
    font=("Arial", 16, "bold")
)
title_label.pack(pady=10)

# -----------------------------
# Fuel Input
# -----------------------------
fuel_label = tk.Label(app, text="Enter Fuel Level (liters):")
fuel_label.pack()
fuel_entry = tk.Entry(app)
fuel_entry.pack(pady=5)

# -----------------------------
# Traffic Input
# -----------------------------
traffic_label = tk.Label(app, text="Enter Traffic (low / medium / high):")
traffic_label.pack()
traffic_entry = tk.Entry(app)
traffic_entry.pack(pady=5)

# -----------------------------
# Road Input
# -----------------------------
road_label = tk.Label(app, text="Enter Road Condition (good / average / poor):")
road_label.pack()
road_entry = tk.Entry(app)
road_entry.pack(pady=5)

# -----------------------------
# Output Box
# -----------------------------
output_box = tk.Text(app, height=8, width=50)
output_box.pack(pady=10)

# -----------------------------
# Logic Function
# -----------------------------
def start_assistant():
    output_box.delete("1.0", tk.END)

    fuel = fuel_entry.get()
    traffic = traffic_entry.get().lower()
    road = road_entry.get().lower()

    try:
        fuel = float(fuel)
    except:
        messagebox.showerror("Error", "Fuel must be a number")
        return

    output_box.insert(tk.END, "🤖 Assistant Analysis:\n\n")

    # Fuel logic
    if fuel < 5:
        output_box.insert(tk.END, f"⚠️ Fuel low ({fuel} L). Refuel soon.\n")
    else:
        output_box.insert(tk.END, f"✅ Fuel OK ({fuel} L).\n")

    # Traffic logic
    if traffic == "high":
        output_box.insert(tk.END, "⚠️ Traffic is high. Take alternate route.\n")
    elif traffic == "medium":
        output_box.insert(tk.END, "🚗 Traffic is moderate.\n")
    else:
        output_box.insert(tk.END, "✅ Traffic is smooth.\n")

    # Road logic
    if road == "poor":
        output_box.insert(tk.END, "⚠️ Road condition poor. Drive carefully.\n")
    elif road == "average":
        output_box.insert(tk.END, "🚗 Road condition average.\n")
    else:
        output_box.insert(tk.END, "✅ Road condition good.\n")

    output_box.insert(tk.END, "\n🤖 Assistant finished analysis.")

# -----------------------------
# Button
# -----------------------------
start_button = tk.Button(
    app,
    text="Start Assistant",
    font=("Arial", 12, "bold"),
    bg="green",
    fg="white",
    command=start_assistant
)
start_button.pack(pady=10)

# -----------------------------
# Run App
# -----------------------------
app.mainloop()
