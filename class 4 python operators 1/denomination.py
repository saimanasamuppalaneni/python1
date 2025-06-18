# denomination calculator
amt=int(input("enter the amount"))
note500=amt//500
note100=(amt%500)//100
note50=(amt%500)%100//50
print("number of 500 notes",note500)
print("number of 100 notes",note100)
print("number of 50 notes",note50)
