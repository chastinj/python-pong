import time
from turtle import Screen
from scoreboard import Scoreboard
from ball import Ball
from paddle import Paddle

rsPaddle = Paddle((350, 0))
lsPaddle = Paddle((-350, 0))
score = Scoreboard()
ball = Ball()


class GameBoard:
    def __init__(self):
        self.screen = Screen()
        self.screen.bgcolor("black")
        self.screen.setup(width=810, height=620)
        self.screen.title("Pong")
        self.screen.tracer(0)

    def startgame(self):
        game_is_on = True
        while game_is_on:
            time.sleep(ball.movespeed)
            self.screen.update()
            ball.move()

            # Detect wall collision
            if ball.ycor() > 280 or ball.ycor() < -280:
                ball.bounce_y()
            # Detect collision with paddles
            if ball.distance(rsPaddle) < 50 and ball.xcor() > 320 or \
                    ball.distance(lsPaddle) < 50 and ball.xcor() < -320:
                ball.bounce_x()

            #miss with rspaddle
            if ball.xcor() > 380:
                ball.reset_position()
                score.l_point()

            #miss with lspaddle
            if ball.xcor() < -380:
                ball.reset_position()
                score.r_point()

    def listen(self):
        self.screen.listen()
        self.screen.onkeypress(rsPaddle.go_up, "Up")
        self.screen.onkeypress(rsPaddle.go_down, "Down")
        self.screen.onkeypress(lsPaddle.go_up, "w")
        self.screen.onkeypress(lsPaddle.go_down, "s")

    def update(self):
        self.screen.update()

    def exitonclick(self):
        self.screen.exitonclick()
