#length

# Q1. Take a string input from the user and print the number of characters using len().
# line=input("Enter a string :")
# a=len(line)
# print(a)

# Q2. Write a function that returns the number of words in a sentence using len() and split()
# def words(sentence):
#     word=sentence.split()
#     return len(word)
# user_input=input("Enter a sentence :") #strip() -> use for remove first and last space in the sentence 
# print(words(user_input))

#  Q3. Write a function that returns the sum of a list of numbers..
# def num(number):
#     return sum(number)
# a=[1,2,3,6,4,5]
# print(num(a))

#  Q4. Ask the user to input 5 numbers and print their total using sum().
# list=[]
# for i in range(5):
#     num=int(input("Enter a number :"))
#     list.append(num)
# total=sum(list)
# print(total)

# Use map() and lambda to convert a list of temperatures in Celsius to Fahrenheit.Formula: F = (C × 9/5) + 32

# celsius=[78,56,48,32,69]
# fahrenheit= list(map(lambda c:c*9/5 + 32 ,celsius))
# print(fahrenheit)

# Use map() to convert a list of strings into uppercase:
# words = ['data', 'science', 'python']
# a=list(map(lambda c:c.upper(),words))
# print(a)

# Use filter() and lambda to get all even numbers from this list:
# nums = [1, 3, 4, 6, 8, 9]
# a=list(filter(lambda e:e%2==0,nums))
# print(a)

# Use filter() to get all words longer than 4 characters from this list:
# words = ['data', 'science', 'is', 'cool']
# a=list(filter(lambda e:len(e)>4,words))
# print(a)

# Q9. You have two lists:Use zip() to pair them and print: Alice - 85, Bob - 90, etc.
# names = ['Alice', 'Bob', 'Charlie']
# scores = [85, 90, 78]
# a=dict(zip(names,scores))
# print(a)

# Q10. Use zip() to add elements from two lists:output = [5, 7, 9]
# a = [1, 2, 3]
# b = [4, 5, 6] 
# sum=[x+y for x,y in zip(a,b)]
# print(sum)