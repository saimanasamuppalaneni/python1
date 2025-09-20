class myclass:
    __pvar = 100

    def __pri_meth(self):
        print("the value is ",myclass.__pvar)
    def pub(self):
        print("the value is ",myclass.__pvar)

obj1 = myclass()
obj1.pub()
obj1.__pri_meth()