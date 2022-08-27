from tkinter import *

class Snake:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("hola mundo")

if __name__=="__main__":
    ventana = Tk()
    app = Snake(ventana)
    ventana.mainloop()
