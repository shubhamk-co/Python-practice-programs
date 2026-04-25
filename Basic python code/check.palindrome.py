def palindrome(x):
    temp=x
    rev=0
    while temp>0:
        r=temp%10
        temp//=10
        rev=rev*10+r
    # return rev==x
    if rev==x:
        print("number is palindrome....😎")
    else:
        print("number are not palindrome >>>>😅")

x=int(input("Enter a number :"))
palindrome(x)