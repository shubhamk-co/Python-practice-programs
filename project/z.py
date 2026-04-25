import pandas as pd
import random

# --- Load your Excel file ---
file_path = "Food_Mood.xlsx"
df = pd.read_excel(file_path)

# --- Step 1: Define 2022 festival dates with names ---
festival_dates = {
    "Republic Day": "2022-01-26",
    "Holi": "2022-03-18",
    "Eid": "2022-05-03",
    "Independence Day": "2022-08-15",
    "Raksha Bandhan": "2022-08-11",
    "Dussehra": "2022-10-05",
    "Diwali": "2022-10-24",
    "Christmas": "2022-12-25"
}
# Convert to datetime
festival_dates = {name: pd.to_datetime(date) for name, date in festival_dates.items()}

# --- Step 2: Calculate how many rows to assign festival dates ---
total_rows = len(df)
festival_count = int(total_rows * 0.10)
non_festival_count = total_rows - festival_count

# --- Step 3: Create festival assignments ---
festival_name_date_pairs = list(festival_dates.items())
festival_assignments = [random.choice(festival_name_date_pairs) for _ in range(festival_count)]
festival_dates_only = [fd[1] for fd in festival_assignments]
festival_names_only = [fd[0] for fd in festival_assignments]

# --- Step 4: Non-festival dates ---
all_possible_dates = pd.date_range(start="2022-01-01", end="2022-12-31")
non_festival_dates = [d for d in all_possible_dates if d not in festival_dates.values()]
non_festival_assignments = random.choices(non_festival_dates, k=non_festival_count)
non_festival_names = ["No"] * non_festival_count

# --- Step 5: Combine and shuffle both ---
all_dates = festival_dates_only + non_festival_assignments
all_labels = festival_names_only + non_festival_names

combined = list(zip(all_dates, all_labels))
random.shuffle(combined)

# Unpack shuffled data back into lists
shuffled_dates, shuffled_labels = zip(*combined)

# --- Step 6: Assign to DataFrame ---
df["Order_Date"] = shuffled_dates
df["Festival"] = shuffled_labels

# --- Step 7: Save the result ---
output_path = "Food_Mood_2022_With_Festival.xlsx"
df.to_excel(output_path, index=False)

print("✅ Order_Date and Festival columns updated.\nSaved as:", output_path)
