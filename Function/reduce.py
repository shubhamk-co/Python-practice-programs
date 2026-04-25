from functools import reduce  # step by step combine the number 
                                # Step 1: 2*3  → 6
                                # Step 2: 6*4 → 24
# num=[2, 3, 4]
# mult =reduce(lambda a,b:a*b,num)
# print(mult)

# inding the maximum value in a list using reduce()?
numbers = [10, 45, 23, 67, 12, 98, 34]
max=reduce(lambda a,b:a if a>b else b,numbers)
print(max)


# or using reduce to join strings like ["Hello", "World"] → "Hello World"?
str=["Hello", "World"]
add=reduce(lambda a,b:a + b,str)
print(add)

str2=["Python", "is", "awesome"]
pr=reduce(lambda a,b: a+" "+b,str2)
print(pr)