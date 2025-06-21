# BMI checker
weight=float(input("enter your weight"))
height=float(input("enter your height in meters"))
BMI=weight/(height)**2
if BMI<18.5:
    print("you are under weight")
elif BMI<25:
    print("you are healthy")
elif BMI<30:
    print("you are over weight")
else:
    print("you are obese")