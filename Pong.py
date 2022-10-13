import turtle

window = turtle.Screen()
window.bgcolor("Black")
window.setup(height=600, width=800)
window.tracer(0)

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.color("white")
paddle_a.shape("square")
paddle_a.shapesize(stretch_len=1, stretch_wid=4)
paddle_a.penup()
paddle_a.goto(-350, 0)
paddle_a.write("A")

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.color("white")
paddle_b.shape("square")
paddle_b.shapesize(stretch_len=1, stretch_wid=4)
paddle_b.penup()
paddle_b.goto(350, 0)
paddle_b.write("B")

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.color("white")
ball.shape("circle")
# ball.shapesize(stretch_len=1, stretch_wid=4)
ball.penup()
ball.goto(0, 0)
ball.dx = 0.2
ball.dy = 0.2

# Player A
pA = 0
penA = turtle.Turtle()
penA.speed(0)
penA.color("white")
penA.penup()
penA.hideturtle()
penA.goto(-320, 265)
penA.write("Player A: 0",align="center", font=("Arial",20,"bold"))

# Player B
pB=0
penB = turtle.Turtle()
penB.speed(0)
penB.color("white")
penB.penup()
penB.hideturtle()
penB.goto(300, 265)
penB.write("Player B: 0",align="center", font=("Arial",20,"bold"))

ball_speed=1

speed = turtle.Turtle()
speed.speed(0)
speed.color("White")
speed.penup()
speed.hideturtle()
speed.goto(0,265)
speed.write(ball_speed,"X", align="center", font=("Arial",20,"bold"))

def paddle_a_up():
    y = paddle_a.ycor()
    y = y + 20
    if y > 260:
        return
    paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()
    y = y - 20
    if y < -260:
        return
    paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()
    y = y + 20
    if y > 260:
        return
    paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()
    y = y - 20
    if y < -260:
        return
    paddle_b.sety(y)

def speed_plus():
    ball.dx = ball.dx*2
    speed.clear()
    global ball_speed
    ball_speed+=1
    speed.write(str(ball_speed)+"X", align="center", font=("ariel",20, "bold"))
def speed_minus():
    ball.dx = ball.dx/2
    speed.clear()
    global ball_speed
    ball_speed -= 1
    speed.write(str(ball_speed)+"X", align="center", font=("ariel", 20, "bold"))

window.listen()
window.onkeypress(lambda: paddle_a_up(), "w")
window.onkeypress(lambda: paddle_a_down(), "s")
window.onkeypress(lambda: paddle_b_up(), "Up")
window.onkeypress(lambda: paddle_b_down(), "Down")
window.onkey(speed_plus, "plus")
window.onkey(speed_minus, "minus")

while True:
    window.update()
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() > 280:
        ball.dy = ball.dy * -1

    if ball.ycor() < -280:
        ball.dy = ball.dy * -1
    if ball.xcor() > 390:
        ball.goto(0, 0)
        penB.clear()
        pB+=1
        penB.write("Player B: "+str(pB),align="center", font=("Arial",20,"bold"))
        ball.dx *= -1
    if ball.xcor() < -390:
        ball.goto(0, 0)
        penA.clear()
        pA+=1
        penA.write("Player A: "+str(pA),align="center", font=("Arial",20,"bold"))
        ball.dx *= -1
    if (ball.xcor() > 350 and
            paddle_b.ycor() + 50 > ball.ycor() > paddle_b.ycor() - 50
    ):
        ball.dx *= -1
        # ball.dy *= -1

    if (ball.xcor() < -350 and
            paddle_a.ycor() + 50 > ball.ycor() > paddle_a.ycor() - 50
    ):
        ball.dx *= -1
        # ball.dy *= -1