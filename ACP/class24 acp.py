# random password
import random

def shuffle(string):
    tempList = list(string)
    random.shuffle(tempList)
    return ''.join(tempList)
uppercaseletter1 = chr(random.randint(65,90))
uppercaseletter2 = chr(random.randint(65,90))
lowercaseletter1 = chr(random.randint(91,116))
lowercaseletter2 = chr(random.randint(91,116))
number1 = random.randint(0,9)
number2 = random.randint(0,9)
password = uppercaseletter1 + uppercaseletter2 + lowercaseletter1 + lowercaseletter2 + str(number1) + str(number2)
passsword = shuffle(password)
print(password)