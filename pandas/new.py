import pandas as pd

# Load the uploaded uncleaned dataset
file_path = "/mnt/data/foodmood_with_weather.xlsx"
df_uncleaned = pd.read_excel(file_path)

# Display first few rows and columns for user reference
df_uncleaned.head(), df_uncleaned.columns.tolist()
