#Creation of a simple game named pong - its my third project 
# it is a code along by @TokyoEdTech

import turtle

wn = turtle.Screen()
wn.title("Pong game by Michal, thanks to tutor @TokyoEdTech")
wn.bgcolor("red")
wn.setup(width=800, height=600)
wn.tracer(0)


# cretion od the first object - Paddle A 

paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350,0) # placement of the paddle 

# cretion od the 2nd object - Paddle B

paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350,0) # placement of the paddle 


#ball

ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0,0) # placement of the ball 
ball.dx = 4
ball.dy = 4 


#functions to move paddles 

def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)



#keyboard binding

wn.listen() #this listens to the keyboard
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

#main game loop

while True:
    wn.update() 

    #movin mechanizm
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #border checking

    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    elif ball.ycor() <  -290:
        ball.sety(-290)
        ball.dy *= -1

    elif ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1
    
    elif ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1

    