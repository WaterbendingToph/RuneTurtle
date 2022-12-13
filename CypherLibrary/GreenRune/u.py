import turtle
window = turtle.Screen()
window.setup(width = 500, height=500)

letterHeight = 250

turtle.mode("logo")
turtle.penup()
turtle.goto(-125, 125)
turtle.pendown()

#START
startingPoint = turtle.position()
turtle.setheading(45)
turtle.circle(int(-letterHeight * (3 / 5) ), 270, int(letterHeight / 4) )
turtle.penup()
turtle.goto(startingPoint)
turtle.pendown()
turtle.setheading(37)
turtle.circle(int(-letterHeight * (7 / 10) ), 285, int(letterHeight / 4) )
#END

turtle.done()