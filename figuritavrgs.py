import turtle


ventana = turtle.Screen()
ventana.bgcolor("black")
ventana.title("Carrito")


carro = turtle.Turtle()
carro.color("cyan")
carro.pensize(4)
carro.speed(0)

# Posicon de inicio we 
carro.penup()
carro.goto(-150, -50)
carro.pendown()

# Base del carro pyton
carro.forward(200)
carro.left(90)
carro.forward(50)
carro.left(45)
carro.forward(50)
carro.left(45)
carro.forward(80)
carro.left(45)
carro.forward(50)
carro.left(45)
carro.forward(50)

# Llanta vergs
carro.penup()
carro.goto(-100, -50)
carro.pendown()
carro.circle(30)

# Llanta vrgas 2
carro.penup()
carro.goto(50, -50)
carro.pendown()
carro.circle(30)

# Ventana del carro vergs
carro.penup()
carro.goto(-20, 20)
carro.pendown()
carro.left(90)
carro.forward(40)
carro.right(90)
carro.forward(50)
carro.right(90)
carro.forward(40)

turtle.done()
