import turtle 
window = turtle.Screen()
window.setup(width=400, height=400)

height = 150
width = 50
digit = 1000

turtle.mode("logo")
turtle.penup()
turtle.goto(0, -100)
turtle.pendown()
turtle.setheading(0)
turtle.forward(height)
if (digit == 100) | (digit == 1000):
    turtle.penup()
    turtle.goto(0, -100)


#START
turtle.pendown()
if (digit == 1) | (digit == 100):
    turtle.setheading(90)
else:
    turtle.setheading(270)
turtle.forward(width)
if (digit == 1) | (digit == 10):
    turtle.setheading(180)
else:
    turtle.setheading(0)
turtle.forward(width)
if (digit == 1) | (digit == 100):
    turtle.setheading(270)
else:
    turtle.setheading(90)
turtle.forward(width)
#END


turtle.done()