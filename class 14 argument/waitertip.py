# waiter tip
def tip(amount,percentage=10):
    tamt=(amount*percentage/100)+amount
    tamt=round(tamt,2)
    print("the tip you have to give to the waiter is",tamt)

tip(500)
tip(700,20)    