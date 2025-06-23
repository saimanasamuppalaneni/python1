# exam eligibility
mc=input("enter if you have medical cause or not(y\n)")
if mc.lower() == "y":
    print("the student is allowed to write the exam")
elif mc.lower() =="n":
    att=int(input("enter the student attendance"))
    if att>75:
        print("you can write the exam")
    else:
        print("you are not eligible to write exam")
else:
    print("invalid input")