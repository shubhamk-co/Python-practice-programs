a={"apple","mango","banana","peach","Date"}
b={"apple","mango","orange","pineapple","strawberry","berry"}

c={1,2,3,4,5,6}#superset of d
d={1,2,3,4}#subset of c

#print(a.isdisjoint(b))#not common
#print(c.issubset(d))#kya c bachha hei d ka
#print(c.issuperset(d))#kya d bachha hei c ka

# a.add("Grapes")
# print(a)

# a.remove("Date")#or discard
# print(a)

# a.pop()#we dont know what item will be popped
# print(a)

print(c)#Deletes the set
del c

print(d)
d.clear()#Deletes the elements inside the set
print(d)