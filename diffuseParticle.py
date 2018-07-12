"""
Diffuse on a canvas
Canvas borders are diffusion borders
"""

from tkinter import *
import random
import time

tk = Tk()
canvas = Canvas(tk, width=500, height=400)
tk.title("Diffuse particle")
canvas.pack()


num_of_balls = 10
balls = []

for i in range(num_of_balls):
    ball = canvas.create_oval(10, 10, 40, 40, fill='red')
    canvas.move(ball, 250, 200)
    balls.append(ball)


while True:
    for i in range(num_of_balls):
        xspeed = random.randint(-10, 10)
        yspeed = random.randint(-10, 10)


        pos = canvas.coords(balls[i])


        if pos[3] + yspeed >= 400:
            yspeed = -yspeed
        if pos[1] + yspeed <= 0:
            yspeed = -yspeed

        if pos[2] + xspeed >= 500:
            xspeed = -xspeed
        if pos[0] + xspeed <= 0:
            xspeed = -xspeed

        canvas.create_line((pos[0] + pos[2]) // 2, (pos[1] + pos[3]) // 2,
                           (pos[0] + pos[2]) // 2 + xspeed, (pos[1] + pos[3]) // 2 + yspeed)


        canvas.move(balls[i], xspeed, yspeed)


    tk.update()
    time.sleep(0.1)

tk.mainloop()


