import matplotlib.pyplot as plt
import numpy as np

# Function to fill a rectangle using Scanline Fill Algorithm
def scanline_fill(rect):
    # Extract coordinates
    x_min, y_min = rect[0]
    x_max, y_max = rect[2]

    # Create an empty list to store filled pixels
    filled_pixels = []

    # Iterate over each scanline (horizontal line)
    for y in range(y_min, y_max + 1):
        for x in range(x_min, x_max + 1):
            filled_pixels.append((x, y))

    return filled_pixels

# Define rectangle as 4 vertices (bottom-left, bottom-right, top-right, top-left)
# Format: [(x1, y1), (x2, y2), (x3, y3), (x4, y4)]
rectangle = [(10, 10), (30, 10), (30, 20), (10, 20)]

# Get filled pixels
filled = scanline_fill(rectangle)

# Separate x and y coordinates for plotting
x_coords, y_coords = zip(*filled)

# Plot the filled rectangle
plt.figure(figsize=(6, 6))
plt.plot(*zip(*(rectangle + [rectangle[0]])), color='black')  # Draw rectangle outline
plt.scatter(x_coords, y_coords, color='skyblue', marker='s', s=100)  # Draw filled pixels
plt.gca().invert_yaxis()
plt.gca().set_aspect('equal', adjustable='box')
plt.title("Scanline Rectangle Fill")
plt.grid(True)
plt.show()
