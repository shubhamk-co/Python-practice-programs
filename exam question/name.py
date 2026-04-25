name=input("enter a name")
gender=input("enter a genter ").lower()
if gender=="male" or "m":
    print(f"mr.{name}")
elif gender=="female" or "f":
    print(f"MS.{name}")
else:
    print("invalid ")