# list=["Delhi", "Mumbai", "Delhi", "Bangalore", "Mumbai"]
# print(type(list))
# list=set(list)
# print(type(list))
# print(list)

#Q2
# fav_cities = {"Delhi", "Goa", "Manali"}
# if "pune" in fav_cities :
#     print("pune is in the set ")
# else:
#     print("pune not in cities")
# if "Goa" in fav_cities:
#     print("goa is in the set")
# else:
#     print("goa is not in the set")

#Q3
# north = {"Delhi", "Punjab", "Haryana"}
# south = {"Chennai", "Kerala", "Delhi"}
# print(north.symmetric_difference(south))
# print(north.difference(south))

#Q4
# sample =set()
# sample.add("football")
# sample.add("criket")
# sample.add("Ludo")
# sample.add("badminton")
# sample.add("hockey")

# print("Before removing the element ",sample )

# sample.pop()
# print("After removing element in the list ",sample)

#Q5
# person1 = {"Reading", "Swimming", "Gaming", "Cooking"}
# person2 = {"Dancing", "Cooking", "Gaming", "Painting"}
# c=(person1.union(person2))
# print("set c:",c)

# #Q6
# print(person1.difference(person2))

#Q7 check attendance 
# students = {"Aman", "Riya", "Simran", "Tina", "Karan"}
# absent = {"Simran", "Tina"}

# print("this student are present :",students.difference(absent))

#Q8 update clud 
# club = {"Rohan", "Aman", "Riya"}
# new_joined = {"Simran", "Ali", "Riya"}
# club.update(new_joined)
# print("updated club :",club)

#Q9
# emails = ["a@gmail.com", "b@gmail.com", "a@gmail.com", "c@gmail.com", "b@gmail.com"]
# emails=set(emails)
# print("print set :",emails)

# emails.add("shubham@gmail.com")
# print("print updated email",emails)

#Q10

# word1 = "hello"
# word2 = "world"
# w1=set(word1)
# w2=set(word2)
# common = w1.intersection(w2)
# print("Common letters:", common)

# # Unique letters in word1
# unique_word1 = w1.difference(w2)
# print("Unique letters in word1:", unique_word1)

# # All letters used in both words
# all_letters = w1.union(w2)
# print("All letters used:", all_letters)

#Q11
list=[1,2,3,4,5,6,7,1,2,7,3,6,4]
print("before removing repetative element :",list)
new_list=[]
for i in list:
    if i not in new_list:
        new_list.append(i)
print("After removing repetative element :",new_list )

