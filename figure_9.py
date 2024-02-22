import turtle
import math

t = turtle.Turtle()

t.pensize(2)
t.speed(0)

def draw(lado, type):
    ancho = lado
    alto = (lado / 2) + 25

    ancho_test = lado / 4 - 20
    ancho_test_mini = ancho_test / 2
    
    if type == "center":
        for i in range (4):
            if i % 2 == 0:
                t.forward(ancho)
                t.left(90)
            else:
                t.forward(alto)
                t.left(90)
        
        t.forward(ancho_test)

        t.left(90)
        t.forward(alto)

        t.left(90)
        t.forward(ancho_test)

        t.left(90)
        t.forward(ancho_test_mini)

        t.left(90)
        t.forward(ancho)

        t.left(90)
        t.forward(ancho_test_mini)

        t.left(90)
        t.forward(ancho_test)

        t.left(90)
        t.forward(alto)

        t.left(90)
        t.forward(ancho_test)

        t.left(90)
        t.forward(ancho_test_mini)

        t.left(90)
        t.forward(ancho)

        t.left(90)
        t.forward(ancho_test_mini)
    
    if type == "right":
        for i in range(4):
            if i % 2 == 0:
                t.forward(ancho)
                t.right(90)
            else:
                t.forward(alto)
                t.right(90)

        t.forward(ancho_test)

        t.right(90)
        t.forward(alto)

        t.right(90)
        t.forward(ancho_test)

        t.right(90)
        t.forward(ancho_test_mini)

        t.right(90)
        t.forward(ancho)

        t.right(90)
        t.forward(ancho_test_mini)

        t.right(90)
        t.forward(ancho_test)

        t.right(90)
        t.forward(alto)

        t.right(90)
        t.forward(ancho_test)

        t.right(90)
        t.forward(ancho_test_mini)

        t.right(90)
        t.forward(ancho)

        t.right(90)
        t.forward(ancho_test_mini)

    if type == "left":
        for i in range(4):
            if i % 2 == 0:
                t.forward(ancho)
                t.left(90)
            else:
                t.forward(alto)
                t.left(90)

        t.forward(ancho_test)

        t.left(90)
        t.forward(alto)

        t.left(90)
        t.forward(ancho_test)

        t.left(90)
        t.forward(ancho_test_mini)

        t.left(90)
        t.forward(ancho)

        t.left(90)
        t.forward(ancho_test_mini)

        t.left(90)
        t.forward(ancho_test)

        t.left(90)
        t.forward(alto)

        t.left(90)
        t.forward(ancho_test)

        t.left(90)
        t.forward(ancho_test_mini)

        t.left(90)
        t.forward(ancho)

        t.left(90)
        t.forward(ancho_test_mini)

#parametros
lado = 266 #estatico si lo mueve la caga
incremento_angulo = 18

t.pensize(4)
draw(lado, "center")

t.left(90)

t.penup()
t.goto(-6, 6)

t.left(58)
t.pendown()

draw(lado, "right")

t.left(90)

t.penup()
t.goto(0, 0)

t.left(122)
t.goto(lado + 6, 6)

t.left(90+32)
t.pendown()

draw(lado, "left")

turtle.done()
