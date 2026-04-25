#sum of the element in list 
lit=[1,2,3,5,6,4,6]
sum=0
for num in lit :
    sum+=num
print("the sum of the element of the list :",sum)

##remove duplicates
list=[1,2,3,1,2,3,1,2,3]
print("before removing duplicates:",list )
list1=[]
for num in list :
    if num not in list1 :
        list1.append(num)
print("After removing the duplicates:",list1)
    
#Reverse without using reverse method 
lst=[1,2,3,4,5,6,7,8]
rev=[]
for i in range(len(lst)-1,-1,-1):#range(start ,stop,skip)
    rev.append(lst[i])
print("After reverseing the list:",rev)

#find even number from list 
numbers=[1,2,3,4,5,6,4,5,6,7,8,9]
even=[]
for num in numbers:
    if num%2==0:
        even.append(num)
print("even element of list:",even)

