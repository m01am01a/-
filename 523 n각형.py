
import turtle
t=turtle.Turtle()
t.shape("turtle")

def apple(length):
    for i in range(length):
        t.forward(400/length)
        t.left(360/length)

length=int(input("몇각형?: "))
apple(length)
