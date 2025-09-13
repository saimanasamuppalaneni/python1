# upper case
class iostring:
    def __init__(self):
        self.str1 = ""
    def getstr (self):
        self.str1 = input("enter the phrase")
    def convert(self):
        print("the given string in upper case : ",self.str1.upper())
obj1 = iostring()
obj1.getstr()
obj1.convert()