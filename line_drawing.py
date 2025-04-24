# Write a program to implement Bresenham's line drawing algorithm.
import matplotlib.pyplot as plt

def bresenham_line(x1, y1, x2, y2):
    points = []

    # Calculate deltas
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)

    # Determine the direction of step
    sx = 1 if x2 > x1 else -1
    sy = 1 if y2 > y1 else -1

    x, y = x1, y1

    if dx > dy:
        err = dx // 2
        while x != x2:
            points.append((x, y))
            err -= dy
            if err < 0:
                y += sy
                err += dx
            x += sx
    else:
        err = dy // 2
        while y != y2:
            points.append((x, y))
            err -= dx
            if err < 0:
                x += sx
                err += dy
            y += sy

    points.append((x2, y2))  # Add the last point
    return points

# Example coordinates
x_start, y_start = 2, 3
x_end, y_end = 10, 8

# Get the list of points from Bresenham's algorithm
line_points = bresenham_line(x_start, y_start, x_end, y_end)

# Plotting the points
x_coords, y_coords = zip(*line_points)
plt.figure(figsize=(6, 6))
plt.plot(x_coords, y_coords, marker='o', color='green')
plt.title("Bresenham's Line Drawing Algorithm")
plt.grid(True)
plt.axis('equal')
plt.show()
