# Write a program to implement Midpoint circle drawing algorithm
import matplotlib.pyplot as plt

def plot_circle_points(xc, yc, x, y, points):
    # 8-way symmetry points
    points.extend([
        (xc + x, yc + y),
        (xc - x, yc + y),
        (xc + x, yc - y),
        (xc - x, yc - y),
        (xc + y, yc + x),
        (xc - y, yc + x),
        (xc + y, yc - x),
        (xc - y, yc - x)
    ])

def midpoint_circle(xc, yc, r):
    x = 0
    y = r
    p = 1 - r
    points = []

    while x <= y:
        plot_circle_points(xc, yc, x, y, points)
        if p < 0:
            p = p + 2 * x + 3
        else:
            p = p + 2 * (x - y) + 5
            y -= 1
        x += 1

    return points

# Main part
if __name__ == "__main__":
    xc = int(input("Enter X coordinate of center: "))
    yc = int(input("Enter Y coordinate of center: "))
    r = int(input("Enter radius: "))

    circle_points = midpoint_circle(xc, yc, r)

    # Split x and y coordinates
    x_coords, y_coords = zip(*circle_points)

    # Plotting the circle
    plt.figure(figsize=(6,6))
    plt.plot(x_coords, y_coords, 'ro')  # red dots
    plt.title(f"Midpoint Circle (center=({xc}, {yc}), radius={r})")
    plt.gca().set_aspect('equal')
    plt.grid(True)
    plt.show()
