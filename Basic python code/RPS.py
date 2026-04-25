import random
print("🪨        ✂️      📃")
option =["rock","scissor","paper"]
while True:
    userchoice=input("choose any one = rock ,scissor,paper,exit \n ").lower()
    if userchoice=="exit":
        print("thanks for playing ")
        break
    if userchoice not in option :
        print("invalid choice ")
        continue 
    computerchoice=random.choice(option)
    print(f"computer choice ->{computerchoice}")
    if computerchoice==userchoice :
        print("tie ")
        continue
    elif (
        (userchoice=="rock" and computerchoice == "scissor" ) or
        (userchoice=="paper"and computerchoice=="rock")or
        (userchoice=="scissor" and computerchoice=="paper")   
    ):
        print("you won bhai 🎉 ")
        continue
    else:
        print("computer won 💻")
        continue