# ✅ Create a class Person with attributes name and age. Add a method to display details.
# class person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age

#     def display(self):
#         print(f"name is :{self.name} \nage is {self.age}")

    
# p=person("shubham",12)
# p.display()


# # ✅ Create a class Student that inherits from Person and adds a marks attribute.
# class student(person):
#     def __init__(self,name,age,marks):
#         super().__init__(name,age)
#         self.marks=marks

#     def disp(self):
#         print(f"name is :{self.name}  \nage is {self.age} \nmarks:{self.marks}")

# s=student("shubham",16,88)
# s.disp()

# ✅ Make a class Rectangle with length and breadth. Add methods to calculate area and perimeter.
# class rectangle:
#     def __init__(self,length,breadth):
#         self.length=length
#         self.breadth=breadth

#     def calculate(self):
#         print(f"{self.length}X{self.breadth}",self.length*self.breadth)

#     def perimeter(self):
#         print(f"2({self.length}X{self.breadth})",2*(self.length*self.breadth))

# r=rectangle(4,5)
# r.calculate()
# r.perimeter()

# Create a class Employee with name, emp_id, and salary. Inherit and make a class Manager with department info.
# class Employee:
#     def __init__(self,name,emp_id,salary):
#         self.name