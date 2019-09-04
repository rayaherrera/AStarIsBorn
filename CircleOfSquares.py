import turtle
turtle.bgcolor("black")
turtle.color("green")
turtle.speed(50)
def square(sidelength):
    for i in range(4):
        turtle.forward(sidelength)
        turtle.right(90)





for i in range(60):
    square(100)
    turtle.right(5)



turtle.exitonclick()