import random 
choose=(random.randint(1,10))
attempt=5
user_input=int(input("Enter a number :"))
while attempt<0:
    user_input=int(input("Enter a number :"))
    if choose > user_input:
        print("you number is to small")
        attempt-=1
    elif choose < user_input:
        print("you number is to big")
        attempt-=1
    else:
        print(f"choose number is this{choose}")
        attempt=-1