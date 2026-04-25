#recursion means function call itself with in the same function 
def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
print(factorial(5))

# using without recursion
def func(num):
    result=1
    for i in range(1,num+1):
        result*=i
    return result
num=int(input("Enter a number: "))
print(func(num))