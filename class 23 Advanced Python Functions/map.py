# map
list1 = [23,45,66,77]
list2 = [23,45,12,89]
a = map(lambda x,y: x+y ,list1,list2)
print(list(a))
def sqr(x):
    return x * x
b = list(map(sqr,list1))
print("thw square of the list is ",b)