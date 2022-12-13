import turtle
window = turtle.Screen()
window.setup(width = 500, height=500)

letterHeight = 250

turtle.mode("logo")
turtle.penup()
turtle.goto(-125, 125)
turtle.pendown()

#START
turtle.setheading(180)
turtle.forward(letterHeight / 4)
turtle.setheading(0)
turtle.forward(letterHeight / 8)
turtle.setheading(90)
turtle.forward(letterHeight * (7/8) )
turtle.setheading(225)
turtle.forward( (2 * ( ( (7 / 8) * letterHeight) ** 2) ) ** (0.5) )
turtle.setheading(90)
turtle.forward(letterHeight * (7/8) )
turtle.setheading(0)
turtle.forward(letterHeight / 8)
turtle.setheading(180)
turtle.forward(letterHeight / 4)
#END

turtle.done()