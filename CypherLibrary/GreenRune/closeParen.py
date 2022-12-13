import turtle
window = turtle.Screen()
window.setup(width = 500, height=500)

letterHeight = 250

diagonalLength = ( ( ( (2 / 3) * letterHeight) ** 2) * 2) ** (0.5)

turtle.mode("logo")
turtle.penup()
turtle.goto(125, -125)
turtle.pendown()

#START
turtle.setheading(180)
turtle.circle(int(-letterHeight / 4), 145, int(letterHeight / 4) )
turtle.setheading(330)
turtle.forward(diagonalLength / 2)
horizonatalStartingPoint = turtle.position()
turtle.forward(diagonalLength / 2)
turtle.circle(int(letterHeight / 4), 145, int(letterHeight / 4) )
turtle.penup()
turtle.goto(horizonatalStartingPoint)
turtle.setheading(90)
turtle.forward(letterHeight / 4)
turtle.pendown()
turtle.setheading(270)
turtle.forward(letterHeight / 2)
#END

turtle.done()