from turtle import *
import turtle
import time
from food import Food
from snake import Snake

class Control:

    def __init__(self,ventana, snake, food):
        self.ventana = ventana
        self.snake: Snake = snake
        self.food: Food = food

        self.score = 0
        self.high_score = 0
        self.state_game = True

        self.marcador()


    def marcador(self):
        self.text = turtle.Turtle()
        self.text.speed(0)
        self.text.color("white")
        self.text.penup()
        self.text.hideturtle()
        self.text.goto(0,260)
        texto = "Score: {}   High Score: {}".format(self.score, self.high_score)
        self.text.write(texto , align = "center", font= ("Courier", 24, "normal"))

    def set_marcador(self):
        self.text.clear()
        texto = "Score: {}   High Score: {}".format(self.score, self.high_score)
        self.text.write(texto , align = "center", font = ("Courier", 24, "normal"))




    def listen_snake(self):
        wn = self.ventana
        wn.onkeypress(self.up, "Up")
        wn.onkeypress(self.down, "Down")
        wn.onkeypress(self.right, "Right")
        wn.onkeypress(self.left, "Left")
        wn.onkeypress(self.stop_play, "space")
        wn.listen()

    def up(self):
        self.state_game = True
        self.direction_snake("up")
        #print("arriba")

    def down(self):
        self.state_game = True
        self.direction_snake("down")

    def right(self):
        self.state_game = True
        self.direction_snake("right")

    def left(self):
        self.state_game = True
        self.direction_snake("left")
    
    def stop_play(self):
        self.state_game = False

    def direction_snake(self, direcction):
        snake = self.snake.head_snake
        
        while self.state_game:
            #self.colision_snake_body()
            self.colision_snake_food()
            self.colision_wall()
            self.snake.show_body(self.state_game)

            y = snake.ycor()
            x = snake.xcor()
            if direcction == "up":
                valor = y + 20
                snake.sety(valor)
            if direcction == "down":
                snake.sety(y - 20)
            if direcction == "right":
                snake.setx(x + 20)
            if direcction == "left":
                snake.setx(x - 20)
            time.sleep(0.1)
        

    def colision_snake_food(self):
        #print("entra a colision food {}".format(len(self.snake.body)))

        snake = self.snake.head_snake
        food = self.food.foods
        if snake.distance(food) < 20:
            self.food.position_food(food)
            self.snake.body_snake()
            self.score += 1
            self.set_marcador()

    def colision_wall(self):
        hs = self.snake.head_snake
        #print("entra a colision wall {}".format(len(self.snake.body)))
        if (hs.xcor() > 280 or hs.xcor() < -280 or hs.ycor() > 280 or hs.ycor() < -280):
            time.sleep(1)
            self.state_game = False
            for b in self.snake.body:
                b.hideturtle()
            self.snake.body.clear()
            #print(len(self.bo))
            if self.score > self.high_score:
                self.high_score = self.score
            self.score = 0
            self.set_marcador()
            hs.goto(0,0)
            return False
        return True



