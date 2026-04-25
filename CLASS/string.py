# st="this is a string "
# print(st [0])

# str=("unit 1","unit 2","unit 3")
# print(".".join(str))

# str=(1,2,3,4,5,6)
# print(str[-1:len(-1)])

# b.Write a program to count all the vowels in the string.
# Accept string from user.

# user_input=input("Enter a string :")
# vowels=("a","e","i","o","u")
# count=0
# for i in user_input :
#     if i in vowels:
#         count+=1    
        
# if count==0:
#     print("the string has not vowels")
# else :
#     print("no of vowels in string is ",count)

# Write a program to check whether a string is palindrome or not.
user_input=input("enter a stirng ")
pal=user_input[::-1]
if user_input==pal:
    print("string in palindrom")
else:
    print("is not palindrom")