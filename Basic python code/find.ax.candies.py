candies=[2,3,5,1,3]
extracandies=3
max_candies=max(candies)
ans=[]
# print(max_candies)
for i in candies:
    if (i+extracandies)>=max_candies:
        ans.append("True")
    else:
        ans.append("False")
# print(ans)
    # return ans