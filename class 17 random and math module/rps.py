# rock,paper,scissors
import random
list1 = ['rock','paper','scissors']
while True:
    c = random.choice(list1)
    u = (input("enter your choice :- rock , paper , scissors =  ")).lower()
    if c == u:
        print("it's a tie!!!")
        print(c)
    elif (u == 'rock'and c == 'scissors')or(u == 'paper'and c == 'rock')or(u == 'scissors'and c== 'paper'):
        print ("you win the game!!!")
        print (c)
    else:
        print("computer win the game ")
        print(c)
    ch = input("do you want to play again???(y/n)")
    if ch == 'n':
        break