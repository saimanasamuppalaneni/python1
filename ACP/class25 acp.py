# dog breed
class dog:
    species = "dog"
    def __init__(self,name,age):
        self.name = name 
        self.age = age
d1 = dog("german shepherd",2)
d2 = dog("american eskimo dog",3)
print("the breed of the 1st",dog.species)
print(f"my name is {d1.name}and i am {d1.age}years old")
print("the breed of the 2nd",dog.species)
print(f"my name is {d2.name}and i am {d2.age}years old")