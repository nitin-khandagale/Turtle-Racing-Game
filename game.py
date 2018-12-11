from turtle import *
from random import randint

# Lets make  a racetrack for turtles using Turtle library
speed(0)
penup()
goto(-100 , 50)
for step in range(11):
	write(step , align="center")
	right(90)
	forward(10)
	pendown()
	forward(150)
	penup()
	backward(160)
	left(90)
	forward(20)

# Now add some players which are ofcourse turtles

Akshay = Turtle()
Akshay.color("red")
Akshay.shape('turtle')
Akshay.penup()
Akshay.goto(-100 , 20)
Akshay.pendown()

Kartik = Turtle()
Kartik.color("green")
Kartik.shape('turtle')
Kartik.penup()
Kartik.goto(-100 , -10)
Kartik.pendown()

Nitin = Turtle()
Nitin.color("yellow")
Nitin.shape('turtle')
Nitin.penup()
Nitin.goto(-100 , -40)
Nitin.pendown()

Hrithik = Turtle()
Hrithik.color("blue")
Hrithik.shape('turtle')
Hrithik.penup()
Hrithik.goto(-100 , -70)
Hrithik.pendown()

#Make a list of all players so we can loop over it instead of moving them manually one by one.

players = [Akshay , Kartik , Nitin , Hrithik]

# Run a loop to move turtles random number of steps

for move in range(11):
  for player in players:
    player.forward(randint(1 , 11))
  
