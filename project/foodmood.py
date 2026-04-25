import pandas as pd
import random

# Step 1: Load your Excel file
df = pd.read_excel(r"C:\Users\shubh\Downloads\Kaggledatasets\foodmood.xlsx")

# Step 2: Simulate random weather for each row
def simulate_weather():
    conditions = [
        {"weather": "Sunny", "temp_range": (30, 40), "humidity_range": (20, 40)},
        {"weather": "Rainy", "temp_range": (22, 30), "humidity_range": (70, 100)},
        {"weather": "Cloudy", "temp_range": (25, 33), "humidity_range": (50, 70)},
        {"weather": "Foggy", "temp_range": (18, 25), "humidity_range": (80, 95)},
        {"weather": "Thunderstorm", "temp_range": (23, 31), "humidity_range": (75, 100)},
    ]
    choice = random.choice(conditions)
    return {
        "Weather": choice["weather"],
        "Temperature (°C)": round(random.uniform(*choice["temp_range"]), 1),
        "Humidity (%)": round(random.uniform(*choice["humidity_range"]), 1)
    }

# Step 3: Apply weather simulation
weather_data = df.apply(lambda row: pd.Series(simulate_weather()), axis=1)

# Step 4: Merge with original DataFrame
df = pd.concat([df, weather_data], axis=1)

# Step 5: Save final DataFrame as a new Excel or CSV file
output_path_excel = r"C:\Users\shubh\Downloads\Kaggledatasets\foodmood_with_weather.xlsx"

df.to_excel(output_path_excel, index=False)
print("✅ Weather data added and saved to Excel and CSV successfully.")
