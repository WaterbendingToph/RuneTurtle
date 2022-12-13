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
turtle.forward(letterHeight)
#END

turtle.penup()
turtle.goto(-125, 100)
turtle.pendown()

#SINGULAR START
turtle.setheading(210)
turtle.circle(letterHeight / 2, steps=3)
turtle.setheading(180)
turtle.penup()
turtle.forward(letterHeight / 3)
turtle.pendown()
turtle.setheading(90)
turtle.forward( (letterHeight * (6/7) ) )
#SINGULAR END

turtle.done()