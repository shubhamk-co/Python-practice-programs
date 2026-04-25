# # simple inheritance 
# class A:

#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
        
#     def display(self):
#         print(self.name,self.age)

# class B(A):
#     def __init__(self,name,age,rollno,marks):
#         super().__init__(name,age)
#         self.rollno=rollno
#         self.marks=marks

#     def display(self):
#         super().display()
#         print(self.rollno,self.marks)


# b=B("shubham",20,23,12)
# b.display()

# multilevel inheritance

# class A:
#     def grand_method(self):
#         print("this is your grandfather")

# class B(A):
#     def father_method(self):
#         print("this is your father")

# class C(B):
#     def child_method(self):
#         print("this is child ")

# c=C()
# c.grand_method()
# c.father_method()
# c.child_method()

# hierarchical inheritance

# class A:
#     def parent_method(self):
#         print("this is parent class ")

# class B(A):
#     def child_method(self):
#         print("this is child method ")

# class C(A):
#     def child2_method(self):
#         print("this is second child method")

# b=B()
# b.parent_method()
# b.child_method()
# c=C()
# c.parent_method()
# c.child2_method()

# mulitple inheritance

# class A:
#     def parent1(self):
#         print("this is parent 1 method ")


# class b:
#     def parent2(self):
#         print("this is parent 2 method ")

# class C(A,b):
#     def child(self):
#         print("this is child method ")

# c=C()
# c.parent1()
# c.parent2()
# c.child()

class Test:
    def m1(self):
        print('no-arg method')

    def m1(self, a):
        print('one-arg method')

    def m1(self, a, b):
        print('two-arg method')

t = Test()
t.m1(10)
