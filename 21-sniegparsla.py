#!/bin/python3


import turtle
import random
anna = turtle.Turtle()

turtle.Screen().bgcolor("grey")
colours = ["cyan", "purple", "white", "blue"]

anna.penup()
anna.forward(90)
anna.left(45)
anna.pendown()

def branch():
    for i in range(3):
        for i in range(3):
            anna.forward(30)
        anna.backward(30)
        anna.right(45)
    anna.left(90)
    anna.backward(30)
    anna.left(45)
anna.right(90)
anna.forward(90)

for i in range(8):
    branch()
    anna.left(45)

#anna.color(random.choice(colours))
        


    
