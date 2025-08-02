# age counter
try:
    n=int(input("enter your age"))
    print("the age is entered ",n)
except ValueError as ex:
    print("a error occured",ex)
    n=int(input("enter your age again to check if it is even or odd!!"))
if n %2==0:
    print("the number is an even number")
else:
    print("the number is an odd number")
    