# infinite loop
flag=True
while flag:
    try:
        n=int(input("enter the number"))
        if n%2==0:
            while True:
                print("bye")
        else:
            print (n,"is an odd number")
            flag=False
    except:
        print("an error occured")