# Python
# Autumn Knox
# Favorite math formual, plot it with two lists created.
# April 25th,

import matplotlib.pyplot as plt
import math
import numpy
"""Initalize the point of rays"""
x_values = []
y_values = []
"""The size of the triangle, and background style"""
triangle_side_len = 10
plt.style.use('dark_background')


"""Draw bottom line """
for t in range(triangle_side_len+1):
    x_values.append(t)
    y_values.append(0)

"""Draw rising line"""
for t in range(triangle_side_len+1):
    x_values.append(t/2)
    y_values.append(t)

"""Draw falling line"""
for t in range(triangle_side_len+1):
    x_values.append(triangle_side_len/2 + t/2)
    y_values.append(10 - t)

"""Graph the Triangle"""
figure, graph = plt.subplots()
graph.plot(x_values, y_values, linewidth=3, color='gold')

"""Added a title and x and y axis lables"""
graph.set_title('The Deathly Hallows', fontsize=8, loc='left', color='gold')
graph.set_xlabel('Power Output',fontsize=10, color='darkred')
graph.set_ylabel('Living Outcome', fontsize=10, color='limegreen')

"""Added text for visuals"""
plt.text(4.1,7, 'Invisablity Cloak', fontsize=7, color='lightgreen')
plt.text(1.5, 2, 'Ressurection Stone', fontsize=7, color='yellow')
plt.text(8.2,0.5, 'Elder Wand', fontsize=7, color='red')

plt.show()