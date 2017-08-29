from turtle import *
from random import randint

penup()

goto(-200,200) #coordinate where the race begins

for marker in range(15): #drawing meter markers

    if marker != 14: #there are 14m in total, marked every meter
    
        write(str(marker) + 'm', align='center')
        right(90)
        forward(10)
        pendown()
        forward(150)
        penup()
        backward(160)
        left(90)
        forward(20)

    else: #mark the finish line seperartely
    
        write("END", align='center')
        right(90)
        forward(10)
        pendown()
        forward(150)
        penup()
        backward(160)
        left(90)
        forward(20)
ht()

#drawing border across the race field 
border_cursor = Turtle()
border_cursor.penup()
border_cursor.goto(-230, 230)
border_cursor.pendown()
border_cursor.forward(360)
border_cursor.right(90)
border_cursor.forward(230)
border_cursor.right(90)
border_cursor.forward(360)
border_cursor.right(90)
border_cursor.forward(230)
border_cursor.penup()
border_cursor.ht()

#initializing player 1
red_turtle = Turtle()
red_turtle.color('red')
red_turtle.shape('turtle')
red_turtle.penup()
red_turtle.goto(-220,180)

#initializing player 2
blue_turtle = Turtle()
blue_turtle.color('blue')
blue_turtle.shape ('turtle')
blue_turtle.penup()
blue_turtle.goto(-220,140)

#initializing player 3
green_turtle = Turtle()
green_turtle.color('green')
green_turtle.shape('turtle')
green_turtle.penup()
green_turtle.goto(-220,100)

#initializing player 4
yellow_turtle = Turtle()
yellow_turtle.color('yellow')
yellow_turtle.shape('turtle')
yellow_turtle.penup()
yellow_turtle.goto(-220,60)

#set random speed for each turtle
for turn in range(100):
    red_turtle.forward(randint(1,5))
    blue_turtle.forward(randint(1,5))
    green_turtle.forward(randint(1,5))
    yellow_turtle.forward(randint(1,5))
    
