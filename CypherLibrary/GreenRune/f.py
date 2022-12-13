import turtle
window = turtle.Screen()
window.setup(width = 500, height=500)

letterHeight = 250

turtle.mode("logo")
turtle.penup()
turtle.goto(-125, 125)
turtle.pendown()

#START
turtle.setheading(90)
turtle.circle(letterHeight * 3, 5, int(letterHeight / 10) )
verticalStartingPoint = turtle.position()
turtle.setheading(90)
turtle.circle(-letterHeight / 6, 180, int(letterHeight / 4) )
turtle.penup()
turtle.goto(verticalStartingPoint)
turtle.pendown()
turtle.setheading(180)
turtle.forward(letterHeight)
#END

turtle.done()