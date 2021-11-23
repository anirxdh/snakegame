from turtle import Turtle


class Score (Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.write(f"Score: {self.score}", align="center",font=("Arial",17,"normal"))
        self.hideturtle()

    def update_score(self):
        self.write(f"Score: {self.score}", align="center", font=("Arial", 17, "normal"))

    def inc_score(self):
        self.score+=1
        self.clear()
        self.update_score()

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER ", align="center", font=("Arial", 25, "normal"))