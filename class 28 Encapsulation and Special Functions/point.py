# point function
class point:
    def __init__(self,x = 0,y = 0):
         self.x = x
         self.y = y

    def __str__(self):
         return f"({self.x},{self.y})"

p1 = point(20,40)
print(p1)