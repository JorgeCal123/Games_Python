from turtle import *
import turtle
import time

class Main_Snake:

    def __init__(self):
        self.main_ventana()
        self.snake()
        self.move_snake()
        self.update_main_ventana(True)


    
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
        self.head_snake.direction = "stop"

    def update_main_ventana(self, start):
        while start:
            self.ventana.update()
            #self.direction_snake("right")
            self.move_snake()
            time.sleep(0.1)

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

            


