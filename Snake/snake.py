from turtle import *
import turtle
import time
import random

class Snake:

    def __init__(self):
        self.snake()
        self.body: turtle.Turtle = []


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

    def show_body(self, state_game):
        size = len(self.body)
        print("show body {}".format(len(self.body)))
        if state_game:
            print(state_game)
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
