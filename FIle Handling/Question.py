# Q1.
# Create a text file named notes.txt and write "Python is fun!" into it.
# file=open("notes.txt","w")
# file.write("python is fun ")

# Q2.
# Read and print the entire content of a file named story.txt.
# f=open("story.txt","r")
# content=f.read()
# print(content)

# Q3.
# Write a Python program to append "This is a new line" to a file named story.txt
# with open("story.txt","a") as file:
    # file.write("This is a new line ")

# Q4.
# Check if a file data.csv exists or not. If it exists, print “Found”; otherwise print “Missing”.
# import os
# if os.path.exists("data.csv"):
#     print("file found")
# else:
#     print("Missing")

# Q5.
# Create a file called greetings.txt and write the following lines using writelines() method:
# ["Hello\n", "Good Morning\n", "Welcome to Python\n"]
# file=open("greetings.txt","x")
# file.writelines(["Hello\n","Good Morning\n","Welcome to python\n"])

# Q6.
# Create a file numbers.txt with numbers 1 to 10 (each on a new line). Then read and print only even numbers from the file.
# with open("number.txt","w") as file:
#     file.writelines(["1\n","2\n","3\n","4\n","5\n","6\n","7\n","8\n","9\n","10\n"])

# with open("number.txt","r") as file:
#     content = file.readlines()
#     for num in content:
#         num = int(num.strip())  # remove \n and convert to int
#         if num % 2 == 0:
#             print(num)

# Write a program to count how many lines are there in a file named poem.txt
