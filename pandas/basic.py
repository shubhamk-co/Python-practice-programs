import pandas as pd

file_path = r"C:\Users\shubh\Desktop\GoogleAds_DataAnalytics_Sales_Uncleaned.csv"

df = pd.read_csv(file_path)

print(df.head())

print("print ID:",df[df["Ad_ID"]=="A1003"])
# print("print location ",df[df["Location"]=="mumbai"])
df.drop("Keyword",axis=1,inplace=True)
print(df.head(10))
df.drop("Device",axis=1,inplace=True)

df.drop(df.index[25:2600],axis=0,inplace=True)

df.drop("Impressions",axis=1,inplace=True)
print(df)

import matplotlib.pyplot as plt
x=["Device"]
y=["Sale_amount"]
plt.bar(x,y ,color='black')  #.bar ,.dis,.plot
plt.title("Bar chart")
plt.show()