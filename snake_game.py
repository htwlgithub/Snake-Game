# Part 1: Getting Started
import turtle
import time
import random

DELAY = 0.1

# -------------
# Set up the screen
# -------------

win = turtle.Screen()
win.title("Snake Game by @EliasWei")
win.bgcolor("darkgrey")
win.setup(width=600, height=600)
win.tracer(0)

# ----------------------
# Snake head
# ----------------------
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("darkgreen")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# ----------------------
# Snake head
# ----------------------
food = turtle.Turtle()
food.speed(0)
food.shape("square")
food.color("red")
food.penup()
food.goto(0, 50)

# ----------------------
# Snake segment
# ----------------------
segments = []

# ----------------------
# Pen
# ----------------------
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0  Record : 0", align="center",
          font=("Arial", 18, "normal"))

# Score
score = 0
hight_score = 0


# -------------
# Change directions
# -------------


def go_up():
    if head.direction != "dowin":
        head.direction = "up"


def go_dowin():
    if head.direction != "up":
        head.direction = "dowin"


def go_left():
    if head.direction != "right":
        head.direction = "left"


def go_right():
    if head.direction != "left":
        head.direction = "right"


def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y+20)

    if head.direction == "dowin":
        y = head.ycor()
        head.sety(y-20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x-20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x+20)


# -----------------------------
# keyboard bindings
# --------------------------------
win.listen()
win.onkeypress(go_up, "w")
win.onkeypress(go_dowin, "s")
win.onkeypress(go_left, "a")
win.onkeypress(go_right, "d")


# -------------------------------
# Main game loop
# ---------------------------------
while True:
    win.update()

    # check for collision with the game border
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"

        # hide the segments
        for segment in segments:
            segment.goto(1000, 1000)

        # clear the segments list
        segments.clear()

        # reset score
        score = 0
        pen.clear()
        pen.write("Score: {}   Record: {}".format(score, hight_score), align="center",
                  font=("Arial", 18, "normal"))

        # snake eats the food
    if head.distance(food) < 20:
        # move the food to a random spot
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        time.sleep(DELAY)
        food.goto(x, y)

        # add segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("green")
        new_segment.penup()
        segments.append(new_segment)

        # increase the score
        score += 10

        if score > hight_score:
            hight_score = score

        # avoid overwrite
        pen.clear()
        pen.write("Score: {}   Record: {}".format(score, hight_score), align="center",
                  font=("Arial", 18, "normal"))

    # move the end segment fisrt in reverse order
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)

    # move the segment 0 to head
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    # call the function move
    move()

    # check for the head eat the body segments
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"

            # hide the segments
            for segment in segments:
                segment.goto(1000, 1000)

            # clear the segments list
            segments.clear()

            # reset score
            score = 0
            pen.clear()
            pen.write("Score: {}   Record: {}".format(score, hight_score), align="center",
                      font=("Arial", 18, "normal"))

    time.sleep(DELAY)
win.mainloop()
