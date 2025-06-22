# alphabet or not
c=input("enter the character")
if len(c)>1:
    print("\n invalid input")
else:
    if c>='a'and c<='z':
        print("\n\"" +c+ "\"is an alphabet.")
    elif c>='A'and c<='Z':
        print("\n\"" +c+ "\"is an alphabet.")
    else:
        print("\n\"" +c+ "\"is not a alphabet.")



