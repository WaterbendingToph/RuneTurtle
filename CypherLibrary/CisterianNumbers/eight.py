import turtle 
window = turtle.Screen()
window.setup(width=400, height=400)

height = 150
width = 50
digit = 1

turtle.mode("logo")
turtle.penup()
turtle.goto(0, -100)
turtle.pendown()
turtle.setheading(0)
turtle.forward(height)
turtle.penup()
if (digit == 1) | (digit == 10):
    turtle.setheading(180)
else:
    turtle.goto(0, -100)
    turtle.setheading(0)
turtle.forward(width)


#START
turtle.pendown()
if (digit == 1) | (digit == 100):
    turtle.setheading(90)
else:
    turtle.setheading(270)
turtle.forward(width)
if (digit == 1) | (digit == 10):
    turtle.setheading(0)
else:
    turtle.setheading(180)
turtle.forward(width)
#END


turtle.done()