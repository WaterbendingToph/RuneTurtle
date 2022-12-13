import turtle
window = turtle.Screen()
window.setup(width = 500, height=500)

letterHeight = 250

turtle.mode("logo")
turtle.penup()
turtle.goto(-125, 125)
turtle.pendown()

#START
turtle.setheading(0)
turtle.circle(int(-letterHeight / 8), 180, int(letterHeight / 8) )
turtle.setheading(180)
turtle.forward( (2 / 6) * letterHeight)
turtle.setheading(90)
turtle.forward( (2 / 6) * letterHeight)
turtle.setheading(0)
turtle.forward( (letterHeight / 2) )
turtle.setheading(180)
turtle.forward(letterHeight)
#END

turtle.done()