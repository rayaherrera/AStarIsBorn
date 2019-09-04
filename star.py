import turtle
turtle.color("deep pink")
turtle.speed(25)
def star(sidelength):
    for i in range (5):
        turtle.forward(sidelength)
        turtle.right(144)
star(190)
turtle.forward(90)
turtle.right(144)
def starspiral():
    for i in range(60):
        star()
turtle.exitonclick()