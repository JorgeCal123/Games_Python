from turtle import *
import turtle
import time
from food import Food
from snake import Snake
from controls import Control

def main_ventana():
    # Creamos una ventana
    ventana = turtle.Screen()
    # titulo de la ventaana
    ventana.title("Snake JC")
    # color del fondo de la ventana
    ventana.bgcolor("black")
    # tamaño de la ventana
    ventana.setup(width=600, height=600)

    return ventana

if __name__=="__main__":
    wn = main_ventana()
    snake = Snake()
    food = Food()
    control = Control(wn, snake, food)
    control.listen_snake()

    done()

