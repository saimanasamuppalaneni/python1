# flip flop
def flip_flop(tup1):
    l = len(tup1)
    s = 0
    e = l-1
    while s < e:
        if tup1[s] != tup1[e]:
            return False
        s += 1
        e -= 1
    return True

tup1 = (1,47,2,47,1)
res = flip_flop(tup1)
if res :
    print("the given tuple is a paindrome")
else:
    print("the given tuple is not a palindrome")