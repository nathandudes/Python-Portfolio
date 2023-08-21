import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)

player = Player()
car = CarManager()
score = Scoreboard()

screen.listen()
screen.onkeypress(player.move_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_car()
    car.drive()
    score.update_score()

    # Detects if player collides with car
    for c in car.all_cars:
        if c.distance(player) < 25:
            game_is_on = False
            score.game_over()

    # UPDATES LEVEL IF PLAYER CROSSES
    if player.successful_run():
        score.level_up()
        player.reset()
        car.level_up()


screen.exitonclick()
