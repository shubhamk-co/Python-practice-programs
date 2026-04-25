# Create dictionary of months and number of days
months = {
    "January": 31,
    "February": 28,
    "March": 31,
    "April": 30,
    "May": 31,
    "June": 30,
    "July": 31,
    "August": 31,
    "September": 30,
    "October": 31,
    "November": 30,
    "December": 31
}

print(months.items())
# (a) Ask user for month name and print number of days
# month = input("Enter month name: ")

# if month in months:
#     print("Number of days:", months[month])
# else:
#     print("Invalid month name")

# # (b) Print all keys in alphabetical order
# print("\nMonths in alphabetical order:")
# for m in sorted(months.keys()):
#     print(m)

# # (c) Print months with 31 days
# print("\nMonths with 31 days:")
# for m, d in months.items():
#     if d == 31:
#         print(m)



