import turtle
import math

t = turtle.Turtle()
t.pensize(2)
t.speed(0)

#calcular nuevas coordenadas después de la rotación
def rotate_point(x, y, angle):
    angle = math.radians(angle)
    new_x = x * math.cos(angle) - y * math.sin(angle)
    new_y = x * math.sin(angle) + y * math.cos(angle)
    return new_x, new_y

def draw(lado):
    for i in range (4):
        t.forward(lado)
        t.left(90)

    ancho = lado / 4

    for i in range (4):
        if i == 0:
            t.forward(ancho)
    
        t.left(90)
        t.forward(lado)

        t.left(90)
        t.forward(ancho)

        if i < 3:
            t.left(90)
            t.forward(ancho)


# dibujar la siguiente figura en la misma posicion
def draw_rotated_square(t, angle, lado):
    t.penup()
    new_x, new_y = rotate_point(-100, -100, angle)  # (Posicion inicial en x, posicion inicial en y, angulo a girar)
    t.goto(new_x, new_y)
    t.setheading(angle)
    t.pendown()

    draw(lado)

#parametros
lado = 200 #estatico si lo mueve la caga
incremento_angulo = 18
cantidad_figuras = 5

# Dibujar figura
for i in range(cantidad_figuras):
    draw_rotated_square(t, i * incremento_angulo, lado)

turtle.done()
