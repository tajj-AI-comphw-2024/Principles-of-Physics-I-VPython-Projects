from vpython import *


left=sphere(pos=vector(0, 1, 0), radius=0.5, color=color.green)
middle=sphere(pos=vector(1, 3, 0), radius=0.5, color=color.green)
right=sphere(pos=vector(2, 1, 0), radius=0.5, color=color.green)

# Left Arrow
arrow(pos=left.pos, axis=right.pos- left.pos, color=color.red)
# Middle Arrow
arrow(pos=middle.pos, axis=left.pos- middle.pos, color=color.red)
# Right Arrow
arrow(pos=right.pos, axis=middle.pos- right.pos, color=color.red)



while True:
    pass