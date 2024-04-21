from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, x_pos, y_pos):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(x_pos, y_pos)

    def go_up(self):
        self.goto(self.xcor(), self.ycor() + 10)

    def go_down(self):
        self.goto(self.xcor(), self.ycor() - 10)
