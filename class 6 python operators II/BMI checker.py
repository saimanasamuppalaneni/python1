# BMI checker
weight=float(input("enter your weight in KG"))
height=float(input("enter your height in meters"))
BMI=weight/(height)**2
print("your BMI is",round (BMI,2))
if BMI<18.5:
    print("you are under weight")
elif BMI<25:
    print("you are healthy")
elif BMI<30:
    print("you are over weight")
else:
    print("you are obese")