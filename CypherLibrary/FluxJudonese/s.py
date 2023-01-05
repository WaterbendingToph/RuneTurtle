import turtle
window = turtle.Screen()
window.setup(width = 360, height = 360)

length =        40
topLeft =       -140,140
bottomLeft =    -140,-140
ReturnPoint =   0,0
direction = 1

turtle.speed(0)

turtle.mode("logo")
turtle.pencolor("red")
turtle.penup()
turtle.goto(-140, -180)
turtle.setheading(0)
turtle.pendown()
turtle.forward(360)

turtle.penup()
turtle.goto(-180, 140)
turtle.pendown()
turtle.setheading(90)
turtle.forward(360)

turtle.penup()
turtle.goto(140, 180)
turtle.pendown()
turtle.setheading(180)
turtle.forward(360)

turtle.penup()
turtle.goto(180, -140)
turtle.pendown()
turtle.setheading(270)
turtle.forward(360)

turtle.pencolor("blue")
turtle.penup()
turtle.goto(-100, -140)
turtle.pendown()
turtle.setheading(0)
turtle.forward(280)

turtle.penup()
turtle.goto(-60, 140)
turtle.pendown()
turtle.setheading(180)
turtle.forward(280)

turtle.penup()
turtle.goto(-20, -140)
turtle.pendown()
turtle.setheading(0)
turtle.forward(280)

turtle.penup()
turtle.goto(20, 140)
turtle.pendown()
turtle.setheading(180)
turtle.forward(280)

turtle.penup()
turtle.goto(60, -140)
turtle.pendown()
turtle.setheading(0)
turtle.forward(280)

turtle.penup()
turtle.goto(100, 140)
turtle.pendown()
turtle.setheading(180)
turtle.forward(280)

turtle.penup()
turtle.goto(140, -100)
turtle.pendown()
turtle.setheading(270)
turtle.forward(280)

turtle.penup()
turtle.goto(-140, -60)
turtle.pendown()
turtle.setheading(90)
turtle.forward(280)

turtle.penup()
turtle.goto(140, -20)
turtle.pendown()
turtle.setheading(270)
turtle.forward(280)

turtle.penup()
turtle.goto(-140, 20)
turtle.pendown()
turtle.setheading(90)
turtle.forward(280)

turtle.penup()
turtle.goto(140, 60)
turtle.pendown()
turtle.setheading(270)
turtle.forward(280)

turtle.penup()
turtle.goto(-140, 100)
turtle.pendown()
turtle.setheading(90)
turtle.forward(280)

#START

#END

turtle.done()