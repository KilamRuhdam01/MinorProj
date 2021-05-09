import numpy as np
x, y = np.meshgrid(np.linspace(-np.pi/2, np.pi/2, 30), np.linspace(-np.pi/2, np.pi/2, 30))
image = (np.sin(x**2+y**2)[1:-1,1:-2] > 0.9).astype(int) #boolean image
print(image)



#CONSTRUCTION OF HORIZONTAL EDGES
hx, hy = np.where(image[1:] & image[:-1]) #horizontal edge start positions

h_units = np.array([hx, hy]).T
print(h_units)
h_starts = [tuple(n) for n in h_units]
h_ends = [tuple(n) for n in h_units + (1, 0)] #end positions = start positions shifted by vector (1,0)
horizontal_edges = zip(h_starts, h_ends)

#CONSTRUCTION OF VERTICAL EDGES
vx, vy = np.where(image[:,1:] & image[:,:-1]) #vertical edge start positions
v_units = np.array([vx, vy]).T
v_starts = [tuple(n) for n in v_units]
v_ends = [tuple(n) for n in v_units + (0, 1)] #end positions = start positions shifted by vector (0,1)
vertical_edges = zip(v_starts, v_ends)