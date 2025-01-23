import turtle
window = turtle.Screen()
window.setup(width = 500, height=500)

letterHeight = 250

diagonalLength = ( ( (letterHeight / 2) ** 2) * 2) ** (0.5)

turtle.mode("logo")
turtle.penup()
turtle.pencolor("red")
turtle.goto(-250, 125)
turtle.pendown()
turtle.setheading(90)
turtle.forward(500)
turtle.penup()
turtle.goto(-250, -125)
turtle.pendown()
turtle.setheading(90)
turtle.forward(500)
turtle.pencolor("black")
turtle.penup()

turtle.goto(125, 125)
turtle.pendown()

#START
diagonalLength = ( ( (letterHeight / 2) ** 2) * 2) ** (0.5)
turtle.setheading(0)
turtle.penup()
turtle.backward(letterHeight / 4)
turtle.pendown()
turtle.forward(letterHeight / 4)
turtle.setheading(270)
turtle.forward(letterHeight)
turtle.setheading(135)
turtle.forward(diagonalLength)
turtle.setheading(225)
turtle.forward(diagonalLength)
turtle.setheading(90)
turtle.forward(letterHeight)
turtle.setheading(0)
turtle.forward(letterHeight / 4)
#END

turtle.done()