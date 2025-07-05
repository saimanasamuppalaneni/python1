# mid product
n=int(input("enter the number"))
strn=str(n)
l=len(strn)
if l%2==0:
    mid=l//2-1
else:
    mid=l//2
product=int(strn[mid])*int(strn[mid+1])
print("the product is",product)
