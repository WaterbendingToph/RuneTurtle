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
turtle.circle(int(letterHeight / 3), 180, int(letterHeight / 2) )
turtle.penup()
turtle.setheading(270)
turtle.forward(letterHeight / 3)
turtle.setheading(180)
turtle.forward(letterHeight / 3)
turtle.pendown()
turtle.setheading(90)
turtle.circle(int(-letterHeight / 6), 360, int(letterHeight / 2) )
turtle.penup()
turtle.setheading(180)
turtle.forward(letterHeight / 3)
turtle.pendown()
turtle.setheading(180)
turtle.forward(letterHeight / 6)
turtle.setheading(90)
turtle.forward(letterHeight / 6)
turtle.setheading(270)
turtle.forward(letterHeight / 3)
turtle.setheading(90)
turtle.forward(letterHeight / 6)
turtle.setheading(180)
turtle.forward(letterHeight / 6)
#END

turtle.done()