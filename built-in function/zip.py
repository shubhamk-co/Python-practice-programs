# names = ["Alice", "Bob", "Charlie"]
# scores = [85, 90, 95]
# a=list(zip(names,scores))
# print(a)

# Use zip() with different-length lists:
# a = [1, 2, 3, 4]
# b = [10, 20]
# zipped=list(zip(a,b))
# print(zipped)

# Convert zipped object into a dictionary:

# keys = ["name", "age", "city"]
# values = ["Alice", 25, "Delhi"]
# zipped=dict(zip(keys,values))
# print(zipped)


# Unpack zipped pairs using *:

# pairs = [(1, 'a'), (2, 'b'), (3, 'c')]
# num,char=zip(*pairs)
# print(num)
# print(char)

# Sum two lists element-wise using zip() and list comprehension:

# a = [1, 2, 3]
# b = [4, 5, 6]
# c=[x+y for x,y in list(zip(a,b))]
# print(c)

# Check if all elements in two lists are equal position-wise:
# a = [1, 2, 3]
# b = [1, 2, 4]
# compare=[x==y for x,y in list(zip(a,b))]
# print(compare)

# Transpose a matrix using zip():

# matrix = [
#     [1, 2, 3],
#     [4, 5, 6]
# ]
# zip_matrix=list(zip(*matrix))
# print(zip_matrix)

# # Iterate over three lists at once and format a string:
# names = ["Alice", "Bob"]
# scores = [85, 90]
# grades = ["A", "B"]
# zipped=list(zip(names,scores,grades))
# for name,score,grade in zipped:
#     print(f"{name} got {score} and grade {grade}")

# Create a list of dictionaries from multiple lists:
# headers = ["name", "age"]
# data = [
#     ["Alice", 25],
#     ["Bob", 30]
# ]
# # Output: [{"name": "Alice", "age": 25}, {"name": "Bob", "age": 30}]
# zipped=dict(zip(headers,row) for row in data)
# print(zipped)



# What happens if you zip a list with itself?

# a = [1, 2, 3]
# zipped = list(zip(a, a))
# print(zipped)

# Why does zip() return an empty object sometimes?
a = [1, 2]
b = [3, 4]
zipped = zip(a, b)
list1 = list(zipped)
list2 = list(zipped)
print(list1)
# Why is list2 empty?
print(list2)