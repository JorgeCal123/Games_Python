from turtle import *
import turtle
import random


class Food:

    def __init__(self):
        self.food()

    def food(self):
        self.foods = turtle.Turtle()
        self.foods.speed(0)
        self.foods.shape("circle")
        self.foods.penup()
        self.foods.color("red")
        self.position_food(self.foods)

    def position_food(self, food):
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        food.goto(x,y)
