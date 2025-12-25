while True:
    try:
        fuel_level = float(input("Enter current fuel level (in liters): "))
        if fuel_level < 0:
            print("⚠️ Fuel cannot be negative. Enter again.")
        else:
            break
    except ValueError:
        print("⚠️ Invalid input! Please enter a number (example: 5 or 3.5).")
        if fuel_level < 5:
            print("⚠️ Warning: Fuel is low. Please refuel soon!")
        else:
            print("✅ Fuel level is sufficient.")

while True:
    traffic_level = input("Enter traffic condition (low/medium/high): ").lower()
    if traffic_level in ["low", "medium", "high"]:
        break
    else:
        print("⚠️ Invalid input! Please enter low, medium, or high.")
while True:
    road_condition = input("Enter road condition (good/average/poor): ").lower()
    if road_condition in ["good", "average", "poor"]:
        break
    else:
        print("⚠️ Invalid input! Please enter good, average, or poor.") 
    if fuel_level < 5:
       print("⚠️ Fuel is low. Please refuel soon.")
    else:
        print("✅ Fuel level is sufficient.")
    if traffic_level == "high":
       print("⚠️ Heavy traffic ahead. Suggest alternate route.")
    elif traffic_level == "medium":
        print("🚗 Traffic is moderate.")
    else:
         print("✅ Traffic is smooth.")
    if road_condition == "poor":
       print("⚠️ Road condition is poor. Drive carefully or change route.")
    elif road_condition == "average":
        print("🚗 Road condition is average. Be cautious.")
    else:
         print("✅ Road condition is good.")