import turtle

ventana = turtle.Screen()
ventana.bgcolor("black")
lineas = turtle.Turtle()

# llevando la linea hacia la izquierda
lineas.color("black")
lineas.left(1000)
lineas.forward(1000)
lineas.right(90)
lineas.forward(420)
lineas.right(90)

lineas.color("red")
for i in range(10):
    lineas.forward(100)
    lineas.right(90)
    lineas.forward(850)
    lineas.left(90)
    lineas.forward(100)
    lineas.left(90)
    lineas.forward(850)
    lineas.right(90)
turtle.done()
