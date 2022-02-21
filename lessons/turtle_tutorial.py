"""Exercise three turtle tutoiral."""


from turtle import Turtle, colormode, done
colormode(255)
leo: Turtle = Turtle()
leo.color(99, 204, 250)
leo.fillcolor("pink")
leo.speed(50)
leo.hideturtle()
i: int = 0
while (i < 4):
    leo.forward(300)
    leo.left(90)
    i = i + 1

leo.penup()
leo.goto(45, 60)
leo.pendown()
i: int = 0
leo.begin_fill()
while (i < 3):
    leo.forward(300)
    leo.left(120)
    i = i + 1
leo.end_fill()

bob: Turtle = Turtle()
bob.color(9, 7, 6)
bob.speed(100)
bob.penup()
bob.goto(45, 60)
bob.pendown()
side_length: float = 300.0

i: int = 0
while (i < 50):
    bob.forward(side_length)
    bob.left(120)
    side_length = side_length * .98
    i = i + 1

bob.circle(50)
bob.position()
(-0.00, 0.00)
done()