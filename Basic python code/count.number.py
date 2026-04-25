def countnum(list):
    ans=[]
    for i in list:
        c=0
        for j in list:
            if i>j:
                c+=1
        ans.append(c)
    return ans

list=[8,1,2,2,3]
print(countnum(list))