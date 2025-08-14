from vpython import *

# Function to create dotted axis
# Used python annotation to specify types of parameters
# start: starting position of the axis
# end: ending position of the axis
# step: step size for the axis
# axis_dir: direction of the axis ('x', 'y', or 'z')
# color_val: color of the boxes representing the axis

def create_dotted_axis(start : int, end : int, step : int, axis_dir : chr, color_val : color):
    # Pos val starts at 0 ends at given end value, increments by given step value
    for pos_val in range(start, end + 1, step):
        if axis_dir == 'x':
            pos = vector(pos_val, 0, 0)
            size = vector(0.4, 0.1, 0.1)
        elif axis_dir == 'y':
            pos = vector(0, pos_val, 0)
            size = vector(0.1, 0.4, 0.1)
        else: # axis_dir == 'z'
            pos = vector(0, 0, pos_val)
            size = vector(0.1, 0.1, 0.4)
        box(pos=pos, size=size, color=color_val)

# Will add up to 11 boxes in each direction
# Function calls to create dotted axes
# create_dotted_axis (x,y,z,axis direction, color)
create_dotted_axis(-5, 5, 1, 'x', color.red)

# Y-axis (green, dotted)
create_dotted_axis(-5, 5, 1, 'y', color.green)

# Z-axis (blue, dotted)
create_dotted_axis(-5, 5, 1, 'z', color.blue)

while True:
    pass