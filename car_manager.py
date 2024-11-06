from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE
        
    def random_cars(self ):
            random_chance = random.randint(1,6)
            if random_chance == 2:
                new_cars = Turtle(shape = "square")
                new_cars.shapesize(1,2)
                new_cars.color(random.choice(COLORS))
                new_cars.penup()
                new_cars.goto(720, random.randint(-350 , 320))
                self.all_cars.append(new_cars)


    def move_cars(self ):
         for car in self.all_cars:
            car.backward(self.car_speed)

    def increment(self):
         self.car_speed += MOVE_INCREMENT
                   
         
                   
    


