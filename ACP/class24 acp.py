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
