# Create a Python program that stores the names of 5 fruits in a list. Print the first and last fruit.
# fruits=["apple","mango","kiwi","graphs","orange"]
# print(fruits[0],fruits[-1])

# Create a tuple with 4 different programming languages. Print the second element.
# t=(1,2,3,4,5,6,7)
# print(t[1])

# Create a dictionary with student names as keys and their marks as values. Print the marks of one student.
d={
    1:{"name":"shubham","marks":"75"},
    2:{"name":"amit","marks":"85"}
}
print(d.values())
for key in d:
    print(d[key]["name"])
