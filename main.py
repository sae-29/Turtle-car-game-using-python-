import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

player = Player()
Carmanager = CarManager()
score_board = Scoreboard()

score_board.score_board()

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
screen.onkey(fun = player.move_forward, key = "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    if player.ycor() > 370:
        player.reset_back()
        Carmanager.increment()
        score_board.increment_score()

    Carmanager.random_cars()
    Carmanager.move_cars() 

    for car in Carmanager.all_cars: 
        if car.distance(player) < 30:
            game_is_on = False
            player.game_over()



screen.exitonclick()


      