import turtle
import os

# Создаем окно для игры
win = turtle.Screen()
win.title("Пинг-понг")
win.bgcolor("black")
win.setup(width=600, height=400)

# Создаем левую ракетку
left_pad = turtle.Turtle()
left_pad.speed(0)
left_pad.shape("square")
left_pad.color("white")
left_pad.shapesize(stretch_wid=6, stretch_len=1)
left_pad.penup()
left_pad.goto(-250, 0)

# Создаем правую ракетку
right_pad = turtle.Turtle()
right_pad.speed(0)
right_pad.shape("square")
right_pad.color("white")
right_pad.shapesize(stretch_wid=6, stretch_len=1)
right_pad.penup()
right_pad.goto(250, 0)

# Создаем мяч
ball = turtle.Turtle()
ball.speed(40)
ball.shape("circle")
ball.color("cyan")
ball.penup()
ball.goto(0, 0)
ball.dx = 2
ball.dy = -2

# Создаем счетчик очков
left_score = 0
right_score = 0
score = turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.hideturtle()
score.goto(0, 170)
score.write("Игрок 1: {}  Игрок 2: {}".format(left_score, right_score), align="center", font=("Courier", 14, "normal"))

# Функции для движения ракеток
def left_pad_up():
    y = left_pad.ycor()
    y += 20
    left_pad.sety(y)

def left_pad_down():
    y = left_pad.ycor()
    y -= 20
    left_pad.sety(y)

def right_pad_up():
    y = right_pad.ycor()
    y += 20
    right_pad.sety(y)

def right_pad_down():
    y = right_pad.ycor()
    y -= 20
    right_pad.sety(y)

# Назначаем клавиши для управления ракетками
win.listen()
win.onkeypress(left_pad_up, "w")
win.onkeypress(left_pad_down, "s")
win.onkeypress(right_pad_up, "Up")
win.onkeypress(right_pad_down, "Down")

# Основной цикл игры
while True:
    win.update()

    # Движение мяча
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Отскок мяча от верхней и нижней стенок
    if ball.ycor() > 190 or ball.ycor() < -190:
        ball.dy *= -1

    # Отскок мяча от ракеток
    if (ball.xcor() > 240 and ball.xcor() < 250) and (ball.ycor() < right_pad.ycor() + 50 and ball.ycor() > right_pad.ycor() - 50):
        ball.setx(240)
        ball.dx *= -1

    if (ball.xcor() < -240 and ball.xcor() > -250) and (ball.ycor() < left_pad.ycor() + 50 and ball.ycor() > left_pad.ycor() - 50):
        ball.setx(-240)
        ball.dx *= -1

    # Проверка на выход мяча за границы поля
    if ball.xcor() > 290:
        ball.goto(0, 0)
        ball.dy *= -1
        left_score += 1
        score.clear()
        score.write("Игрок 1: {}  Игрок 2: {}".format(left_score, right_score), align="center", font=("Courier", 14, "normal"))

    if ball.xcor() < -290:
        ball.goto(0, 0)
        ball.dy *= -1
        right_score += 1
        score.clear()
        score.write("Игрок 1: {}  Игрок 2: {}".format(left_score, right_score), align="center", font=("Courier", 14, "normal"))