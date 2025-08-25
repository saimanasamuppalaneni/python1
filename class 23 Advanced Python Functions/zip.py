# zip function
list1 = [1,2,3,4]
list2 = ['a','b','c','d']
print(list(zip(list1,list2)))
print(list(zip(list1,list2[::-1])))
s = ['reliance','infosys','tcs']
p = [1345,5667,2345]
mydic1 = {stocks : prices for stocks,prices in zip(s,p)} 
print(mydic1)