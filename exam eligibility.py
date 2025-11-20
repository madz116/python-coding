reason=str(input("Do you have a medical reason? (yes/no): ")).lower()

if reason=="yes":
    att=int(input("Enter your attendance percentage: "))

    if att>=60:
        print("You are eligible for the exam.")
    else:
        print("You are not eligible for the exam.")
elif reason=="no":
    att=int(input("Enter your attendance percentage: "))

    if att>=75:
        print("You are eligible for the exam.")
    else:
        print("You are not eligible for the exam.")
else:
    print("Invalid answer.")