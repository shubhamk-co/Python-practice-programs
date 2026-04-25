import pandas as pd 
import matplotlib.pyplot as plt

file="D:\Downloads\dirty_employee_data.xlsx"
df=pd.read_excel(file)
print(df)
# df.fillna("unknown",inplace=True)
# df.dropna(inplace=True)
# Identify rows where any value is missing.
print("\nPRINT MISSING VALUE\n",df[df.isnull().any(axis=1)])
# Fill missing Name with "Unknown"
# print('\nTHIS IS CLEAN DATA:\n',df)
df['Name'].fillna("unknown",inplace=True)
# Fill missing Age with the average age (excluding negative values).
avg_age=df["Age"][(df["Age"]> 0) & (df["Age"].notnull())]
print(avg_age)
avg=avg_age.mean()
df["Age"].fillna(avg,inplace=True)
# print(df["Age"])



# USING MATPLOTLIB
# 1)find avg salaryof each employee
df.dropna(["Salary"],inplace=True)
avge_salary=df.groupby("Name")["Salary"].mean()
avge_salary.plot(color="skyblue")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("Average salary")
plt.show()
