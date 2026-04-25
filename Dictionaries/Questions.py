# dict={ "rohit":85, "shubham":75,"nishant":98,"neha":99}
# print(dict.keys())
# print(dict.values())
# print(dict.items())


# Q2
# dict2={'English':85, 'Maths':90, 'Science':80}
# if 'Maths' in dict2:
#     print("maths is found :")
# else:
#     print("maths is not found ")
# dict2.update({'history':75})
# print(dict2)
# dict2.update({'Science':95})
# print(dict2)
# dict2.pop("English")
# print(dict2)

#Q3
# dict1 = {'a': 100, 'b': 200}
# dict2 = {'c': 300, 'd': 400}

# dict1.update(dict2)
# print(dict1)


# Q4 ) create a  dictionary for tow list 
# keys = ['name', 'age', 'gender']
# values = ['John', 25, 'Male']

# new_dict=dict(zip(keys,values))
# print(new_dict)

#Q5)
# list=[1,5,4,8,3,4,6,97,1,3,4,3,9,42,3,5,4,25,191,2,9,9,2,99,6,9]
# new_set=set(list)
# print(new_set)

#Q6 )write a program to find maxmim element from dictionary 
# dict ={'A': 10, 'B': 50, 'C': 30}
# maximum=max(dict.items(),key=lambda x:x[1])         #useed with sorted /max/ min
# print(maximum)
# for keys,values in dict :
#     if

#Q7 )list of tuples
# data = [('A', 10), ('B', 50), ('C', 30)]
# maxa=max(data,key=lambda x:x[0])
# print(maxa)