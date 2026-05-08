import tkinter
import turtle

GIF = "dvd.gif"
PASO_X = 4
PASO_Y = 3

# Ventana
ventana = turtle.Screen()
ventana.bgcolor("black")
ventana.setup(width=800, height=500)
ventana.title("DVD Rebotando")

canvas = ventana.getcanvas()

# Cargar fotogramas del GIF
fotogramas = []
indice = 0

while True:
    try:
        fotograma = tkinter.PhotoImage(
            file=GIF,
            format=f"gif -index {indice}",
        )
        fotogramas.append(fotograma)
        indice += 1
    except tkinter.TclError:
        break

if len(fotogramas) == 0:
    raise FileNotFoundError(
        "Guarda un GIF llamado 'dvd.gif' en la misma carpeta."
    )

# Crear imagen
fotograma_actual = 0
x = 0
y = 0

personaje = canvas.create_image(x, y, image=fotogramas[fotograma_actual])

# Dirección
dx = PASO_X
dy = PASO_Y

# Límites de ventana
ANCHO = 400
ALTO = 250

def mover():
    global x, y, dx, dy, fotograma_actual

    # Mover posición
    x += dx
    y += dy

    # Rebotar horizontal
    if x > ANCHO or x < -ANCHO:
        dx *= -1

    # Rebotar vertical
    if y > ALTO or y < -ALTO:
        dy *= -1

    # Mover imagen
    canvas.coords(personaje, x, y)

    # Animar GIF
    fotograma_actual = (fotograma_actual + 1) % len(fotogramas)
    canvas.itemconfig(personaje, image=fotogramas[fotograma_actual])

    # Repetir
    ventana.ontimer(mover, 30)

# Iniciar movimiento
mover()

turtle.done()
