# generate prime number
l=int(input("enter the lower number"))
u=int(input("enter the upper number"))
for i in range (l,u+1):
    for j in range (2,i):
        if i%j==0:
            break
    else:
        print(i)