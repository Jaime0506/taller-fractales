import turtle
import math

t = turtle.Turtle()
t.pensize(2)
t.pendown()
# t.speed(1)

#calcular nuevas coordenadas después de la rotación
def rotate_point(x, y, angle):
    angle = math.radians(angle)
    new_x = x * math.cos(angle) - y * math.sin(angle)
    new_y = x * math.sin(angle) + y * math.cos(angle)
    return new_x, new_y

# dibujar la siguiente figura en la misma posicion
def draw_rotated_square(base,alto, type):

    base_chiquito = base / 4
    alto_chiquito = alto / 3

    if type == "center":

        t.pensize(4)

        for i in range(2):
            if i % 2 == 0:
                t.forward(base)
                t.left(90)

                t.forward(alto)
                t.left(90)

            else:
                t.forward(base)
                t.left(90)

                t.forward(alto)
                t.left(90)
            
        t.pensize(2)

        t.forward(base_chiquito)
        t.left(90)

        t.forward(alto)
        t.left(90)

        t.forward(base_chiquito)
        t.left(90)

        t.forward(alto_chiquito)
        t.left(90)

        t.forward(base)
        t.left(90)

        t.forward(alto_chiquito)
        t.left(90)

        t.forward(base_chiquito)
        t.left(90)

        t.forward(alto)
        t.left(90)

        t.forward(base_chiquito)
        t.left(90)

        t.forward(alto_chiquito)
        t.left(90)

        t.forward(base)
        t.left(90)

        t.forward(alto_chiquito)
        t.left(90)
    
    if type == "right":

        t.pensize(4)

        for i in range(2):
            if i % 2 == 0:
                t.forward(base)
                t.right(90)

                t.forward(alto)
                t.right(90)

            else:
                t.forward(base)
                t.right(90)

                t.forward(alto)
                t.right(90)

        t.pensize(2)

        t.forward(base_chiquito)
        t.right(90)

        t.forward(alto)
        t.right(90)

        t.forward(base_chiquito)
        t.right(90)

        t.forward(alto_chiquito)
        t.right(90)

        t.forward(base)
        t.right(90)

        t.forward(alto_chiquito)
        t.right(90)

        t.forward(base_chiquito)
        t.right(90)

        t.forward(alto)
        t.right(90)

        t.forward(base_chiquito)
        t.right(90)

        t.forward(alto_chiquito)
        t.right(90)

        t.forward(base)
        t.right(90)

        t.forward(alto_chiquito)
        t.right(90)


#parametros
base = 200
alto = 113 #estatico si lo mueve la caga

incremento_angulo = 60
cantidad_figuras = 3

t.speed(0)

draw_rotated_square(base, alto, "center")

t.left(60)

draw_rotated_square(base, alto, "right")

t.right(60)

t.forward(base)

t.left(90 + 30)

draw_rotated_square(base, alto, "center")

turtle.done()
    
# lado1 = 185
# lado2 = 120