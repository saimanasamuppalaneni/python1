# array operations
import array as arr
s1 = arr.array("i",[2,3,4,1,2,8,6,7,5,5,8,8,45,65,78,34])
print(str(s1))
print(f"the element 8 occurs {s1.count(8)} times in the array")
s1.reverse()
print("the reverse ",s1)