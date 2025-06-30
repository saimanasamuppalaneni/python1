# armstrong number
n=int(input("enter the number"))
t=n
sum=0
while t>0:
    r=t%10
    sum+=r**3
    t//=10
if sum==n:
    print(f"{n} is a armstrong number")
else:
    print(f"{n} is not an armstrong number")