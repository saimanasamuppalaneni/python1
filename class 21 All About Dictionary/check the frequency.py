# check the frequency 
mydic1 = {'codingal':2,'is':2,'for':2,'best':1,'coding':3}
k = 2
count = 0
for value in mydic1.values():
    if value == 2:
        count += 1
print("the words which have 2 frequency is ",count)