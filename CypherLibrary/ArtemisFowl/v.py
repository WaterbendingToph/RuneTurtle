import turtle
window = turtle.Screen()
window.setup(width = 600, height=600)

letterHeight = 400
lineWidth = 20
rightWall = 0
returnPoint = 0,0

turtle.mode("logo")
turtle.penup()
turtle.pencolor("red")
turtle.goto(-300, -250)
turtle.pendown()
turtle.setheading(90)
turtle.forward(600)
turtle.penup()
turtle.goto(250, -300)
turtle.pendown()
turtle.setheading(0)
turtle.forward(600)
turtle.penup()
turtle.goto(300, 250)
turtle.pendown()
turtle.setheading(270)
turtle.forward(600)
turtle.penup()
turtle.goto(-250, 300)
turtle.pendown()
turtle.setheading(180)
turtle.forward(600)
turtle.penup()
turtle.pencolor("blacK")

turtle.goto(0, -letterHeight / 2)
turtle.pendown()


#START
turtle.setheading(135)
turtle.circle(letterHeight / 4, -12)
turtle.circle(letterHeight / 4, 147)     #, 135)
rightWall = turtle.xcor()
turtle.circle(letterHeight / 4, 180)   # 135 makes it an even 270 all the way through the arc
turtle.circle(-letterHeight / 6, 270)
returnPoint = turtle.position()
turtle.circle(-letterHeight / 5, 63)                    #  turtle.circle(-letterHeight / 4, 48)

turtle.penup()
turtle.goto(returnPoint)
turtle.setheading(90)
turtle.forward(2 * (letterHeight / 6) + (letterHeight / 4 - letterHeight / 6) )
returnPoint = turtle.position()
turtle.pendown()
turtle.setheading(270)
turtle.circle(letterHeight / 6, 90)
turtle.circle(-letterHeight / 4, 328)

turtle.penup()
turtle.goto(returnPoint)
turtle.pendown()
turtle.setheading(90)
turtle.circle(-letterHeight / 6, 180)
turtle.circle(-letterHeight / 5, 61)
#END

turtle.penup()
turtle.goto(rightWall, -300)
turtle.pencolor("blue")
turtle.pendown()
turtle.setheading(0)
turtle.forward(600)
turtle.done()