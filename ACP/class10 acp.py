# convert decimal to binary number
n=int(input("enter the number"))
num=n
str1=""
while num>0:
    rem=num%2
    str1=str(rem)+str1
    num//=2
print("the binary number ",23)
print(str1)