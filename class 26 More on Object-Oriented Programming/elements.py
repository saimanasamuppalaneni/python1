# pair of elements
class pairofelements:
    def twosum(self,tuple1,target):
        lookup = {}
        sum = 0
        for i,num in enumerate(tuple1):
            sum = sum + num
            if sum <= target:
                lookup[i] = sum
            else:
                print(lookup)
                print(f"the index number where we go the sum up to {target} is {i-1}")
                return
obj1 = pairofelements()
tuple1 = ( 10,20,30,40,50,60,70)
target = 220
obj1.twosum(tuple1,target)