class computer:
    def __init__(self):
        self.__price = 900
    def disp(self):
        print("the computer price is ",self.__price)
    def setprice(self,p):
        self.__price = p

c1 = computer()
c1.disp()
c1.__price = 1000
c1.disp()
c1.setprice(1000)
c1.disp()