# super penguin
class bird:
    def __init__(self):
        print("the bird is created")
    def disp(self):
        print("the bird has wings")
class penguin(bird):
    def __init__(self):
        super().__init__()
        print("penguin is created")
    def displ1(self):
        print("penguin can run faster")
p1 = penguin()
p1.disp()
p1.displ1()