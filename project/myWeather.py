import pandas as pd
import datetime
import requests

Api_key = '6e6f9659fef62e5c5d1103979100d281'
base_url = 'http://api.openweathermap.org/data/2.5/weather'

# Same code as above
city = "Delhi"
request_url = f"{base_url}?appid={Api_key}&q={city}"
response = requests.get(request_url)

if response.status_code==200:
    data = response.json()
    weather = data['weather'][0]['description']
    temperature = round(data['main']['temp'] - 273.15, 2)

    # Save to DataFrame
    df = pd.DataFrame({
        'City': [city],
        'Weather': [weather],
        'Temperature': [temperature],
        'Timestamp': [datetime.datetime.now()]
    })

    # Save as CSV
    df.to_csv('weather_data.csv', index=False)
    print("Saved weather data to CSV.")
else:
    print("An error occurred...")



# Read Zomato data with correct encoding
zomato_df = pd.read_csv(r'D:\python\ZOMATO_DATA_ANALYSIS.csv', encoding='ISO-8859-1')

# Read weather data
weather_df = pd.read_csv('weather_data.csv')

# Clean both City columns: strip whitespace and convert to lowercase
zomato_df['City'] = zomato_df['City'].str.strip().str.lower()
weather_df['City'] = weather_df['City'].str.strip().str.lower()

# Merge on 'City'
merged_df = pd.merge(zomato_df, weather_df, on='City', how='left')

# Save merged dataset
merged_df.to_csv('zomato_with_weather.csv', index=False)
print("✅ Merged file saved as 'zomato_with_weather.csv'")

    