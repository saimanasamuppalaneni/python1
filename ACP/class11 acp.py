# mirrored triangle
n=int(input("enter the number of rows"))
space=0
for i in range(n,0,-1):
    for k in range(space):
        print(end=" ")
    for j in range(1,i):
        print("*",end="")
    space+=1
    print()
