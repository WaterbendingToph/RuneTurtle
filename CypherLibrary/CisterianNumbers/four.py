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
turtle.penup()
if (digit == 1) | (digit == 10):
    turtle.setheading(180)
else:
    turtle.setheading(0)    
turtle.forward(width)
turtle.pendown()
if digit == 1:
    turtle.setheading(45)
elif digit == 10:
    turtle.setheading(315)
elif digit == 100:
    turtle.setheading(135)
else:
    turtle.setheading(225)
turtle.forward(diagonal)
#END


turtle.done()