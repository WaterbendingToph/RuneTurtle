import turtle
window = turtle.Screen()
window.setup(width = 600, height=600)

letterHeight = 400
lineWidth = 20
rightWall = 0
returnPoint = 0,0
returnPoint1 = 0,0

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
bottomRight = 0,0
headingBR = 0
bottomLeft = 0,0
headingBL = 0
rightBottom = 0,0
headingRB = 0
rightTop = 0,0
headingRT = 0
topRight = 0,0
headingTR = 0
topLeft = 0,0
headingTL = 0
leftTop = 0,0
headingLT = 0
leftBottom = 0,0
headingLB = 0

turtle.setheading(90)
turtle.circle(letterHeight / 8, int(180 - lineWidth / 2) )
returnPoint = turtle.position()
heading = turtle.heading()
turtle.circle(letterHeight / 8, lineWidth)
returnPoint1 = turtle.position()
heading1 = turtle.heading()
turtle.circle(letterHeight / 8, int(180 - lineWidth / 2) )

turtle.penup()
turtle.goto(returnPoint)
turtle.pendown()
turtle.begin_fill()
turtle.setheading(0)
turtle.forward(letterHeight / 8)
returnPoint = turtle.position()
turtle.setheading( 270 - (heading - 270) )
heading = turtle.heading()
turtle.circle(-letterHeight / 8, lineWidth)
turtle.setheading(180)
turtle.forward(letterHeight / 8)
turtle.setheading(heading1)
turtle.circle(letterHeight / 8, -lineWidth)
turtle.end_fill()

turtle.penup()
turtle.goto(returnPoint)
turtle.pendown()
turtle.setheading(heading - 180)
turtle.circle(letterHeight / 8, 90 - lineWidth)
rightBottom = turtle.position()
headingRB = turtle.heading()
turtle.circle(letterHeight / 8, lineWidth)
rightTop = turtle.position()
headingRT = turtle.heading()
turtle.circle(letterHeight / 8, 90 - lineWidth)
topRight = turtle.position()
headingTR = turtle.heading()
turtle.circle(letterHeight / 8, lineWidth)
topLeft = turtle.position()
headingTL = turtle.heading()
turtle.circle(letterHeight / 8, 90 - lineWidth)
leftTop = turtle.position()
headingLT = turtle.heading()
turtle.circle(letterHeight / 8, lineWidth)
leftBottom = turtle.position()
headingLB = turtle.heading()
turtle.circle(letterHeight / 8, 90 - lineWidth)
bottomLeft = turtle.position()
headingBL = turtle.heading()
turtle.circle(letterHeight / 8, lineWidth)
bottomRight = turtle.position()
headingBR = turtle.heading()

turtle.penup()
turtle.goto(rightBottom)
turtle.pendown()
turtle.begin_fill()
turtle.setheading(90)
turtle.forward(letterHeight / 8)
turtle.setheading(headingLB)
turtle.circle(letterHeight / 8, -lineWidth)
turtle.setheading(270)
turtle.forward(letterHeight / 8)
turtle.setheading(headingRT)
turtle.circle(letterHeight / 8, -lineWidth)
turtle.end_fill()

turtle.setheading(90)
turtle.forward(letterHeight / 8)
turtle.setheading(headingLB)
turtle.circle(letterHeight / 8, int(180 - lineWidth / 2) )
rightWall = turtle.xcor()
turtle.circle(letterHeight / 8, int(180 - lineWidth / 2) )

turtle.setheading(270)
turtle.forward(letterHeight / 8)
turtle.setheading(headingRT)
turtle.circle(letterHeight / 8, 90 - lineWidth)
turtle.begin_fill()
turtle.setheading(0)
turtle.forward(letterHeight / 8)
turtle.setheading(headingBR)
turtle.circle(letterHeight / 8, -lineWidth)
turtle.setheading(180)
turtle.forward(letterHeight / 8)
turtle.setheading(headingTL)
turtle.circle(letterHeight / 8, -lineWidth)
turtle.end_fill()

turtle.setheading(0)
turtle.forward(letterHeight / 8)
turtle.setheading(headingBR)
turtle.circle(letterHeight / 8, 360 - lineWidth)
turtle.setheading(180)
turtle.forward(letterHeight / 8)
turtle.setheading(headingTL)
turtle.circle(letterHeight / 8, 90 - lineWidth)

turtle.begin_fill()
turtle.setheading(270)
turtle.forward(letterHeight / 8)
turtle.setheading(headingRT)
turtle.circle(letterHeight / 8, -lineWidth)
turtle.setheading(90)
turtle.forward(letterHeight / 8)
turtle.setheading(headingLB)
turtle.circle(letterHeight / 8, -lineWidth)
turtle.end_fill()

turtle.setheading(270)
turtle.forward(letterHeight / 8)
turtle.setheading(headingRT)
turtle.circle(letterHeight / 8, 360 - lineWidth)
#END

turtle.penup()
turtle.goto(rightWall, -300)
turtle.pencolor("blue")
turtle.pendown()
turtle.setheading(0)
turtle.forward(600)
turtle.done()