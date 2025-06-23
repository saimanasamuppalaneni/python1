# customize your ride
ch=int(input("\n1.Bike\n2.car\nenter your choice"))
if ch==1:
    ch1=int(input("\n1.bike\n2.Scooty\n enter you choice"))
    if ch1==1:
        print("you have choosen bike")
    elif ch1==2:
        print("you have choosen scooty")
    else:
        print("invalid input")
elif ch==1:
    ch1=int(input("\n1.ford\n2.kia\n enter you choice"))
    if ch1==1:
        print("you have choosen ford")
    elif ch1==2:
        print("you have choosen kia")
    else:
        print("invalid input")
else:
    print("wrong choice")