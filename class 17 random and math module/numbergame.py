# number game
import random
c=random.randint(1,10)
a=0
while True:
    a+=1
    n=int(input("enter the number between 1 - 10"))
    if c == n:
        print("you gussed it right .attempt = ",a)
        break
    else:
        print("try again")