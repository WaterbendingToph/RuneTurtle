import turtle
window = turtle.Screen()
window.setup(width = 500, height=500)

letterHeight = 250

triangleLength = ( (4 / 3) * ( (letterHeight / 2) ** 2) ) ** (0.5)

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

turtle.goto(0, 125)
turtle.pendown()

#START
triangleLength = ( (4 / 3) * ( (letterHeight / 2) ** 2) ) ** (0.5)
turtle.setheading(150)
turtle.forward(triangleLength)
turtle.setheading(270)
turtle.forward(triangleLength / 2)
verticalStartingPoint = turtle.position()
turtle.forward(triangleLength / 2)
turtle.setheading(30)
turtle.forward(triangleLength)
turtle.penup()
turtle.goto(verticalStartingPoint)
turtle.pendown()
turtle.setheading(180)
turtle.forward(letterHeight / 4)
turtle.setheading(90)
turtle.forward(letterHeight / 4)
turtle.setheading(270)
turtle.forward(letterHeight / 2)
turtle.setheading(90)
turtle.forward(letterHeight / 4)
turtle.setheading(180)
turtle.forward(letterHeight / 4)
#END

turtle.done()