# Q1. Write a function greet() that prints "Hello, Data Scientist!".
# def greet():
#     print("Hello , Data Scientist !")
# greet()

#Q3. Write a function print_info(name, age=20) that prints the student's name and age. Call it with and without age.
# def print_info(name,age=20):
#     print("name is",name)
#     print("age is",age)
# # print_info("shubham",30)
# print_info("anurag")

#Q4. Write a function that accepts any number of marks (using *args) and returns their average.
# def marks(*args):
#     total=0
#     for i in args:
#         total+=i
#     return total/len(args)
# print(marks(4,56,7))

# Q5. Write a function square(num) that returns the square of a number.
# def square(num):
#     return num*num
# print(square(5))

# Q6. Write a function that takes a string and returns the number of vowels in it.
# def vowals_in(words):
#     a="aeiou"
#     count=0
#     for i in words:
#         if i in a:
#             count+=1
#     return count
# print(vowals_in("shubham"))

#Q7. What will be the output of the following code? Explain the concept of scope:
# x = 10

# def show():
#     x = 5
#     print("Inside function:", x)

# show()
# print("Outside function:", x)

# Q8 . Modify the code so that the function changes the global value of x
# x = 10

# def show():
#     # global x   #global when we use when we want to change the value variable of outside the function 
#     x = 5
#     print("Inside function:", x)

# show()
# print("Outside function:", x)

# Q9. Convert the following to a lambda function:

# def multiply(a, b):
#     return a * b

# multiply= lambda a,b:a*b
# print(multiply(4,4))

# def func(*nums):
#     return sum(nums)
# print(func(1,2,3,4,5,6,7,8,9))

# Q5. Write a function to return the largest element in a list
# def func(lists):
#     a=lists[0]
#     for num in lists:
#         if num>a:
#             a=num
#     return a
# print(func([100,56,150,57,88]))

# Write a function to reverse a string.
# def rev(org):
#     return org[::-1]
# org=input("Enter a string:")
# print(rev(org))

#  Write a function to generate Fibonacci series up to n terms.
# def fibonacci(n):
#     a=0
#     b=1
#     emp_list=[]
#     for i in range(n):
#         emp_list.append(a)
#         a, b = b, a + b 
#     return emp_list
# print(fibonacci(10))


num=int(input("enter  a number :"))
result=1
for i in range(1,num+1):
    result*=i
print(result)

