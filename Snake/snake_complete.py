from turtle import *
import turtle
import time
import random
class Main_Snake:

    def __init__(self):
        self.state_game = True
        self.body = []
        self.score = 0
        self.high_score = 0
        self.text = turtle.Turtle()

        self.main_ventana()
        self.snake()
        self.move_snake()
        self.food()
        self.update_main_ventana(self.state_game)


    def main_ventana(self):
        # Creamos una ventana
        self.ventana = turtle.Screen()
        # titulo de la ventaana
        self.ventana.title("Snake JC")
        # color del fondo de la ventana
        self.ventana.bgcolor("black")
        # tamaño de la ventana
        self.ventana.setup(width=600, height=600)


    def update_main_ventana(self, start):
        self.marcador()
        while start:
            self.ventana.update()
            self.move_snake()


    def snake(self):
        # creamos el puntero
        self.head_snake = turtle.Turtle()
        # cambia velocidad del puntero
        self.head_snake.speed(0)
        # cambia la forma del puntero
        self.head_snake.shape("square")
        # quita el rastro del puntero
        self.head_snake.penup()
        # cambia la posicion
        self.head_snake.goto(0,0)
        # cambia el color del puntero
        self.head_snake.color("white")
        # direccion por defecto stop


    def body_snake(self):
        new_body = turtle.Turtle()
        new_body.speed(0)
        new_body.shape("square")
        new_body.penup()
        new_body.color("black")
        self.body.append(new_body)

    def show_body(self):
        size = len(self.body)
        for i in range(size - 1, 0, -1):
            x = self.body[i - 1].xcor()
            y = self.body[i - 1].ycor()
            self.body[i].goto(x,y)
            self.body[i].color("gray")

        if size > 0:
            x = self.head_snake.xcor()
            y = self.head_snake.ycor()
            self.body[0].goto(x,y)
            self.body[0].color("gray")


    def colision_snake_food(self):
        if self.head_snake.distance(self.foods) < 20:
            self.position_food()
            self.body_snake()
            self.score += 1
            self.marcador()

    def colision_snake_body(self):
        for bod in self.body:
            if bod.distance(self.head_snake) < 20:
                time.sleep(1)
                self.head_snake.goto(0,0)
                self.state_game= False
                self.body.clear()
                self.score = 0
                self.text.clear()
                texto = "Score: {}   High Score: {}".format(self.score, self.high_score)
                self.text.write(texto , align = "center", font= ("Courier", 24, "normal"))

    def position_food(self):
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        self.foods.goto(x,y)


    def move_snake(self):
        wn = self.ventana
        wn.onkeypress(self.up, "Up")
        wn.onkeypress(self.down, "Down")
        wn.onkeypress(self.right, "Right")
        wn.onkeypress(self.left, "Left")
        wn.onkeypress(self.stop_play, "space")
        wn.listen()


    def up(self):
        self.direction_snake("up")

    def down(self):
        self.direction_snake("down")

    def right(self):
        self.direction_snake("right")

    def left(self):
        self.direction_snake("left")
    
    def stop_play(self):
        if self.state_game == False:
           self.state_game = True
        else:
            self.state_game = False


    def direction_snake(self, direcction):
        snake = self.head_snake

        while self.state_game:

            self.colision_snake_food()
            self.colision_snake_body()
            self.check_wall()
            self.show_body()

            y = snake.ycor()
            x = snake.xcor()
            if direcction == "up":
                snake.sety(y + 20)
            if direcction == "down":
                snake.sety(y - 20)
            if direcction == "right":
                snake.setx(x + 20)
            if direcction == "left":
                snake.setx(x - 20)
            time.sleep(0.1)

    def food(self):
        self.foods = turtle.Turtle()
        self.foods.speed(0)
        self.foods.shape("circle")
        self.foods.penup()
        self.foods.color("red")
        self.position_food()

    def check_wall(self):
        hs = self.head_snake
        if (hs.xcor() > 280 or hs.xcor() < -280 or hs.ycor() > 280 or hs.ycor() < -280):
            time.sleep(1)
            hs.goto(0,0)
            self.state_game = False
            self.body.clear()
            self.score = 0

    
    def marcador(self):
        self.text.clear()
        self.text.speed(0)
        self.text.color("white")
        self.text.penup()
        self.text.hideturtle()
        self.text.goto(0,260)
        texto = "Score: {}   High Score: {}".format(self.score, self.high_score)
        self.text.write(texto , align = "center", font= ("Courier", 24, "normal"))
        
        #self.text.write("funciona")