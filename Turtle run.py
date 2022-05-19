from cgitb import text
import turtle as t
import random
score = 0
playing = False
te = t.Turtle()
te.shape("turtle")
te.shapesize(2, 2, 3)
te.color("red")
te.speed(0)
te.up()
te.goto(0, 200)
ts = t.Turtle()
ts.shape("circle")
ts.shapesize(2, 2, 3)
ts.speed(0)
ts.up()
ts.goto(0, -200)
def turn_right():
    t.setheading(0)
def turn_up():
    t.setheading(90)
def turn_lift():
    t.setheading(180)
def turn_down():
    t.setheading(270)
def start():
    global playing
    if playing == False:
        playing = True
        t.cleas()
        play()
def play():
    global score
    global playing
    t.forward(10)
    if random. random(1, 5) == 3:
        ang = te.towards(t.pos())
        te.setheading(ang)
    speed = score + 5
def play():
    global score
    global playing
    t.forward(10)
    if random. random(1, 5) == 3:
        ang = te.towards(t.pos())
        te.setheading(ang)
    speed = score + 5
    if speed > 15:
        speed = 15
    te.forward(speed)
    if t.distance(te) < 12:
        text = "Score: " + str(score)
        message("Game over" , text)
        playing = False
        score = 0
    if t.distance(te)< 12:
        score = score + 1
        t.write(score)
        star_x = random.randint(-230 , 230)
        star_y = random.randint(-230 ,230)
        ts.goto(star_x, star_y)
    if playing:
        t.ontimer(play, 100)
def message(m1, m2):
    t.clear()
    t.goto(0, 100)
    t.write(m1 , False , "center" , ("",20))
    t.goto(0, -100)
    t.write(m2 , False , "center" , ("",15)) 
    t.home()
    t.title("Turtle Run")
    t.setup(500, 500)
    t.bgcolor("orange")
    t.shape("tultre")
    t.shapesize(2, 2, 3)
    t.speed(0)
    t.up()
    t.color("write")
    t.onkeypress(turn_right, "Right")
    t.onkeypress(turn_up, "Up")
    t.onkeypress(turn_down, "Down")
    t.onkeypress(turn_left, "Left")
    t.onkeypress(start, "space")
    t.listen()
    message("Turtle Run","[space]")