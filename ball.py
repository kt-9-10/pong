from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("circle")
        self.x_move = 5
        self.y_move = 5
        self.setheading(self.towards(1, 1))
        self.move_speed = 0.05

    def move(self):
        self.forward(8)

    def bounce_y(self):
        self.setheading(self.heading() * -1)

    def bounce_x(self, direction):
        self.setheading(direction)
        self.move_speed *= 0.8

    def reset_position(self, x, y):
        self.goto(0, 0)
        self.setheading(self.towards(x, y))
        self.move_speed = 0.05

