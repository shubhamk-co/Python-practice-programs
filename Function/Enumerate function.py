# mark=[23,45,78,65,32,14,78,98,12,35]
# for i in range(len(mark)):
#     print(mark[i])
#     if i == 7:
#         print("Topper")

# 1. Print Index and Item
# Question: Print the index and name from the list using enumerate().

# names = ["Alice", "Bob", "Charlie", "Daisy"]
# for index,name in enumerate(names):
#     print(f"{index} : {name}")

# 2. Custom Start Index
# Question: Print items with a custom index starting from 101.

# subjects = ["Math", "Science", "History", "English"]
# for index,subject in enumerate(subjects,start=101):
#     print(f"{index} : {subject}")

#  3. Modify List Based on Index
# Question: Replace every item at even index in a list with "Even"

# colors = ["Red", "Green", "Blue", "Yellow", "Pink"]
# for index,color in enumerate(colors):
#     if index%2==0:
#         colors[index]="Even"
# print(colors)

# 4. Use enumerate() with Strings
# Question: Count how many vowels are in each index of a string and print the index and vowel

# vowel="aeiou"
# texts="enumerate"
# for index,text in enumerate(texts):
#     if text in vowel:
#         print(f"{index} : {text}")

#  5. Index of Matching Item
# Question: Find index of the word "Python" in the list using enumerate().

# words = ["Java", "C++", "Python", "Ruby", "Python"]
# for index,word in enumerate(words):
#     if "Python" == word:
#         print(f"{word} found at {index} ")

# 6. Build a Dictionary from List Using enumerate()
# Question: Convert a list into a dictionary where keys are indexes and values are items.

# fruits_dict={}
# fruits = ["Apple", "Banana", "Mango"]
# for index ,fruit in enumerate(fruits):
#     dict.update({index:fruit})
# print(dict)

# 7. Reverse a list using enumerate()
# Question: Without using reverse function, create a new list in reverse order using enumerate() and indexing.

# listnumber=[1,2,3,6,4,44,68,9,5,4,2]
# reverselist=[0]*len(listnumber)

# for index,listnum in enumerate(listnumber):
#     reverselist[len(listnumber)-1-index] = listnum
# print(reverselist)

#  8. Skip Odd Indices
# Question: Print only elements that are at even indices using enumerate().
new_list=[]
listnumber=[1,2,3,6,4,44,68,9,5,4,2]
for index,listnum in enumerate(listnumber):
    if index%2==0:
        new_list.append(listnumber)
print(listnumber)
        