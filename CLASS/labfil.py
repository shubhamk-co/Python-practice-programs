# str = "shubham kumar"
# print("First six chars       : ", str[0:6])
# print("First six chars       : ", str[:6])
# print("First six chars       : ", str[0:6:1])
# print("Second word           : ", str[6:])
# print("From index 2 to end   : ", str[2:])
# print("Last three chars      : ", str[-3:])
# print("Every 2nd char        : ", str[0::2])
# print("Reverse string        : ", str[::-1])
# print("Index 1 to 6 step 2   : ", str[1:6:2])
# print("Middle part (4 to 9)  : ", str[4:10])
# print("Without first char    : ", str[1:])
# print("Without last char     : ", str[:-1])
# print("Only first char       : ", str[0])
# print("Only last char        : ", str[-1])

# class Student:
#     course = "BCA"  
#     def __init__(self):
#         self.name = None
#         self.age = None
#     def input_data(self):
#         self.name = input("Enter name of student: ")
#         self.age = input("Enter age of student: ")
#     def display(self):
#         print(f"Course of student is {Student.course}")
#         print(f"Name of student is {self.name}")
#         print(f"Age of student is {self.age}")
        
# obj = Student()
# obj.input_data()
# obj.display()

# print("LIST OPERATIONS")
# L = [10, 20, 30, 40, 50]

# print("1. Original List       :", L)
# L.append(60)
# print("2. Append 60           :", L)
# L.insert(2, 25)
# print("3. Insert 25 at index2 :", L)
# L.remove(40)
# print("4. Remove 40           :", L)
# print("5. Pop last element    :", L.pop())
# print("6. Index of 30         :", L.index(30))
# print("7. Count of 20         :", L.count(20))
# L.sort()
# print("8. Sorted List         :", L)
# L.reverse()
# print("9. Reversed List       :", L)
# L.extend([70, 80])
# print("10. Extend with [70,80]:", L)

# print("\nTUPLE OPERATIONS")
# T = (1, 2, 3, 4, 5, 2, 3)

# print("1. Original Tuple      :", T)
# print("2. Element at index 3  :", T[3])
# print("3. Slicing (1:4)       :", T[1:4])
# print("4. Length              :", len(T))
# print("5. Count of 2          :", T.count(2))
# print("6. Index of 3          :", T.index(3))
# print("7. Max element         :", max(T))
# print("8. Min element         :", min(T))
# print("9. Sum of elements     :", sum(T))
# print("10. Convert to List    :", list(T))

# print("\nDICTIONARY OPERATIONS")
# D = {"name": "shubham", "age": 20, "city": "Delhi"}

# print("1. Original Dict       :", D)
# D["country"] = "India"
# print("2. Add country         :", D)
# D["age"] = 21
# print("3. Update age          :", D)
# print("4. Get city            :", D.get("city"))
# print("5. Keys                :", D.keys())
# print("6. Values              :", D.values())
# print("7. Items               :", D.items())
# D.pop("city")
# print("8. Pop city            :", D)
# print("9. Length              :", len(D))
# D.clear()
# print("10. Clear dictionary   :", D)

