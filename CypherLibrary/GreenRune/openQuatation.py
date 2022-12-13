import turtle
window = turtle.Screen()
window.setup(width = 500, height=500)

letterHeight = 250

turtle.mode("logo")
turtle.penup()
turtle.goto(0, -125)
turtle.pendown()

#START
turtle.setheading(270)
turtle.circle(-letterHeight / 2, 180, 2)
#END

turtle.done()