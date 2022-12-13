import turtle
window = turtle.Screen()
window.setup(width = 500, height=500)

letterHeight = 250

diagonalLength = ( (letterHeight) ** 2 + ( ( (3 / 8) * letterHeight) ** 2) ) ** (0.5)

turtle.mode("logo")
turtle.penup()
turtle.goto(-125, 125)
turtle.pendown()

#START
turtle.setheading(90)
turtle.forward(letterHeight / 4)
turtle.setheading(270)
turtle.forward(letterHeight / 8)
turtle.setheading(150)
turtle.forward(diagonalLength)
turtle.setheading(30)
turtle.forward(diagonalLength)
turtle.setheading(90)
turtle.forward(letterHeight / 8)
turtle.setheading(270)
turtle.forward(letterHeight / 4)
#END

turtle.done()