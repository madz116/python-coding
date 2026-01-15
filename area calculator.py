def trianglearea(base,height):
    area=(base*height)/2
    return area

def squarearea(side):
    area=side**2
    return area

def rectanglearea(length,width):
    area=length*width
    return area

def circlearea(radius):
    area=3.14*radius**2
    return area

print("----------Area Calculator----------")
print("1. Triangle")
print("2. Square")
print("3. Rectangle")
print("4. Circle")
print("-----------------------------------")

choice=input("Enter which shape you want to find the area of.")

if choice=="1":
    b=float(input("Enter the base of the triangle: "))
    h=float(input("Enter the height of the triangle: "))
    print("The area of the triangle is: ",trianglearea(b,h))
elif choice=="2":
    s=float(input("Enter the side of the square: "))
    print("The area of the square is: ",squarearea(s))
elif choice=="3":
    l=float(input("Enter the length of the rectangle: "))
    h=float(input("Enter the height of the rectangle: "))
    print("The area of the rectangle is: ",rectanglearea(l,h))
elif choice=="4":
    r=float(input("Enter the radius of the circle: "))
    print("The area of the circle is: ",circlearea(r))
else:
    print("Invalid input.")