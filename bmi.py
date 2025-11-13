weight=float(input("Enter your weight in kg: "))
height=float(input("Enter your height in meters: "))

bmi=weight/height**2

print(f"Your bmi is: {bmi:0.2f} ")

if bmi<18.5:
    print("You are underweight.")
elif 18.5<=bmi<=24.9:
    print("You are at average weight.")
elif 25<=bmi<=29.9:
    print("You are overweight.")
elif 30<=bmi<=34.9:
    print("You are obese.")
else:
    print("You are extremely obese.")