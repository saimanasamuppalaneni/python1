#multiple exeption
try:
    num1,num2=eval(input("enter two numbers separated by commas"))
    s=num1/num2
    print("the value is",s)
except ZeroDivisionError as ex:
    print(ex)
except SyntaxError as ex:
    print(ex)
except:
    ("an error occured")
else:
    ("no error")
finally:
    print("whatever happens this statement will get executed")