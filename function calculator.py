def calculator(choice,a,b):
    if choice==1:
        return a+b
    elif choice==2:
        return a-b
    elif choice==3:
        return a*b
    elif choice==4:
        if b==0:
            return "Error. Division by 0 is not allowed."
        return a/b
    else:
        return "Invalid choice."
    
print("----------Calculator----------")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("------------------------------")
choice=int(input("Enter which operation you want to choose. (1, 2, 3, 4)"))
a=float(input("Enter the first number: "))
b=float(input("Enter the second number: "))
result=calculator(choice,a,b)
print(f"The result: {result}")