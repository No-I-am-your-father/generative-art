# Python, generative art project
# The Recamán Sequence

import turtle

window = turtle.Screen()
window.setup(width=800, height=600, startx=10, starty=0.5)
recaman = turtle.Turtle()
scale = 5

recaman.penup()
recaman.setpos(-390, 0)
recaman.pendown()

current = 0
seen = set()

for step_size in range(1, 100):

    backwards = current - step_size

    if backwards > 0 and backwards not in seen:
        recaman.setheading(90)
        recaman.circle(step_size/2, 180)
        current = backwards
        seen.add(current)
    
    else:
        recaman.setheading(270)
        recaman.circle(step_size/2, 180)
        current += step_size
        seen.add(current)

turtle.done()