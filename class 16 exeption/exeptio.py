# exeption
try:
    n=int(input("enter the number"))
    print("the value is entered ",n)
except ValueError as ex:
    print("a error occured",ex)