import turtle
turtle.Screen().bgcolor('blue')
turtle.Screen().setup(600,500)
p=turtle.Turtle()
p.color('black')
p.pensize(5)
p.shape('turtle')
n=4
for i in range(n):
    p.forward(100)
    p.right(360/n)

turtle.done()