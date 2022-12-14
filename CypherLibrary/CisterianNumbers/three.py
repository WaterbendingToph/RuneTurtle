import turtle 
window = turtle.Screen()
window.setup(width=400, height=400)

height = 150
diagonal = 71
digit = 1

turtle.mode("logo")
turtle.penup()
turtle.pencolor("red")
turtle.goto(-200, 50)
turtle.pendown()
turtle.setheading(90)
turtle.forward(400)
turtle.penup()
turtle.goto(-200, -100)
turtle.pendown()
turtle.setheading(90)
turtle.forward(400)
turtle.penup()
turtle.pencolor("black")

turtle.goto(0, -100)
turtle.pendown()
turtle.setheading(0)
turtle.forward(height)
if (digit == 100) | (digit == 1000):
    turtle.penup()
    turtle.goto(0, -100)


#START
turtle.pendown()
if digit == 1:
    turtle.setheading(135)
elif digit == 10:
    turtle.setheading(225)
elif digit == 100:
    turtle.setheading(45)
elif digit == 1000:
    turtle.setheading(315)
turtle.forward(diagonal)
#END


turtle.done()