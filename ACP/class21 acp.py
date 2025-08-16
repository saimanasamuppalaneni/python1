# check the frequency
mydic1 = {'bread':2,'butter':2,'toast':2,'strawberries':1,'chocolate':3}
k = 2
count = 0
for value in mydic1.values():
    if value == 2:
        count += 1
print("the words which have 2 frequency is ",count)