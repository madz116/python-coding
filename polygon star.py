import turtle
turtle.Screen().bgcolor('green')
turtle.Screen().setup(600,500)
turtle.Screen().title('Star')
p=turtle.Turtle()
p.color('white')
p.pensize(5)
p.shape('classic')
p.penup()
p.goto(-80,70)
p.pendown()
for i in range(5):
    p.forward(200)
    p.right(144)

turtle.done()