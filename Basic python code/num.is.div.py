def Divi(nums):
    
    temp=nums
    ans=0
    while temp>0:
        r=temp%10
        if nums%r==0:
            ans+=1
        temp//=10
    return ans 

nums=(int(input("Enter a number :")))
print(Divi(nums))
