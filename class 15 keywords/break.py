# checking alphabets in the phrase
string1=input("enter the phrase")
ch=input("enter the character")
for i in string1:
    if ch == i:
        print(ch,"found in the given string")
        break
else:
    print(ch,"not found")