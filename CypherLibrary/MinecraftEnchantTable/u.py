import turtle
window = turtle.Screen()
window.setup(width = 200, height = 200)

length =        20
bottomLeft =    -50, -50
bottomRight =   50, -50
topLeft =       -50, 50
topRight =      50, 50

turtle.mode("logo")
turtle.pencolor("red")
turtle.penup()
turtle.goto(-100, -50)
turtle.pendown()
turtle.setheading(90)
turtle.forward(200)
turtle.penup()
turtle.goto(-50, -100)
turtle.pendown()
turtle.setheading(0)
turtle.forward(200)
turtle.penup()
turtle.goto(-100, 50)
turtle.pendown()
turtle.setheading(90)
turtle.forward(200)
turtle.penup()
turtle.goto(50, 100)
turtle.pendown()
turtle.setheading(180)
turtle.forward(200)

turtle.penup()
turtle.pencolor("blue")
turtle.goto(-50, -30)
turtle.pendown()
turtle.setheading(90)
turtle.forward(100)
turtle.penup()
turtle.goto(50, -10)
turtle.pendown()
turtle.setheading(270)
turtle.forward(100)
turtle.penup()
turtle.goto(-50, 10)
turtle.pendown()
turtle.setheading(90)
turtle.forward(100)
turtle.penup()
turtle.goto(50, 30)
turtle.pendown()
turtle.setheading(270)
turtle.forward(100)

turtle.penup()
turtle.goto(-30, 50)
turtle.pendown()
turtle.setheading(180)
turtle.forward(100)
turtle.penup()
turtle.goto(-10, -50)
turtle.pendown()
turtle.setheading(0)
turtle.forward(100)
turtle.penup()
turtle.goto(10, 50)
turtle.pendown()
turtle.setheading(180)
turtle.forward(100)
turtle.penup()
turtle.goto(30, -50)
turtle.pendown()
turtle.setheading(0)
turtle.forward(100)
turtle.penup()
turtle.pencolor("black")

#START




#END

turtle.done()