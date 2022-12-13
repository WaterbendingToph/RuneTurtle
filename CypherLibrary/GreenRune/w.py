import turtle
window = turtle.Screen()
window.setup(width = 500, height=500)

letterHeight = 250

turtle.mode("logo")
turtle.penup()
turtle.goto(0, 125)
turtle.pendown()

#START
turtle.setheading(90)
turtle.circle(-letterHeight / 2, 360, letterHeight)
turtle.setheading(180)
turtle.penup()
turtle.forward(letterHeight / 2)
turtle.setheading(135)
turtle.forward(int(letterHeight * (3 / 8) ) )
turtle.pendown()
turtle.forward(letterHeight / 4)
#END

turtle.done()