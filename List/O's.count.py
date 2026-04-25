list=["mango","rohan","jon","shubham","aman","Riya","Nishant"]
print("before removing from list",list)
# for name in list :
#     if "o" in name :
#         list.remove(name) 
#This code have a bug because we are iterating and removing same time 

#Solution 1
# for name in list[:]:
#     if "o" in name :
#         list.remove(name) 

#Solution 2 
list=[names for names in list if "o" not in names]
print("After removing name's having o's from list :" ,list)

