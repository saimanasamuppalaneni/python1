# sum and average
a = [34,46,67,89,25,98,54]
sum = 0
for i in a:
    sum = sum + i
print("the given list is \n",a)
print("the average of the list is ",round(sum/len(a),2))
print("the maximum in the list is ",max(a))
print("the minimum in the list is ",min(a))