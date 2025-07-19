# cube of a number
n=int(input("enter the number"))
def cube(x):
    return x**3
def divby3(n):
    if n%3 == 0:
        return cube(n)
    else:
        return False
print(f"the cube of the number is",divby3(n))