def product_sum(n):
    temp=n
    sum=0
    mult=1

    while temp>0:
        r=temp%10
        temp//=10
        sum+=r
        mult*=r

    return mult-sum
n=int(input("Enmter anumber :"))
print(product_sum(n))

