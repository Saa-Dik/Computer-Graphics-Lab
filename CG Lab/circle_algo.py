# Write a program to implement Bresenham's circle drawing algorithm
import matplotlib.pyplot as plt

def plot_circle_points(xc, yc, x, y, points):
    # 8-way symmetry
    points.extend([
        (xc + x, yc + y),
        (xc - x, yc + y),
        (xc + x, yc - y),
        (xc - x, yc - y),
        (xc + y, yc + x),
        (xc - y, yc + x),
        (xc + y, yc - x),
        (xc - y, yc - x),
    ])

def bresenham_circle(xc, yc, r):
    x = 0
    y = r
    d = 3 - 2 * r
    points = []

    while x <= y:
        plot_circle_points(xc, yc, x, y, points)
        if d < 0:
            d = d + 4 * x + 6
        else:
            d = d + 4 * (x - y) + 10
            y -= 1
        x += 1

    return points

# Parameters
center_x = 0
center_y = 0
radius = 10

# Get circle points
circle_points = bresenham_circle(center_x, center_y, radius)

# Separate x and y for plotting
x_coords, y_coords = zip(*circle_points)

# Plot
plt.figure(figsize=(6,6))
plt.plot(x_coords, y_coords, 'ro')  # red dots
plt.gca().set_aspect('equal', adjustable='box')
plt.title(f"Bresenham's Circle (r={radius})")
plt.grid(True)
plt.show()


