# Write a lambda function to calculate the cube of a number.
# (using function )
# def cube(num):
#     number=lambda x:x**3
#     return number(num)
# print(cube(5))

# (using without function)
# cube=lambda x:x**3
# print(cube(4))

# Create a lambda to check if a number is positive.
# pos=lambda x:x>0 
# print(pos(-8))

# Write a lambda function that takes two numbers and returns the maximum of the two.
# a=int(input("Enter a number :"))
# b=int (input ("enter number :"))
# check_max=lambda a,b:a if a>b else b                                                            #important 
# print("maximum number is :",check_max(a,b))

# Given a list of numbers: nums = [1, 2, 3, 4, 5],
# Use map() and a lambda to double each number.
# nums = [1, 2, 3, 4, 5]
# num_double=list(map(lambda x:x*2,nums))
# print(num_double)

# convert a list of names to uppercase using map() and lambda.
# Example: ["alice", "bob", "mike"] → ["ALICE", "BOB", "MIKE"]

# list_upper=["alice", "bob", "mike"]
# upper=list(map(lambda x:x.upper(),list_upper))
# print(upper)                                                                         # map() = change the value 

# # Convert a list of strings to their lengths using lambda + map()
# str_list=["apple","banana","strowbarry","mango"]
# num_list=list(map( lambda x:len(x) ,str_list))
# print(num_list)

# Filter all numbers greater than 10 using lambda and filter().                        # filter() = is filter base on condition 
# num=[1,25,56,8,15,8]
# greater_num=list(filter(lambda x:x>10,num))
# print(greater_num)

# Use filter() + lambda to get all even numbers from a list:
# even=[10, 3, 5, 8, 12, 7]
# even_list=list(filter(lambda x:x%2==0,even))
# print(even_list)

# Filter all strings in a list that start with the letter ‘A’ or ‘a’
# str=["Apple", "banana", "Avocado", "mango", "apricot"]
# a_list=list(filter(lambda x:x[0]=="a" or x[0]=="A",str ))
# print(a_list )

# From a list of names, use map() + lambda to return this format:
# Input: ["Alice", "Bob", "Charlie"]
# Output: ["Name: Alice", "Name: Bob", "Name: Charlie"]

# input= ["Alice", "Bob", "Charlie"]
# inp_map=list(map( lambda x:"Name:"+x,input))
# print(inp_map)

# From a list of integers, filter only the perfect squares (e.g., 1, 4, 9, 16...) using filter() and lambda
# numbers = [1, 2, 3, 4, 5, 9, 10, 16, 20, 25, 30]   
#                                                                   (((((((using import math )))))))
# perfect_squ=list(filter(lambda x:x**x==,numbers))
# print(perfect_squ )


# Filter even numbers from a list

# nums = [1, 2, 3, 4, 5, 6]
# evens = list(filter(lambda x:x%2==0, nums))
# print(evens)

# nums = [1, 2, 3, 4]
# squares = list(map(lambda x:x**2, nums))
# print(squares)  # Output: [1, 4, 9, 16]

