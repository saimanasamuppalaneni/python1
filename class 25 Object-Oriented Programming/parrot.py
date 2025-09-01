class parrot:
    species = "Maccaw"
    def __init__(self,name,age):
        self.name = name 
        self.age = age
p1 = parrot("jolly",2)
p2 = parrot("coo",3)
print("the spcies of the parrot 1 is",parrot.species)
print(f"my name is {p1.name}and i am {p1.age}years old")
print("the spcies of the parrot 2 is",parrot.species)
print(f"my name is {p2.name}and i am {p2.age}years old")