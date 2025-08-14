from vpython import *

# Left Most
sphere(pos=vector(0, 1, 0), radius=0.5, color=color.green)
arrow(pos=vector(0, 1, 0), axis=vector(0, -1, 0), color=color.red, length=1)

# Middle
sphere(pos=vector(1, 3, 0), radius=0.5, color=color.green)
arrow(pos=vector(1, 3, 0), axis=vector(-1, 0, 0), color=color.red, length=1)

# Right
sphere(pos=vector(2, 1, 0), radius=0.5, color=color.green)
arrow(pos=vector(2, 1, 0), axis=vector(0, 1, 0), color=color.red, length=1)

# Prevents the program from exiting immediately
while True:
    pass