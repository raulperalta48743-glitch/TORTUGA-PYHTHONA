import turtle

ventana = turtle.Screen()
ventana.bgcolor("black")
tortuga = turtle.Turtle()
tortuga.width(10)
tortuga.speed(1000)
tortuga.hideturtle()
tortuga.pencolor("red")
circulos = 7500000000000000000

for i in range(circulos):
    tortuga.circle(i * 2)
    tortuga.right(10)
turtle.done()
