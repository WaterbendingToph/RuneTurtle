import turtle
window = turtle.Screen()
window.setup(width = 500, height=500)

letterHeight = 250

turtle.mode("logo")
turtle.penup()
turtle.goto(125, 125)
turtle.pendown()

#START
turtle.setheading(180)
turtle.forward(letterHeight / 4)
turtle.setheading(287)
turtle.circle(int(letterHeight / 2), int(360 * (3/5) ), int(letterHeight / 2) )

#END

turtle.done()