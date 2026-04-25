def calculator(a,b):
    i=(a+b)+(a-b)
    print(i)

def isGrater(a,b):
    if (a>b):
        print("first value is grater :",a)
    elif(a==b):
        print("both first and second value are equal")
    else:
        print("second value is grater :",b)
a=2
b=5
calculator(a,b)
isGrater(a,b)
c=10 
d=4
calculator(c,d)
isGrater(c,d)