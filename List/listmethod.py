#insertion
list=[8,6,5,4,3,1,9,2,8,6,8,8]
# for i in range(5):
#     element = int(input(f"enter the element at {i+1} : "))
#     list.append(element)
print("after append :",list)

#Deletion
list.remove(4)
print("after deletion :",list)

#sort
list.sort()
print("after sort :",list)

#Reverse
list.reverse()
print("after reverse :",list)

#Count 
num=list.count(8)
print("after count :",num)


#maximum & minimum
print("maximum : ",max(list))
print(" minimum : ",min(list))


