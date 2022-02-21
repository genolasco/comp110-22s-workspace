"""Custom House Portrait."""

__author__ = "730411655"

from turtle import Turtle, colormode, done 
colormode(255)


def main() -> None:
    """The entrypoint of my scene."""
    ertle: Turtle = Turtle()
    draw_hill(ertle, -500, -420)
    draw_rectangle(ertle, -100, 80)
    draw_rectangle_two(ertle, -20, -120)
    draw_triangle(ertle, -100, 80)
    draw_window(ertle, -80, 60)
    draw_window(ertle, 30, 60)
    
    done()


def draw_window(a_turtle: Turtle, x: float, y: float) -> None:
    """Draw a square located at x, y to create windows."""
    a_turtle.speed(50)
    a_turtle.penup()
    a_turtle.goto(x, y) 
    a_turtle.setheading(0.0)
    a_turtle.pendown()
    a_turtle.color(99, 204, 250)
    a_turtle.fillcolor("white")
    a_turtle.begin_fill()
    a_turtle.hideturtle()
    i: int = 0
    while i < 4:
        a_turtle.forward(50)
        a_turtle.right(90)
        i = i + 1
    a_turtle.end_fill()
    

def draw_hill(a_turtle: Turtle, x: float, y: float) -> None:
    """Draw a semi sircle to create a hill at x, y."""
    a_turtle.speed(50)
    a_turtle.penup()
    a_turtle.goto(x, y) 
    a_turtle.setheading(0.0)
    a_turtle.pendown()
    a_turtle.color("green")
    a_turtle.speed(50)
    a_turtle.begin_fill()
    a_turtle.hideturtle()
    i: int = 0
    while i < 1:
        a_turtle.right(90)
        a_turtle.circle(500, -180) 
        a_turtle.left(90)
        a_turtle.forward(1000)
        i = i + 1
    a_turtle.end_fill()


def draw_rectangle(a_turtle: Turtle, x: float, y: float) -> None:
    """Draw rectangle to create house at x,y."""
    a_turtle.speed(50)
    a_turtle.penup()
    a_turtle.goto(x, y) 
    a_turtle.setheading(0.0)
    a_turtle.pendown()
    a_turtle.color("brown")
    a_turtle.begin_fill()
    a_turtle.hideturtle()
    i: int = 0
    while i < 2:
        a_turtle.forward(200)
        a_turtle.right(90)
        a_turtle.forward(300)
        a_turtle.right(90)
        i = i + 1
    a_turtle.end_fill()


def draw_rectangle_two(a_turtle: Turtle, x: float, y: float) -> None:
    """Draw a smaller rectangle for the door."""
    a_turtle.speed(50)
    a_turtle.penup()
    a_turtle.goto(x, y) 
    a_turtle.setheading(0.0)
    a_turtle.pendown()
    a_turtle.color("black")
    a_turtle.begin_fill()
    a_turtle.hideturtle()
    i: int = 0
    while i < 2:
        a_turtle.forward(50)
        a_turtle.right(90)
        a_turtle.forward(100)
        a_turtle.right(90)
        i = i + 1
    a_turtle.end_fill()


def draw_triangle(a_turtle: Turtle, x: float, y: float) -> None:
    """Draw a roof for the house."""
    a_turtle.speed(50)
    a_turtle.penup()
    a_turtle.goto(x, y) 
    a_turtle.setheading(0.0)
    a_turtle.pendown()
    a_turtle.color("black")
    a_turtle.begin_fill()
    a_turtle.hideturtle()
    i: int = 0
    a_turtle.forward(200)
    while i < 2:
        a_turtle.left(120)
        a_turtle.forward(200)
        i = i + 1
    a_turtle.end_fill()


if __name__ == "__main__":
    main()