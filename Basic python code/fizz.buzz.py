def Fizz_buzz(number):
    ans=[]
    # number=int(input("Enter a number :"))
    for i in range(1,1+number):
        if i%3==0 and i%5==0:
            ans.append("FizzBuzz")
        elif i%3==0:
            ans.append("Fizz")
        elif i%5==0:
            ans.append("Buzz")
        else :
            ans.append(str(i)) 
    return ans
print(Fizz_buzz(int(input("Enter a number :"))))