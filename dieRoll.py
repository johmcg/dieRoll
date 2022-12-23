import random
import turtle
import time

def square():
        turtle.hideturtle()
        turtle.speed(0)
        turtle.width(20)
        turtle.forward(90)
        turtle.right(90)
        turtle.forward(90)
        turtle.right(90)
        turtle.forward(90)
        turtle.right(90)
        turtle.forward(90)
        turtle.right(90)


def dots():
        time.sleep(.1)
        dieValue = random.randint(1,6)
        turtle.hideturtle()
        turtle.speed(0)
        if dieValue == 1:
                turtle.penup()
                turtle.goto(0,0)
                turtle.write('.', font=("Times New Roman", 50, "bold"))
        if dieValue == 2:
                turtle.penup()
                turtle.goto(-20,20)
                turtle.write('.', font=("Times New Roman", 50, "bold"))
                turtle.penup()
                turtle.goto(20,-20)
                turtle.write('.', font=("Times New Roman", 50, "bold"))
        if dieValue == 3:
                turtle.penup()
                turtle.goto(-20,-20)
                turtle.write('.', font=("Times New Roman", 50, "bold"))
                turtle.penup()
                turtle.goto(0,0)
                turtle.write('.', font=("Times New Roman", 50, "bold"))
                turtle.penup()
                turtle.goto(20,20)
                turtle.write('.', font=("Times New Roman", 50, "bold"))
        if dieValue == 4:
                turtle.penup()
                turtle.goto(-20,20)
                turtle.write('.', font=("Times New Roman", 50, "bold"))
                turtle.penup()
                turtle.goto(-20,-20)
                turtle.write('.', font=("Times New Roman", 50, "bold"))
                turtle.penup()
                turtle.goto(20,20)
                turtle.write('.', font=("Times New Roman", 50, "bold"))
                turtle.penup()
                turtle.goto(20,-20)
                turtle.write('.', font=("Times New Roman", 50, "bold"))
        if dieValue == 5:
                turtle.penup()
                turtle.goto(-20,20)
                turtle.write('.', font=("Times New Roman", 50, "bold"))
                turtle.penup()
                turtle.goto(-20,-20)
                turtle.write('.', font=("Times New Roman", 50, "bold"))
                turtle.penup()
                turtle.goto(20,20)
                turtle.write('.', font=("Times New Roman", 50, "bold"))
                turtle.penup()
                turtle.goto(20,-20)
                turtle.write('.', font=("Times New Roman", 50, "bold"))
                turtle.penup()
                turtle.goto(0,0)
                turtle.write('.', font=("Times New Roman", 50, "bold"))
        if dieValue == 6:
                time.sleep(.1)
                turtle.penup()
                turtle.goto(-20,20)
                turtle.write('.', font=("Times New Roman", 50, "bold"))
                turtle.penup()
                turtle.goto(-20,0)
                turtle.write('.', font=("Times New Roman", 50, "bold"))
                turtle.penup()
                turtle.goto(-20,-20)
                turtle.write('.', font=("Times New Roman", 50, "bold"))
                turtle.penup()
                turtle.goto(20,20)
                turtle.write('.', font=("Times New Roman", 50, "bold"))
                turtle.penup()
                turtle.goto(20,0)
                turtle.write('.', font=("Times New Roman", 50, "bold"))
                turtle.penup()
                turtle.goto(20,-20)
                turtle.write('.', font=("Times New Roman", 50, "bold"))

def roll(x,y):
        turtle.clear()
        turtle.hideturtle()
        turtle.penup()
        turtle.goto(-34,64)
        turtle.pendown()
        time.sleep(.4)
        square()
        dots()
        


roll(0,0) ## beginning roll
turtle.Screen().onclick(roll) ##new roll
turtle.mainloop() 
