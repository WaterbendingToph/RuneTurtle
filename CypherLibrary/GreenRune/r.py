import turtle
window = turtle.Screen()
window.setup(width = 500, height=500)

letterHeight = 250

turtle.mode("logo")
turtle.penup()
turtle.goto(-125, -125)
turtle.pendown()

#START
turtle.setheading(180)
turtle.circle(int(letterHeight / 12), 180, int(letterHeight / 6) )
turtle.setheading(0)
turtle.forward( (5 / 6) * letterHeight)
turtle.setheading(90)
turtle.forward( (5 / 6) * letterHeight)
turtle.setheading(180)
turtle.forward( (5 / 6) * letterHeight)
turtle.circle(int(letterHeight / 12), 180, int(letterHeight / 6) )
#END

turtle.done()