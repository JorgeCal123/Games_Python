from turtle import *
import turtle
import time
import random
class Main_Snake:

    def __init__(self):
        self.state_game = True
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

    def update_main_ventana(self, start):
        while start:
            self.ventana.update()

            self.move_snake()

    def colision_snake_food(self):
        if self.head_snake.distance(self.foods) < 20:
            self.position_food()

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
        wn.listen()


    def up(self):
        self.direction_snake("up")

    def down(self):
        self.direction_snake("down")

    def right(self):
        self.direction_snake("right")

    def left(self):
        self.direction_snake("left")


    def direction_snake(self, direcction):
        snake = self.head_snake
        while self.state_game:
            self.colision_snake_food()

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
