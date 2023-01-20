from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Arial' , 16 , 'normal')


class Scoreboard(Turtle):
    with open('data.txt', 'r') as f:
        h_score = int(f.read())

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = self.h_score
        self.color('white')
        self.penup()
        self.goto(0 , 270)
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}   High Score: {self.high_score}" , align=ALIGNMENT , font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('data.txt', 'w') as f:
                f.write(f'{self.high_score}')
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
