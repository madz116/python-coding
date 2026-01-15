def triangleperi(a,b,c):
    perimeter=a+b+c
    return perimeter

def squareperi(side):
    perimeter=side*4
    return perimeter

def rectangleperi(length,width):
    perimeter=2*(l+h)
    return perimeter

def circlecirc(radius):
    circumference=3.14*radius*2
    return circumference

print("----------Perimeter Calculator----------")
print("1. Triangle")
print("2. Square")
print("3. Rectangle")
print("4. Circle")
print("---------------------------------------")

choice=input("Enter which shape you want to find the perimeter of.")

if choice=="1":
    a=float(input("Enter the first side of the triangle: "))
    b=float(input("Enter the second side of the triangle: "))
    c=float(input("Enter the third side of the triangle: "))
    print("The perimeter of the triangle is: ",triangleperi(a,b,c))
elif choice=="2":
    s=float(input("Enter the side of the square: "))
    print("The perimeter of the square is: ",squareperi(s))
elif choice=="3":
    l=float(input("Enter the length of the rectangle: "))
    h=float(input("Enter the height of the rectangle: "))
    print("The perimeter of the rectangle is: ",rectangleperi(l,h))
elif choice=="4":
    r=float(input("Enter the radius of the circle: "))
    print("The circumference of the circle is: ",circlecirc(r))
else:
    print("Invalid input.")