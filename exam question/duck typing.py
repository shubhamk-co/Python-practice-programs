class dog:
    def speak(self):
        print("bwoof")
    
class cat:
    def speak(self):
        print("meow")

def duck(obj):
    obj.speak()


d=dog()
c=cat()

duck(d)
duck(c)