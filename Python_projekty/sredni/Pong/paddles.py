from turtle import Turtle , Screen


class Paddle(Turtle):

    def __init__(self):
        super().__init__()



    def create_paddles(self, position_x, position_y):
        self.color('white')
        self.shape('square')
        self.penup()
        self.shapesize(stretch_len=1 , stretch_wid=5)
        self.goto(position_x, position_y)


    def go_up(self):
        new_y = self.ycor() + 20
        new_x = self.xcor()
        self.goto(new_x, new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        new_x = self.xcor()
        self.goto(new_x, new_y)
