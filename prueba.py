import turtle
import math

# Inicializar Turtle y configurar la pantalla
screen = turtle.Screen()
screen.setup(width=800, height=600)  # Ajustar las dimensiones de la pantalla según sea necesario

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

# Calcular nuevas coordenadas después de la rotación
def rotate_point(x, y, angle):
    angle = math.radians(angle)
    new_x = x * math.cos(angle) - y * math.sin(angle)
    new_y = x * math.sin(angle) + y * math.cos(angle)
    return new_x, new_y

def draw_rotated_square(t, angle, lado, x, y):
    t.penup()
    new_x, new_y = rotate_point(x, y, angle)  # (Posicion inicial en x, posicion inicial en y, angulo a girar)
    t.goto(new_x, new_y)
    t.setheading(angle)
    t.pendown()

    draw(lado)

# Parámetros
lado = 200
incremento_angulo = 60
cant_figuras = 3
counter = 0;

# Obtener dimensiones de la pantalla
window_width = screen.window_width()
window_height = screen.window_height()

# Calcular el número de pasos necesario para cubrir toda la pantalla
num_steps_x = window_width
num_steps_y = window_height 

# Coordenadas
x = -(window_width / 2 - 5)
y = window_height / 2 - 5
t.penup()

for i in range(int(num_steps_x)):
    for j in range(int(num_steps_y / 10)):
        for k in range(cant_figuras):
            draw_rotated_square(t, k * incremento_angulo, lado, x, y)
        print(y)
        y -= 10
    y = window_height / 2 - 5
    x += 10

turtle.done()
