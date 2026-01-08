import turtle
import random
turtle.Screen().bgcolor('black')
turtle.Screen().setup(600.500)
turtle.Screen().title('Random Pattern')
p=turtle.Turtle()
p.pensize(2)
size=0
colors=['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'pink', 'brown', 'white', 'grey']
while True:
    p.color(random.choice(colors))
    for i in range(4):
        p.forward(size+1)
        p.left(90)
        size=size-5
    size+=1