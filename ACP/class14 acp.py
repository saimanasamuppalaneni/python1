# shutdown
import os
s = input("do you wish to shutdown our computer ? (yes/no)  :  ")
if s == 'no':
    exit()
else:
    os.system("shutdown/s/t1")