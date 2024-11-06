from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape("turtle")
        self.left(90)
        self.speed('fastest')
        self.penup()
        self.goto(0 , -350)
        self.move_forward()


    def move_forward(self):
        self.forward(MOVE_DISTANCE)

    def winner(self):
        self.goto(0,0)
        self.write("YOU WIN!!" ,move = True ,align = "center" , font = ("Arial" , 30 , "normal")) 

    def reset_back(self):
        self.goto(0,-350)  
        self.move_forward() 

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER!!" ,move = True ,align = "center" , font = ("Arial" , 30 , "normal")) 

     
