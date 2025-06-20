# profit or loss
cp=float(input("enter the cost price"))
sp=float(input("enterr the selling price"))
if sp>cp:
    print(f"you have a profit of {sp-cp}")
else:
    print(f"you have a loss of {cp-sp}")
