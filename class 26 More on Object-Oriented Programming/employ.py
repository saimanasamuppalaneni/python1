# employ in out
class employee:
    def __init__(self):
        print("employ created")
    def __del__(self):
        print("employee deleted")
e1 = employee()
e2 = employee()
del (e1);
print("this the end of the program")