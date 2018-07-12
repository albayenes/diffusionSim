"""
Diffuse in circle
"""

from tkinter import *
import time
import numpy as np
from numpy.random import randint

# create directory if not exists to save images
img_dir_name = "isotropicDiffusionImgDir"
import os
if not os.path.exists(img_dir_name):
    os.makedirs(img_dir_name)


tk = Tk()
canvas = Canvas(tk, width=500, height=400)
tk.title("Diffuse particle")
canvas.pack()

x1 = 0
y1 = 0
x2 = 300
y2 = 300
bounding_circle = canvas.create_oval(x1, y1, x2, y2, outline="black", width=2)
mx = 100
my = 50
canvas.move(bounding_circle, mx, my)
orig_x = mx + x2 // 2
orig_y = my + y2 // 2
r = orig_x - mx
# ball = canvas.create_oval(10, 10, 30, 30, fill='red')
# canvas.move(ball, orig_x, orig_y)


num_of_balls = 100
balls = []
for i in range(num_of_balls):
    ball = canvas.create_oval(0, 0, 5, 5, fill="#"+("%06x"%randint(0,16777215)))
    xstart = randint(101, 400)
    # calculate corresponding y axis of the points
    # randint for y resctricted using corresponing y values
    # it uses circle equation to calculate y values.
    corrsponding_y1 = (r**2 - (xstart - orig_x)**2)**(1/2.) * -1 + orig_y
    corrsponding_y2 = (r**2 - (xstart - orig_x)**2)**(1/2.) + orig_y
    ystart = randint(corrsponding_y1, corrsponding_y2)
    canvas.move(ball, xstart, ystart)
    balls.append(ball)

counter = 0
while True:
    for i in range(num_of_balls):
        # Random movement
        xspeed = randint(-10, 11)
        yspeed = randint(-10, 11)

        pos = canvas.coords(balls[i])

        # check each point with respect to radius
        # if greater than zero, it means points passes the circle
        # prevent go further
        if (((pos[0] + pos[2]) // 2 + xspeed - orig_x)**2 + ((pos[1] + pos[3]) // 2 + yspeed - orig_y)**2 - r**2) >= 0:
            if pos[0] < orig_x:
                xspeed = np.abs(xspeed)
            else:
                xspeed = np.abs(xspeed) * -1

            if pos[1] < orig_y:
                yspeed = np.abs(yspeed)
            else:
                yspeed = np.abs(yspeed) * -1

        canvas.move(balls[i], xspeed, yspeed)

    tk.update()
    canvas.postscript(file=img_dir_name + "/isotropicDiffusionCanvas_" + str(counter) + ".ps", colormode='color')
    print(img_dir_name + "/isotropicDiffusionCanvas_" + str(counter) + ".ps saved")
    counter += 1
    time.sleep(0.01)

tk.mainloop()


