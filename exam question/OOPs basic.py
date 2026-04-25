class student:

    school="kvs"

    def __init__(self,name,age):
        self.name=name
        self.age=age

    def display(self):
        print("name:",self.name)
        print("age:",self.age)

    @classmethod
    def change_school_name(cls,new_name):
        cls.school=new_name
        print("new school name :",cls.school)

    @staticmethod 
    def greeting():
        print("static method ")

s1=student("shubham",12)
s2=student("sharma",14)
s1.display()
s2.display()
s1.greeting() #staticmethod
student.change_school_name("kvs1") 