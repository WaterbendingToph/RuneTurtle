import turtle 
window = turtle.Screen()
window.setup(width=400, height=400)

height = 150
width = 50
diagonal = 71
digit = 1

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
if (digit == 1) | (digit == 100):
    turtle.setheading(90)
else:
    turtle.setheading(270)
turtle.forward(width)
if digit == 1:
    turtle.setheading(225)
elif digit == 10:
    turtle.setheading(135)
elif digit == 100:
    turtle.setheading(315)
else:
    turtle.setheading(45)
turtle.forward(diagonal)
#END


turtle.done()