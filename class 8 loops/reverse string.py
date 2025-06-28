# reverse the string
string1=(input("enter your phrase you want to reverse"))
reverse=""
for i in string1:
    reverse=i+reverse
print("you reversed phrase is",reverse)