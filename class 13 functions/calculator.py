# calculator
def add (a,b):
    return (a + b)
def sub (a,b):
    return (a - b)
def mul (a,b):
    return (a * b)
def div (a,b):
    return (a / b)
op=input("1.Addition\n2.Subtraction\n3.multiplication\n4.Division\nEnter your choice!!!")
n1=int(input("enter the first number"))
n2=int(input("enter the second number"))
if op =="1":
    print(f"{n1}+{n2}={add (n1,n2)}")
elif op =="2":
    print(f"{n1}-{n2}={sub (n1,n2)}")
elif op =="3":
    print(f"{n1}*{n2}={mul (n1,n2)}")
elif op =="4":
    print(f"{n1}/{n2}={div (n1,n2)}")
else:
    print("invalid input!!")