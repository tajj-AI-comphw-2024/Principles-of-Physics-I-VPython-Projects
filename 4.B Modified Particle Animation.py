from vpython import *

# Make two objects
redbox = box(pos=vector(0, 0, -1), size=vector(5, 5, 0.5), color=color.red, opacity=0.4)
particle = sphere(pos=vector(5, 0, 0), radius=0.3, color=color.cyan, make_trail=True)

# Initialize variables; create a new velocity property for the particle object
particle.v = vector(-0.5, 0, 0)
dt = 0.05
t = 0

# Animation loop
while t < 20:
    # Control the animation frame rate
    rate(100)
    # Move the particle
    particle.pos = particle.pos + particle.v * dt
    t = t + dt

while True:
    pass