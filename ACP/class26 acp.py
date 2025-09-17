# area and circumference
class iostring:
    def __init__(self,r):
        self.r = r
    
    def area(self):
        a = 3.14 * self.r *self.r
        print("the area of the cicle is ",a)
    
    def circumference(self):
        c = 2 * 3.14 * self.r 
        print("the perimeter of the circle is ",c)

s1 = iostring(8)
s1.area()
s1.circumference()