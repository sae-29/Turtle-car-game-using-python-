from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.score = 0

    def score_board(self):
        self.penup()
        self.hideturtle()
        self.goto(-650,340)
        self.write(f"Level = {self.score}" ,move = True ,align = "center" , font = ("Arial" , 30 , "normal")) 

    def increment_score(self):
        self.score += 1
        self.clear()
        self.score_board()  