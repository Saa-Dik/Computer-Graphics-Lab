#Write a program to implement DDA(Digital Differential Analyzer) line drawing algorithm.
import matplotlib.pyplot as plt

def DDA(x1, y1, x2, y2):
    # Calculate dx and dy
    dx = x2 - x1
    dy = y2 - y1

    # Calculate steps
    steps = int(max(abs(dx), abs(dy)))

    # Calculate the increment in x and y
    x_inc = dx / steps
    y_inc = dy / steps

    # Store the line points
    x = x1
    y = y1
    points = []

    for _ in range(steps + 1):
        points.append((round(x), round(y)))
        x += x_inc
        y += y_inc

    return points

# Input start and end points
x_start = int(input("Enter x1: "))
y_start = int(input("Enter y1: "))
x_end = int(input("Enter x2: "))
y_end = int(input("Enter y2: "))

# Get the points using DDA
line_points = DDA(x_start, y_start, x_end, y_end)

# Display the points
print("Points on the line:")
for point in line_points:
    print(point)

# Plot the line using matplotlib
x_vals, y_vals = zip(*line_points)
plt.plot(x_vals, y_vals, marker='o', color='blue')
plt.title('DDA Line Drawing')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)
plt.axis('equal')
plt.show()
