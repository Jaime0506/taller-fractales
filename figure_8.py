import turtle
import math

screen = turtle.Screen()

width = screen.window_width()
height = screen.window_height()

print(width, height)

t = turtle.Turtle()
t.pensize(2)
t.speed(0)

def draw(lado):

    ancho_normal = lado * .4
    ancho_chiquito = lado * .2 

    for i in range(4):
        t.forward(lado)
        t.left(90)

    t.forward(ancho_normal)
    t.left(90)

    t.forward(lado)
    t.right(90)
    
    t.forward(ancho_chiquito)
    t.right(90)

    t.forward(lado)

    t.right(90)
    t.forward(lado * .60)

    t.right(180)

#calcular nuevas coordenadas después de la rotación
def rotate_point(x, y, angle):
    angle = math.radians(angle)
    new_x = x * math.cos(angle) - y * math.sin(angle)
    new_y = x * math.sin(angle) + y * math.cos(angle)
    return new_x, new_y

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
incremento_angulo = 60
cantidad_figuras = 3

# Dibujar figura
for i in range(cantidad_figuras):
    draw_rotated_square(t, i * incremento_angulo, lado)

turtle.done()
