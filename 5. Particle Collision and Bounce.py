from vpython import *

# Make two objects
redbox = box(pos=vector(0, 0, -1), size=vector(5, 5, 0.5), color=color.red, opacity=0.4)
particle = sphere(pos=vector(5, 0, 1), radius=0.3, color=color.cyan, make_trail=True)

# Initialize variables; create a new velocity property for the particle object
particle.v = vector(-0.5, 0, -0.3)
dt = 0.05
t = 0

# Box bounds for collision detection
box_min_x = redbox.pos.x - redbox.size.x / 2
box_max_x = redbox.pos.x + redbox.size.x / 2
box_min_y = redbox.pos.y - redbox.size.y / 2
box_max_y = redbox.pos.y + redbox.size.y / 2
box_front_z = redbox.pos.z + redbox.size.z / 2  # Front surface (higher z)

# Animation loop
while t < 20:
    # Control the animation frame rate
    rate(100)
    # Move the particle
    particle.pos = particle.pos + particle.v * dt
    
    # Check for collision with front surface of box
    if (particle.pos.z <= box_front_z + particle.radius and
        box_min_x <= particle.pos.x <= box_max_x and
        box_min_y <= particle.pos.y <= box_max_y):
        # Bounce: reverse z-velocity component
        particle.v.z = -particle.v.z
    
    t = t + dt

while True:
    pass