# Import libraries
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Change the Size of Graph using
# Figsize
fig = plt.figure(figsize=(10, 10))

# Generating a 3D sine wave
ax = plt.axes(projection='3d')

# Creating array points using
# numpy
x = np.arange(0, 20, 0.1)
y = np.sin(x)
z = y*np.sin(x)
c = x + y

# To create a scatter graph
ax.scatter(x, y, z, c=c)

# turn off/on axis
plt.axis('off')

# show the graph
plt.show()
from numpy import linspace
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d


# Creating 3D figure
fig = plt.figure(figsize=(8, 8))
ax = plt.axes(projection='3d')

# Creating Dataset
z = np.linspace(0, 15, 1000)
x = np.sin(z)
y = np.cos(z)
ax.plot3D(x, y, z, 'green')

# 360 Degree view
for angle in range(0, 360):
	ax.view_init(angle, 30)
	plt.draw()
	plt.pause(.001)

plt.show()
