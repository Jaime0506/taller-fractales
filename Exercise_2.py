import turtle

turtle.speed(0)
turtle.penup()
turtle.goto(0,-200)

turtle.left(90)
turtle.pendown()

def dibujo(tam, prof):
    if prof == 0:
        return
    else:
        turtle.forward(tam)
        turtle.left(45)
        dibujo(tam*2/3, prof-1)
        turtle.right(90)
        dibujo(tam*2/3, prof-1)
        turtle.left(45)
        turtle.back(tam)


dibujo(200, 12)
turtle.done()
