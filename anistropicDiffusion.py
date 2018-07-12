"""
Diffuse in a tubular structure
"""

from tkinter import *
import time
import numpy as np
from numpy.random import randint

# create directory if not exists to save images
img_dir_name = "anisotropicDiffusionImgDir"
import os
if not os.path.exists(img_dir_name):
    os.makedirs(img_dir_name)

tk = Tk()
canvas = Canvas(tk, width=500, height=400)
tk.title("Diffuse particle")
canvas.pack()

# draw two lines as borders
x1 = 0
y1 = 0
x2 = 300
y2 = 0
bounding_line1 = canvas.create_line(x1, y1, x2, y2)
bounding_line2 = canvas.create_line(x1, y1, x2, y2)
mx = 100
my1 = 125
r = 50
my2 = my1 + r

# set poisition of borders
canvas.move(bounding_line1, mx, my1)
canvas.move(bounding_line2, mx, my2)

# create balls at random positions with
# random colors
num_of_balls = 20
balls = []
for i in range(num_of_balls):
    ball = canvas.create_oval(0, 0, 5, 5, fill="#"+("%06x"%randint(0,16777215)))
    xstart = randint(mx, mx + x2)
    ystart = randint(my1, my2)
    canvas.move(ball, xstart, ystart)
    balls.append(ball)

counter = 0
while True:
    for i in range(num_of_balls):
        # Random movement
        xspeed = randint(-10, 11)
        yspeed = randint(-10, 11)

        pos = canvas.coords(balls[i])

        # prevent crossing borders of the balls
        # in the y direction
        if pos[1] + yspeed <= my1:
            yspeed = np.abs(yspeed)
        elif pos[3] + yspeed >= my2:
            yspeed = np.abs(yspeed) * -1

        # if the ball goes away from the riht start
        # it from the right again
        # if the ball goes away from the left start
        # it from the left
        if pos[2] + xspeed > mx + x2:
            xspeed = xspeed - x2
        elif pos[0] + xspeed < mx:
            xspeed = xspeed + x2

        canvas.move(balls[i], xspeed, yspeed)

    tk.update()
    # save canvas to the folder
    canvas.postscript(file=img_dir_name + "/anisotropicDiffusionCanvas_" + str(counter) + ".ps", colormode='color')
    print(img_dir_name + "/anisotropicDiffusionCanvas_" + str(counter) + ".ps saved")
    counter += 1
    time.sleep(0.01)

tk.mainloop()
