# check the character ocurrence in a phrase
str1=input("enter the word")
ch=input("enter the character to be counted")
count=0
for i in str1:
    if i.lower()==ch.lower():
        count+=1
print(f"the no. of {ch} occured in {str1} is {count}")